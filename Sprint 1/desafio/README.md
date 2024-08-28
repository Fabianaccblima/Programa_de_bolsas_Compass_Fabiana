
# ETAPAS

## Passo 1

1. **Arquivo dados_de_vendas:**

   - Fiz download do arquivo *dados_de_vendas.sh* e, em seguida, criei um diretório **ecommerce** e inseri o arquivo *dados_de_vendas.sh* nele.
     'mkdir ecommerce'
      'cd ecommerce'
       'mv /home/fabiana/Downloads/dados_de_vendas.csv .'

## Passo 2

1. Criei um arquivo executável com o nome *processamento_de_vendas.sh*, usei o comando sudo chmod+x para tornar o arquivo executável e inseri os seguintes comandos:

    ```
    touch processamento_de_vendas.sh
    sudo chmod +x  
    nano processamento_de_vendas.sh
    ```
    [alt text](C:\Users\fabia\OneDrive\Área de Trabalho\Desafio 1\prints\01.png)

    - Um diretório **vendas** será criado e o arquivo *dados_de_vendas.sh* que está dentro do diretório **ecommerce** será copiado para dentro do diretório **vendas**.

    - Dentro do diretório **vendas**, crie um subdiretório chamado **backup** e faça uma cópia do arquivo *dados_de_vendas.csv* para dentro dele, mudando o **nome** do arquivo para a data do dia precedido por hífen: `dados-<yyyy.mm.dd>.csv`.

    - Ainda dentro do diretório **backup**, renomeie o arquivo anterior para *backup-dados<yyyy.mm.dd>.csv* e crie um arquivo chamado **relatorio.txt** para obter as seguintes informações:

      1. Data do sistema operacional em formato `YYYY/MM/DD HH:MM`.
      2. Data do primeiro registro de venda contida no arquivo.
      3. Data do último registro de venda contido no arquivo.
      4. Quantidade total de itens diferentes vendidos.
      5. Mostrar as 10 primeiras linhas do arquivo *backup-dados<yyyy.mm.dd>.csv* dentro do relatório.

    - Feito isso, compacte o arquivo *backup-dados<yyyy.mm.dd>.csv* para `.zip` e apague o arquivo *backup-dados<yyyy.mm.dd>.csv* do diretório **backup** e o arquivo *dados_de_vendas.csv* do diretório **vendas**.

## Passo 3

- Crie um crontab para executar o arquivo *processamento_de_vendas.sh* para **realizar 4 execuções de segunda a quinta às 15:27**.
  
  ### Nota:
  - Eu manipulei manualmente o relatório para que pudesse gerar relatórios com dados diferentes.

## Passo 4

- Depois que os 4 relatórios foram gerados, criei um novo script chamado *consolidador_de_vendas.sh* para unir os relatórios e gerar um **relatório final.txt**.
