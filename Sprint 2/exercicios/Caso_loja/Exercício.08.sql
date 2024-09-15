with cte_tab

as

(select vendedor.nmvdd  ,vendedor.cdvdd, count (*) as quantidade
    from tbvendas as vendas
    inner join tbvendedor as vendedor
    on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído'
group by vendedor.cdvdd
)

select cte_tab.cdvdd, cte_tab.nmvdd
    from cte_tab
    order by quantidade DESC
    limit 1

-- Fiz uma tabela "CTE_TAB" com as quantidades vendidas por vendedor.
-- Posteriormente, fiz um select ordenando a quantidade vendida em ordem descendente, selecionando o código e nome do 
-- vendedor. Para a obtenção do vendedor com a maior quantidade de vendas, adicionei a cláusula "limit 1".




