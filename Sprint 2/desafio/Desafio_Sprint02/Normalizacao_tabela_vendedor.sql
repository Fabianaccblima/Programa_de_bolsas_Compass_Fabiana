insert into tb_vendedor
select DISTINCT
       idVendedor
     , nomeVendedor
     , sexoVendedor
     , estadoVendedor
  from tb_locacao_old
;  