## OBJETIVOS DA SPRINT

#### Nesta Sprint, os principais objetivos foram:

## Exercícios

1. Apache Spark:

Neste exercício, meu objetivo foi configurar um ambiente com Apache Spark para processar dados e realizar a contagem de palavras no arquivo README.md do meu repositório Git. Primeiro, fiz o pull da imagem spark/all-spark-notebook para criar o contêiner com Spark. Em seguida, utilizei o terminal do Spark (pyspark) dentro do contêiner, onde executei os comandos necessários para analisar o arquivo linha a linha. Por fim, no terminal do Spark, apliquei a sequência de comandos para contar as ocorrências de cada palavra no arquivo, praticando o uso do Spark para manipulação de dados.

2. Lab Glue:

Neste exercício, desenvolvi um job no AWS Glue para processar o arquivo nomes.csv no S3. Após fazer o upload do arquivo, li os dados, ajustei a coluna nome para maiúsculas, calculei a contagem de linhas, agrupei por ano e sexo, e ordenei os dados por ano. Também identifiquei os nomes masculino e feminino mais frequentes e gravei o resultado no S3 em formato JSON, particionado por sexo e ano.
Em seguida, configurei e executei um crawler no Glue para criar automaticamente a tabela frequencia_registro_nomes_eua no catálogo de dados, vinculando-a ao bucket S3. Finalizei verificando a tabela no Glue Catalog e no Athena.

3. TMDB

Criei uma conta no TMDb e obtive minha chave de API para acessar os dados relacionados aos filmes de comédia romântica para a análise que estou realizando.

[Exercícios](./Exercicios)

## Desafio

O objetivo do desafio foi criar uma função Lambda no AWS para processar filmes de comédia, com base na minha análise, buscando informações na API do TMDb. Inicialmente, criei a função no Lambda. Para incluir as dependências, criei um Dockerfile, construí uma imagem Docker e instalei as bibliotecas necessárias (requests e boto3). Após compactar e fazer o upload da camada para o S3, associei-a à função Lambda. Em seguida, criei uma política de permissões no IAM para garantir o acesso ao S3. No Lambda, desenvolvi o código, criando funções para buscar os filmes, obter os dados da análise e salvar os resultados em arquivos JSON. Os dados processados foram enviados para o S3, e o resultado final foi verificado no meu data lake no S3, onde os arquivos foram armazenados com sucesso.

[Desafio](./desafio)