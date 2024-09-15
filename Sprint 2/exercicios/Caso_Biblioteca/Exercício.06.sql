with cte_tab
as 
( select  aut.codautor,  count (*) as "quantidade"
    from livro  as liv
    inner join autor as aut
    on aut.codautor = liv.autor
group by liv.autor ) 

select cte_tab.codautor, aut.nome,  max (cte_tab.quantidade) as quantidade
from cte_tab
      inner join autor as aut
          on aut.codautor = cte_tab.codautor



with cte_tab as (
    select aut.codautor, aut.nome, count(*) as quantidade_publicacoes
    from livro as liv
    inner join autor as aut on aut.codautor = liv.autor
    group by aut.codautor, aut.nome
)
select codautor, nome, quantidade_publicacoes
from cte_tab
order by quantidade_publicacoes desc
limit 1;



-- Fiz uma tabela 'cte_tab' utilizando o comando with;
-- A tabela 'cte_tab' tem como objetivo obter a quantidade de publicações de livro de cada autor;
-- Posteriormente, foi feito um 'select' à tabela 'cte_tab' com o objetivo de obter o autor 
-- com o maior número de publicações;
-- Para obter o nome do autor foi feito o 'inner join' entre a tabela autor e à tabela 'cte_tab'
-- pelo código do autor;
-- O comando 'order by desc' foi utilizado para obter o autor com maior número de publicações primemiro;
-- E por fim, o 'limit 1' para me trazer somente 1 número do registro. 


