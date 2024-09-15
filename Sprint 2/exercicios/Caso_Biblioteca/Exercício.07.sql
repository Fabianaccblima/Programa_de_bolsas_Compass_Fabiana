
with cte_tab
as 
(select  aut.nome, liv.cod
    from autor  as aut
    LEFT join livro  as liv
    on aut.codautor = liv.autor)

select cte_tab.nome
   from cte_tab
where cte_tab.cod is null 

--Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
-- Para obtenção dos autores sem publicação, fiz uma tabela "CTE_TAB" com o left join" entre as tabelas autor e livro. 
-- A coluna liv.cod com valores a nulo da tabela "CTE_TAB" representa os autores sem publicação.
-- Em cima da tabela "CTE_TAB" foi feito um select, cujo código do livro igual a nulo, seleciona 
-- apenas os autores sem publicação.
