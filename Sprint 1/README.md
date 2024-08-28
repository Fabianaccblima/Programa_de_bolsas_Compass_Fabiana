
#### INTRUÇÕES

1 - Conforme solicitado, foi baixado o arquivo *dados_de_vendas.sh* e criado um **diretório** chamado *ecommerce* e inserido o arquivo dados_de_vendas.sh nele.
    
    
     1 - mkdir ecommerce
     2 - cd ecommerce
     3 - mv /home/fabiana/Downloads/dados_de_vendas .
     

    

1- Também foi criado um *arquivo executável* chamado *processamento_de_vendas.sh* onde o mesmo cria os **diretórios** venda e backup. Além disso, gera relatórios a partir do arquivo *dados_de_vendas.cvs* e faz a compactuação do backup em .zip a cada execução do script.
 
 `touch processamento_de_vendas.sh`

 `sudo chmod +x`

 `nano processamento_de_vendas.sh`

 ##### Os comandos do **processamento_de_vendas.sh** estão no Readme.Desafio


1-A execução do script * processamento_de_vendas.sh* foi realizada através dos 4 agendamentos **segunda a quinta as 15:27**

1-Após as 4 execuções, foi solicitado para criar um **novo script** chamado de *consolidador_de_processamentos_de_vendas.sh* para gerar um relatório final juntando todos os relatório em um só. 
    
### Evidências
 
1- Criação do arquivo executável *processamento_de_vendas.sh* com permissão para torná-lo executável.


[Permissão Executável](Sprint%201/Permissao_executavel.png)


1- Criação do *crontab* para executar os 4 agendamentos do arquivo *processamento_de_vendas.sh*

[Crontab](Sprint%201/crontab%20.png)


1-Criação do **novo script** *consololidador_de_processamentos_de_vendas.sh* para juntar os relatórios em um só. 

`touch consolidador_de_processamento_de_vendas.sh`

`sudo chmod +x consolidador_de_processamento_de_vendas` 

`nano consolidador_de_processamento_de_vendas`

[Consolidador_de_Vendas](Sprint%201/Consolidador_de_vendas.png)

