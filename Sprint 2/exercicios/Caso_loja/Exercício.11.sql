select cdcli, nmcli, 
sum(qtd * vrunt) as gasto
from tbvendas
where status = 'Concluído'
group by nmcli
order by gasto DESC
limit 1

-- Foi feito um  "group by" por código do cliente e nome do cliente para obtenção dos gastos dos clientes.
-- O cálculo do gasto do cliente é obtido através do somatório entre a quantidade comprada e o valor unitário do produto.
-- Para que o resultado apresente na primeira linha o cliente com maior gasto na loja,foi feito um
-- order by da coluna que representa o valor gasto em ordem descendente.