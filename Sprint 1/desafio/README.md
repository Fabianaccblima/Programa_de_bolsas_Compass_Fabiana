
# ETAPAS

## Passo 1

1. **Arquivo dados_de_vendas:**

   - Fiz download do arquivo *dados_de_vendas.sh* e, em seguida, criei um diretório **ecommerce** e inseri o arquivo *dados_de_vendas.sh* nele.
        ```
       mkdir ecommerce
       cd ecommerce
       mv /home/fabiana/Downloads/dados_de_vendas.csv .
        ```

## Passo 2

1. Criei um arquivo executável com o nome *processamento_de_vendas.sh*, usei o comando sudo chmod+x para tornar o arquivo executável e o nano para inseri os seguintes comandos:

    ```
    touch processamento_de_vendas.sh
    sudo chmod +x  
    nano processamento_de_vendas.sh
    ```
   [Permissão Executável](Sprint%201/desafio/Permissao_executavel.png)



    - Um diretório **vendas** foi criado e o arquivo *dados_de_vendas.sh* que está dentro do diretório **ecommerce** foi copiado para dentro do diretório **vendas**.

    - Dentro do diretório **vendas**, criei um subdiretório chamado **backup** e fiz uma cópia do arquivo *dados_de_vendas.csv* para dentro dele, mudando o **nome** do arquivo para a data do dia precedido por hífen: `dados-<yyyy.mm.dd>.csv`.

    - Ainda dentro do diretório **backup**, renomeiei o arquivo anterior para *backup-dados<yyyy.mm.dd>.csv* e crie um arquivo chamado **relatorio.txt** para obter as seguintes informações:

      1. Data do sistema operacional em formato `YYYY/MM/DD HH:MM`.
      2. Data do primeiro registro de venda contida no arquivo.
      3. Data do último registro de venda contido no arquivo.
      4. Quantidade total de itens diferentes vendidos.
      5. Mostrar as 10 primeiras linhas do arquivo *backup-dados<yyyy.mm.dd>.csv* dentro do relatório.

    - Feito isso, compactei o arquivo *backup-dados<yyyy.mm.dd>.csv* para `.zip` e apaguei o arquivo *backup-dados<yyyy.mm.dd>.csv* do diretório **backup** e o arquivo *dados_de_vendas.csv* do diretório **vendas**.

[Editor_nano_1](Sprint%201/desafio/nano1.png)

[Editor_nano_2](Sprint%201/desafio/nano2.png)

[Data_Hora_Dados_Vendas](Sprint%201/desafio/Data_hora_dados_vendas.png)

[Primeira Data Dados de Vendas](Sprint%201/desafio/primeira_data_dados_de_vendas.png)

[Última Data Dados de Vendas](Sprint%201/desafio/ultima_data_dados_de_vendas.png)

[Quantidade_de_Itens_Vendidos](Sprint%201/desafio/Qnt_itens_vendidos.png)


## Passo 3

- Criei um crontab para executar o arquivo *processamento_de_vendas.sh* para **realizar 4 execuções de segunda a quinta às 15:27**.

```
crontab -e
```

[Crontab](Sprint%201/desafio/crontab.png)

  
  ### Nota:
  - Eu manipulei manualmente o relatório para que pudesse gerar os 4 relatórios com dados diferentes.


## Relatórios:

[Relatório_2608](Sprint%201/desafio/relatorio_2608.png)

[Relatório_2708](Sprint%201/desafio/relatorio_2708.png)

[Relatório_2808](Sprint%201/desafio/relatorio-2808.png)

[Relatório_2908](Sprint%201/desafio/relatorio_2908.png)

[4_Execuções](Sprint%201/desafio/4%20execuções.png)


## Passo 5

- Depois que os 4 relatórios foram gerados, criei um novo script executável chamado *consolidador_de_vendas.sh* para unir os relatórios e gerar um **relatório final.txt**.

    ``` 
    touch consolidador_de_vendas.sh
    sudo chmod +x
    nano consolidador_de_vendas.sh
    ```
[Consolidador_de_Vendas](Sprint%201/desafio/Consolidador_de_vendas.png)

[Relatório_Final_1](Sprint%201/desafio/relatorio_final_1.png)

[Relatório_Final_2](Sprint%201/desafio/relatorio_final_28_29.png)


