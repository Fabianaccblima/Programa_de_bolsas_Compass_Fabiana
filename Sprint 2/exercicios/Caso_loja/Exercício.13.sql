select cdpro, nmcanalvendas, nmpro, sum(qtd) as quantidade_vendas
 from tbvendas 
where status = 'Concluído'
and (nmcanalvendas = 'Matriz' or nmcanalvendas = 'Ecommerce')
group by cdpro, nmcanalvendas, nmpro
order by quantidade_vendas ASC
limit 10

-- Utilizei o comando "select " para especificar os campos da tabela que eu gostaria de visualizar;
-- Utilizei a função 'sum(qtd)' para obter a quatidade_vendas;
-- A tabela selecionada foi a tbvendas através do comando 'from';
-- Para selecionar apenas os status conclúidos e o canal de vendas = Matriz ou Ecommerce
-- usei o comando 'where';
-- Agrupei pelo cdpro, nmcanalvendas e nmpro;
-- Fiz um 'order by' para obter a quantidade_vendas em ordem crescente;
-- Utilizei um 'limit 10' para listra os 10 produtos menos vendidos. 