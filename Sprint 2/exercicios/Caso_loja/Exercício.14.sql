select estado, round(avg(qtd * vrunt), 2) as gastomedio
from tbvendas
where status = 'Concluído'
group by estado
order by gastomedio DESC

-- Utilizei o comando 'round(avg(qnt* vrut),2)' para obter o gasto médio com duas casas decimais;
-- A tabela selecionada foi a 'tbvendas';
-- Para selecionar apenas os status conclúidos, usei o comando 'where';
-- Para obter a média de gasto por Estado, fiz um agrupamento por Estado;
-- E para ordernar o gasto médio em ordem decrescente, usei o comando 'ordey by desc'.