insert into tb_locacao
select idlocacao 
     , idcliente
     , idcarro
     , kmcarro
     , idvendedor
     , datalocacao
     , vlrdiaria
     , qtddiaria
     , horalocacao
     , dataentrega
     , horaentrega
  from tb_locacao_old 
  ;



