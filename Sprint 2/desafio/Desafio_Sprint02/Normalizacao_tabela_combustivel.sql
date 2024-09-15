insert into tb_combustivel
select DISTINCT
       idcombustivel
     , tipoCombustivel
  from tb_locacao_old
;     