
select edi.codEditora, edi.nome, count (*) as quantidade_livros 
   from livro as liv 
      INNER JOIN editora as edi
         on liv.editora = edi.codeditora
group by edi.codeditora, edi.nome
order by quantidade_livros DESC
limit 5 



