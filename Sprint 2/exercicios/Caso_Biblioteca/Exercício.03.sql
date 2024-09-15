select count (*) as "quantidade", edi.nome, end.estado, end.cidade 
  from livro  as liv
       inner JOIN editora as edi
               on liv.editora = edi.codeditora 
       inner join endereco as end 
               on end.codendereco = edi.endereco
 group by liv.editora
 order by quantidade desc 
 limit 5;


-- Utilizei o comando "select" para selecionar as colunas indicadas no exercício;
-- Para obter as editoras com mais livros na biblioteca, fiz um "count (*)" relacionado ao 
--"group by" pelo código da editora da tabela de livro;
-- Atribui um "alias" quantidade ao "count (*)" para representar a quantidade editoras com livros na biblioteca; 
-- Para obter os dados da tabela "Editora", fiz um "inner join" da tabela de livro com a tabela editora
-- ligados pelo código da editora;
-- Para obter os dados da tabela "Endereço", fiz um "inner join" da tabela editora com a tabela endereço 
-- ligados pelo código do endereço;
-- Para obter as linhas em ordem decrescente de quantidade de editoras com livro na biblioteca, utilizei
-- o comando "order by desc";
-- Utilizei o comando "limit 5" para selecionar somente as 5 editoras com mais livros na biblioteca,
-- entretanto, identifiquei que há somente 2 editoras com livros na biblioteca.