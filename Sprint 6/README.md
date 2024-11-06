## OBJETIVOS DA SPRINT

#### Nesta Sprint, os principais objetivos foram:

#### Cursos de Analytics na AWS
1. Fundamentals of Analytics on AWS – Parte 1 (Português):

Abordou os conceitos fundamentais de análise de dados na AWS, com foco nas ferramentas e serviços principais para armazenar, processar e analisar grandes volumes de dados.

2. Fundamentals of Analytics on AWS – Parte 2 (Português):

Dando sequência à Parte 1, este curso aprofundou as práticas recomendadas, as arquiteturas de soluções e a integração entre os serviços AWS para análise de dados.

3. AWS Skill Builder - Serverless Analytics (Português):

Explorou como realizar análises de dados sem gerenciar servidores, utilizando serviços como AWS Lambda, Amazon Athena e Amazon S3 para criar soluções escaláveis e econômicas.

4. AWS Skill Builder - Introduction to Amazon Athena (Português):

Explicou a usar o Amazon Athena para consultas interativas em dados armazenados no Amazon S3, sem necessidade de infraestrutura de servidor.

5. AWS Skill Builder - AWS Glue Getting Started:

Introdução ao AWS Glue, um serviço de ETL (Extração, Transformação e Carregamento) que facilita a preparação e o carregamento de dados para análise em diversos sistemas de armazenamento da AWS.

6. AWS Skill Builder - Amazon EMR Getting Started:

Explicou a usar o Amazon EMR (Elastic MapReduce) para processar grandes volumes de dados com frameworks como Apache Hadoop, Apache Spark e Apache Hive.

7. AWS Skill Builder - Getting Started with Amazon Redshift:

Introdução ao Amazon Redshift, um serviço de data warehouse totalmente gerenciado que facilita a análise de grandes volumes de dados com alta performance.

8. AWS Skill Builder - Best Practices for Data Warehousing with Amazon Redshift:

Explicou as melhores práticas para criar, gerenciar e otimizar data warehouses no Amazon Redshift, melhorando a performance e reduzindo custos.

9. AWS Skill Builder - Amazon QuickSight - Getting Started:

Explicou como utilizar o Amazon QuickSight para criar visualizações interativas e painéis de controle a partir de dados armazenados na AWS, facilitando a análise e a tomada de decisões.

[Certificados](./Certificados)


## Exercícios

1. Lab AWS S3

O objetivo deste exercício foi ensinar como configurar um bucket no Amazon S3 para funcionar como hospedagem de conteúdo estático. Onde aprendi a criar um bucket, habilitar a hospedagem de site estático, configurar documentos de índice e erro, ajustar as permissões de acesso público e testar o endpoint do site. Ao final, o exercício proporcionou uma compreensão prática das capacidades do Amazon S3 para hospedar sites.

2. Lab AWS Athena

O exercício  ensina a configurar o Athena para realizar consultas em dados no S3. Aprendi a configurar o Athena para realizar consultas em dados armazenados no S3. Primeiro, verifiquei se o arquivo nomes.csv estava no meu bucket S3, e, caso não estivesse, criei um novo bucket, fiz o upload do arquivo e criei uma pasta para armazenar os resultados das consultas. Em seguida, criei um banco de dados no Athena e uma tabela externa, baseada em dados no S3, definindo os campos e tipos de dados. Após criar a tabela, testei as consultas usando SQL, incluindo uma query para listar os 3 nomes mais usados por década, de 1950 até o presente.

3. Lab AWS Lambda

No exercício "Lab AWS Lambda", criei uma função Lambda no console da AWS, selecionando o runtime Python 3.9 e escrevendo um código para acessar um arquivo CSV armazenado no S3, usando as bibliotecas Pandas e Boto3 para contar o número de linhas no arquivo. Ao testar a função, encontrei um erro devido à falta da biblioteca Pandas, o que me levou a criar uma "Layer" no Lambda. Para isso, utilizei o Docker para instalar o Pandas e suas dependências, criei um arquivo ZIP com as bibliotecas e o carreguei no S3. Em seguida, criei a camada no Lambda, vinculando-a à minha função. Após isso, testei a função novamente e obtive com sucesso a contagem das linhas do arquivo CSV, indicando que a configuração foi bem-sucedida.

[Exercícios](./Exercicios)

## Desafio

Na Etapa 1 do desafio, meu objetivo foi criar um Data Lake e realizar a ingestão de arquivos CSV (movies e series) em um bucket Amazon S3, na Raw Zone. Para isso, eu precisei construir um código Python, que seria executado dentro de um container Docker, utilizando a biblioteca Boto3 para carregar os dados dos arquivos locais para o S3 na nuvem.

[Desafio](./desafio)