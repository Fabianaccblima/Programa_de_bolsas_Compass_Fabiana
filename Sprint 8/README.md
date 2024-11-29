## OBJETIVOS DA SPRINT

#### Nesta Sprint, os principais objetivos foram:

## Exercícios

1 - Geração e massa de dados

O objetivo desse exercício foi praticar manipulação de listas, ordenação, e escrita de arquivos. Gerei números aleatórios, inverti e exibi a lista, ordenei uma lista de animais e salvei em CSV, e criei 10 milhões de nomes aleatórios baseados em 3.000 nomes únicos, armazenando-os em um arquivo de texto.

2 - Apache Spark

O objetivo desse exercício foi usar PySpark para processar um grande conjunto de dados, adicionando colunas simuladas como nível educacional, país de origem e ano de nascimento. Realizei filtros, consultas SQL e contagens por geração e país, consolidando os resultados em um DataFrame final, demonstrando manipulação eficiente de dados em grande escala.

3 - TMDB

Criei uma conta no TMDb e obtive minha chave de API para acessar os dados relacionados aos filmes de comédia romântica para a análise que estou realizando.

[Exercícios](./Exercicios)

## Desafio

O objetivo do desafio foi utilizar o Apache Spark, integrado ao serviço AWS Glue, para processar dados existentes na camada Raw Zone e movê-los para a Trusted Zone no Amazon S3. O processo visou padronizar os dados, armazená-los em formato Parquet na Trusted Zone e registrá-los no AWS Glue Data Catalog. Dessa forma, os dados tornaram-se acessíveis via AWS Athena para análise com comandos SQL, garantindo consistência no armazenamento e facilidade de consulta no Data Lake.

[Desafio](./desafio)


## Análise 

Análise dos filmes de comédia romântica (1984-2022) investiga a relação entre nota média, popularidade e duração, além de tendências na produção e recepção crítica por década. Foca em como a duração influencia o desempenho, se filmes populares têm melhores notas, e padrões de sucesso do gênero ao longo do tempo.