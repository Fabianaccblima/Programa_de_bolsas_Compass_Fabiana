import requests
import json
import os
import time
import boto3

# Chave de API do TMDb
api_key = 

# Função para buscar detalhes do filme
def buscar_detalhes_filme(movie_id, tentativas=3, delay=5):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"
    for tentativa in range(tentativas):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Levanta um erro se o status code não for 200
            dados = response.json()
            return {
                "nome": dados.get("title"),
                "ano": dados.get("release_date", "")[:4],
                "popularidade": dados.get("popularity"),
                "nota_media": dados.get("vote_average"),
                "votos": dados.get("vote_count"),
                "orcamento": dados.get("budget"),
                "receita": dados.get("revenue"),
                "runtime": dados.get("runtime"),
                "generos": [g["name"] for g in dados.get("genres", [])]
            }
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados do filme (tentativa {tentativa + 1}): {e}")
            if tentativa < tentativas - 1:
                print(f"Tentando novamente após {delay} segundos...")
                time.sleep(delay)  # Espera antes de tentar novamente
            else:
                print("Falha ao buscar dados após várias tentativas.")
                return None

# Função para buscar filmes por década e gênero
def buscar_filmes_por_decada_genero(decada_inicio, decada_fim, generos, page=1, tentativas=3, delay=5):
    filmes = []
    # Buscando filmes entre decada_inicio e decada_fim
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&primary_release_date.gte={decada_inicio}-01-01&primary_release_date.lte={decada_fim}-12-31&with_genres={generos}&page={page}"
    
    for tentativa in range(tentativas):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Levanta um erro se o status code não for 200
            for item in response.json().get("results", []):
                detalhes = buscar_detalhes_filme(item["id"])
                if detalhes:
                    filmes.append(detalhes)
            return filmes
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar filmes para a década {decada_inicio}-{decada_fim} (tentativa {tentativa + 1}): {e}")
            if tentativa < tentativas - 1:
                print(f"Tentando novamente após {delay} segundos...")
                time.sleep(delay)  # Espera antes de tentar novamente
            else:
                print("Falha ao buscar filmes após várias tentativas.")
                return filmes

# Função para calcular a média de popularidade, votos, orçamento e receita
def calcular_media_analise(filmes):
    if not filmes:
        return {
            "media_popularidade": 0,
            "media_nota": 0,
            "media_votos": 0,
            "media_orcamento": 0,
            "media_receita": 0
        }
    
    total_popularidade = sum([filme["popularidade"] for filme in filmes])
    total_votos = sum([filme["votos"] for filme in filmes])
    media_nota = sum([filme["nota_media"] for filme in filmes]) / len(filmes)
    total_orcamento = sum([filme["orcamento"] for filme in filmes if filme["orcamento"] > 0])
    total_receita = sum([filme["receita"] for filme in filmes if filme["receita"] > 0])
    
    return {
        "media_popularidade": total_popularidade / len(filmes),
        "media_votos": total_votos / len(filmes),
        "media_nota": media_nota,
        "media_orcamento": total_orcamento / len(filmes) if total_orcamento > 0 else 0,
        "media_receita": total_receita / len(filmes) if total_receita > 0 else 0
    }

# IDs de gêneros (comédia = 35, romance = 10749)
generos_comedia_romance = "35,10749"

# Função para salvar a análise por década e fazer upload para o S3
def salvar_analise_por_decada(decada_inicio, decada_fim, filmes, analise):
    # Diretório onde os arquivos JSON serão salvos
    output_dir = '/tmp/analises_por_decada'  # Usando /tmp para Lambda (no ambiente AWS Lambda, /tmp é o único diretório gravável)
    os.makedirs(output_dir, exist_ok=True)

    dados_analise = {
        "decada": f"{decada_inicio}s",
        "total_filmes_encontrados": len(filmes),
        "media_popularidade": analise["media_popularidade"],
        "media_votos": analise["media_votos"],
        "media_nota": analise["media_nota"],
        "media_orcamento": analise["media_orcamento"],
        "media_receita": analise["media_receita"],
        "filmes_comedia_romance": filmes
    }

    # Salvando os dados no formato de arquivo JSON para a década específica
    file_path = os.path.join(output_dir, f"analise_filmes_comedia_romance_{decada_inicio}s_{decada_fim}s.json")
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(dados_analise, json_file, ensure_ascii=False, indent=4)

    print(f"Análise para a década de {decada_inicio}-{decada_fim} salva localmente em '{file_path}'")

    # Agora, fazer o upload do arquivo para o S3
    s3 = boto3.client('s3')
    bucket_name = 'data-lake-de-fabiana'  # Substitua com o nome do seu bucket S3

    # Caminho do arquivo no S3
    s3_key = f"raw/tmdb/json/2024/11/17/{os.path.basename(file_path)}"
    
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"Arquivo enviado para o S3 com sucesso: s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Erro ao enviar o arquivo para o S3: {e}")

# Função lambda_handler que será chamada pela AWS Lambda
def lambda_handler(event, context):
    # Loop para percorrer as décadas de 1980 a 2020
    for decada_inicio in range(1984, 2023, 10):
        decada_fim = decada_inicio + 9
        filmes_comedia_romance = buscar_filmes_por_decada_genero(decada_inicio, decada_fim, generos_comedia_romance)
        analise = calcular_media_analise(filmes_comedia_romance)
        
        # Salvar os dados da análise para a década e fazer upload para o S3
        salvar_analise_por_decada(decada_inicio, decada_fim, filmes_comedia_romance, analise)

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }
