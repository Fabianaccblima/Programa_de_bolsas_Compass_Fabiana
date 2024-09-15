select estado, nmpro, round(avg(qtd),4) as quantidade_media
from tbvendas
WHERE status = 'Concluído'
group by estado, nmpro
order by estado, nmpro

-- Utilizei o comando "select " para especificar os campos da tabela que eu gostaria de visualizar;
-- Utilizei o comando 'round(avg), 4' para obter a quantidade média na quarta casa decimal e dei o nome de
--'quantidade_media';
-- A tabela selecionada foi a tbvendas através do comando 'from'
-- Para selecionar apenas os status conclúidos, usei o comando 'where';
-- E por fim, fiz um 'group by' e 'order by' por Estado e Nome, para obter a médida vendida de cada
-- produto por Estado.