
SELECT 
    autor.codAutor, 
    autor.nome, 
    autor.nascimento, 
    COUNT(livro.cod) AS quantidade
FROM 
    autor
LEFT JOIN 
    livro ON autor.codAutor = livro.autor
GROUP BY 
    autor.codAutor, autor.nome, autor.nascimento
ORDER BY 
    autor.nome ASC;

-- Utilizei o comando "select" conjuntamente com o comando "group by" para agrupar o 
-- total de livros por autor, mostrando também o nome e data de nascimento do autor.
-- A seleção do nome e data de nascimento do autor conjuntamente com o "group by" não tem impacto no
-- somatório da quantidade de livros publicados porque estes atributos pertecem a entidade autor. 
-- Fiz a junção das tabelas autor com livro utilizando o comando "letf join", pois é a forma existente para 
-- poder mostrar autores sem livros publicados.
-- Atribui um "alias" quantidade ao "count (*)" para representar a quantidade de livros publicados por cada autor; 
-- Para obter as linhas em ordem crescente de nomes de autor, utilizei o comando "order by ". 