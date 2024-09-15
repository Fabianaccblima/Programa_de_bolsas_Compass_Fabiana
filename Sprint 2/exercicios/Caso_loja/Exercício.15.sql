select cdven
from tbvendas
where deletado = '1'
order by cdven 

-- Utilizei o comando select para selecionar o campo da tabela;
-- Selecionei a tabela através do comando 'from' tbvendas;
-- Para filtrar os códigos das vendas identificadas como deletadas, usei o comando 'where', onde as linhas deletadas 
-- são representadas pelo número '1'.
-- Para apresentar o resultado em ordem crescente, utilizei o comando 'order by'.