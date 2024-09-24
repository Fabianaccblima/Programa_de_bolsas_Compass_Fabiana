### Primeiro passo: 

1 - Importei as biblioteca Pandas e Matplotlib.

2- Baixei o arquivo "googleplaystore.csv" e o chamei de df_google.

3 - Utilizei um comando  `pd.set_option('display.max_rows', 20)` para exibir no máximo 20 linhas do dataframe. 

4- Em seguida, utilizei o comando `drop_duplicates()` para remover as linhas duplicadas no dataframe.

### Segundo passo: 

#### Para obter os 5 maiores aplicativos por números de instalação, foi necessário fazer um tratamento dos dados.

1 - Convertir a coluna "Intalls" para string. Feito isso, utilizei comandos para remover o nome "Free" e símbolo "+"

2- Substituir strings vazias por NaN.

3- Convertir a coluna 'Installs' resultante  para float e ordenei os aplicativos pela coluna 'Installs' em ordem decrescente.

4- Por fim, utilizei o comando `print` para obter o resultado.

#### Contar quantos aplicativos existem em cada categoria 

1 - Utilizei o comando `category_count = df_google['Category'].value_counts()` para obter a contagem das categorias. 

2 - Por fim, utilizei o comando `print` para obter o resultado

### Obter o aplicativo mais caro 

1 - Convertir a coluna 'Price' para string.

2 - Removir o símbolo $ e substitui 'Everyone' por '0'.

3 - Convertir  a coluna resultante de volta para float para garantir que os valores sejam numéricos.

4- Ordenei o DataFrame pela coluna 'Price' em ordem decrescente para pegar o aplicativo mais caro e utilizei o comando 
`head` para obter a primeira linha.

5 - Por fim, utilizei o comando `print` para obter o resultado

### Obter quantos aplicativos são classificados como Mature 17+ 

1 - Filtrei  os aplicativos com classificação "Mature 17+".

2 - Removir as duplicatas com base na coluna 'App', garantindo que cada aplicativo seja contado apenas uma vez.

3 -Contei o número de aplicativos únicos com classificação "Mature 17+".

4 - Por fim, utilizei o comando `print` para obter o resultado.

####  Exibir o nome dos "Aplicativos" e o número de "Reviews"

1 - Convertir 'Reviews' para numérico.

2 - Removir duplicatas com base no nome do aplicativo (coluna 'App').

3 - Ordenei o DataFrame pelo número de reviews em ordem decrescente.

4- Por fim, utilizei o comando `print` para obter o resultado.

#### Obter os 10 mais gêneros frequentes

1 - Utilizei o comando `value_counts()` na coluna 'Genres' do DataFrame "df_google" para contar a quantidade de ocorrências de cada gênero.

2 - Utilizei o comando `head(10)` para retornar os 10 gêneros mais frequentes.

3 - Por fim, utilizei o comando `print` para obter o resultado.

#### Obter os tipos de contagem 

1 - Utilizei o comando `value_counts()` na coluna 'Type' do DataFrame df_google para contar quantas vezes cada valor aparece.

2 - A coluna 'Type' indica se o aplicado é gratuito ("Free") ou pago ("Paid").

3 - Por fim, utilizei o comando `print` para obter o resultado.

### Terceiro passo:

1 - Utilizei o Matplotlib para gerar os gráficos solicitados.