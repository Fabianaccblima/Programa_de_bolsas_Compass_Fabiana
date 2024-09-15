select DISTINCT aut.nome
  from livro  as liv
       inner JOIN autor as aut
               on liv.autor = aut.codautor 
       inner JOIN editora as edi
               on liv.editora = edi.codeditora 
       inner join endereco as end 
               on end.codendereco = edi.endereco
where end.estado <> 'PARANÁ' 
  AND end.estado <> 'RIO GRANDE DO SUL'
order by aut.nome 

-- Utilizei o comando "select" com "distinct" para apresentar os nomes sem a duplicação dos mesmos.
-- Para obter os dados da tabela "Autor", fiz um "inner join" da tabela de livro com a tabela autor
-- ligados pelo código do autor;
-- Para obter os dados da tabela "Editora", fiz um "inner join" da tabela de livro com a tabela editora
-- ligados pelo código da editora;
-- Para obter os dados da tabela "Endereço", fiz um "inner join" da tabela editora com a tabela endereço
-- ligados pelo código do endereço;
-- Para selecionar somente as editoras do Sul do país, selecionei a coluna Estado da tabela de endereço
-- diferente de 'Paraná' e 'Santa Catarina' e 'Rio Grande do Sul';
-- Foi utilizado "order by" para ordenar o resultado pela coluna nome do autor;
