select *
  from livro
 where publicacao > '2014-12-31'
 order by cod ASC
;

-- Utilizei o comando "select *" para especificar todos os  
-- campos da tabela que eu gostaria de visualizar, depois utilizei o 
-- comando "from" para indicar o nome da tabela (livro) que eu gostaria 
-- de obter as informações, e por fim, utilizei o comando "where"
-- para selecionar os livros publicados após 2014 ordenados pelo código do livro.  

