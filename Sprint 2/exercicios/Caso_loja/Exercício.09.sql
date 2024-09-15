with cte_tab
AS
(
select cdpro, nmpro, sum(qtd) as total_vendido
   from tbvendas 
where dtven BETWEEN '2014-02-03' and '2018-02-02'
     AND status = 'Concluído'
group by cdpro ) 

select cte_tab.cdpro, cte_tab.nmpro
   from cte_tab
group by cdpro
order by cte_tab.total_vendido DESC
limit 1 

-- Fiz uma tabela "CTE_TAB" com o somatório das quantidades vendidas por vendedor, cujo estado da venda igual a concluído.
-- Posteriormente, fiz um select ordenando o total de vendas em ordem decrescente, selecionando o código e nome do 
-- produto. Para a obtenção do produto mais vendidos, adicionei a cláusula "limit 1".
