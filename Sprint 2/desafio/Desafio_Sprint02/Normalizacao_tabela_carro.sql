insert INTO tb_carro
select DISTINCT
       idCarro
     , marcaCarro
     , modeloCarro
     , anoCarro
     , idcombustivel
     , classiCarro
  from tb_locacao_old
; 