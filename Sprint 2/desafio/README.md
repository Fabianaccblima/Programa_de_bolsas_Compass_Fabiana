## Primeiro passo:
1 - Baixei a tabela concessionária e obtive a tabela locação não normalizada. 

2 - Para a normalização da tabela, utilizei os princípios das 3 normas de normalização (1FN, 2FN e 3FN).

3 - Em consequência da normalização, foram identicadas as seguintes tabelas : "Tb_locacao", "Tb_combustível", "Tb_carro", "Tb_cliente" e "Tb_vendedor" no modelo relacional.

## Segundo passo:
1- Criação do modelo lógico relacional normalizado através do site dbdiagram.

## Terceiro passo:
1 - Criação dimensional a partir do relacional.

2 - No modelo dimensional foi utilizado o esquema estrela, pois permite uma certa não normalização dos dados para uma 
obteção mais simples e rápida da informação.

3- As tabelas de dimensão e fato do modelo dimensional foram criadas a partir de "VIEWS" das tabelas do modelo relacional.

4- Tabelas resultantes do modelo dimensional: 

4.1 "dim_carro" criada a partir da "tb_carro".

4.1.1 A tabela "dim_carro" está não normalizada com a criação da coluna "tipo de combustível".

4.1.2 Em função da não normalização da tabela "dim_carro" não foi necessário a criação da tabela "dim_combustível".

4.2 "dim_vendedor" criada a partir da "tb_vendedor".

4.3 "dim_cliente" criada a partir da "tb_cliente".

4.4 "dim_tempo" criada a partir da data de locação da "tb_locação".

4.5 "fato_locacao" criada a partir da "tb_locação".

4.5.1 Nesta tabela fato ficou decidido que a data da locação da "tb_locação" não faria parte da mesma.

4.5.2 O motivo pelo qual ficou decidido o ítem 4.5.1 é que a data da locação ocasionaria uma granularidade quase igual 
ou mesmo igual a tabela "tb_locação", pois não é habitual que um cliente alugue, em um mesmo dia, mais do que um carro.

4.5.3 Portanto, em substituição da data de locação foram criados os campos "ano, mês e dia da semana" na tabela de fato
locação.

4.5.4 Ficou decidido também que na tabela "fato_locação" o código do cliente não fará parte da mesma pelo mesmo motivo de
uma tabela resultante com muita granularidade.

4.5.5 Para representação analítica dos dados relacionados de locações por cliente foi criada uma tabela "fato_locação_cli". 

5 "fato_locação_cli" criada com o propósito de armanezar as locações dos clientes por "ano, mês e dia da semana".   

## Quarto passo:
1- Criação do modelo dimensional através do site dbdiagram. 