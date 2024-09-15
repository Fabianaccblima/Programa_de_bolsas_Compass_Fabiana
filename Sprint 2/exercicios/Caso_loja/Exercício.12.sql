with cte_total_de_vendas
as 
(select cdvdd,  sum(qtd * vrunt) as total_de_vendas
    from tbvendas as venda
where status = 'Concluído'
group by cdvdd
having total_de_vendas >0 
)

SELECT dep.cddep, dep.nmdep, dep.dtnasc, min(cte_tab.total_de_vendas) as valor_total_vendas
      FROM tbdependente as dep
      INNER JOIN cte_total_de_vendas as cte_tab
       ON dep.cdvdd = cte_tab.cdvdd
ORDER BY cte_tab.total_de_vendas 
LIMIT 1;



-- Fiz uma tabela 'cte_total_de_vendas' utilizando o comando with;
-- A tabela 'cte_total_de_vendas' tem como objetivo obter o total de vendas com status concluídos por vendedor;
-- Posteriormente, foi feito um 'select' à tabela 'tbcte_total_de_vendas' com a tabela de dependentes com
-- o objetivo de obter os dados dos dependentes, e ao mesmo tempo obter o vendedor com menor valor de vendas.
-- Para a obtenção dos dados relativos ao vendedor com a menor venda, foi feito um "order by" 
-- pela coluna de total de vendas por vendedor em ordem crescente e, posteriormente, o comando "limit 1"


