
select liv.cod, liv.titulo, aut.codautor, aut.nome, liv.valor, 
edi.codeditora, edi.nome
  from livro as liv
  INNER JOIN autor as aut
    on liv.autor= aut.codautor
  inner join editora edi
    on liv.editora = edi.codeditora
    order by liv.valor desc 
  limit 10

