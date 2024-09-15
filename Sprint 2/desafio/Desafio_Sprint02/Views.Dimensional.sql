
create VIEW dim_cliente as
    SELECT idCliente
         , nomeCliente
         , cidadeCliente
         , estadoCliente
         , paisCliente
      from tb_cliente
;



create VIEW dim_carro as
   SELECT car.idCarro 
        , car.marcaCarro
        , car.modeloCarro
        , car.anoCarro
        , com.tipoCombustivel
        , car.classiCarro
   from   tb_carro          as car
  inner join tb_combustivel as com
      on car.idCarro = com.idcombustivel
;


create VIEW dim_vendedor as
   SELECT  idVendedor
        ,  nomeVendedor
        , sexoVendedor
        , estadoVendedor
    from tb_vendedor
;


create VIEW dim_tempo as 
 SELECT distinct 
       dataLocacao
     , strftime('%Y', substr(dataLocacao, 1, 4)  || '-' ||
                     substr(dataLocacao,  5, 2)  || '-' ||
                     substr(dataLocacao,  7, 2))            AS ano
 
     , strftime('%m', substr(dataLocacao, 1, 4)  || '-' ||
                     substr(dataLocacao,  5, 2)  || '-' ||
                     substr(dataLocacao,  7, 2))            AS mes
 
     , strftime('%d', substr(dataLocacao, 1, 4)  || '-' ||
                     substr(dataLocacao,  5, 2)  || '-' ||
                     substr(dataLocacao,  7, 2))            AS dia
 
     , strftime('%W', substr(dataLocacao, 1, 4)  || '-' ||
                     substr(dataLocacao,  5, 2)  || '-' ||
                     substr(dataLocacao,  7, 2))            AS dia_da_semana
FROM tb_locacao; 
 



CREATE view fato_locadora as 
Select tem.ano
     , tem.mes
     , tem.dia_da_semana
     , idVendedor
     , idCarro
     , sum(vlrDiaria) as total_vlrdiaria
     , sum(qtdDiaria) as total_qtddiaria
     , count (*)      as total_qtdlocacao
     from tb_locacao as loc
       inner join dim_tempo as tem
        on loc.dataLocacao = tem.dataLocacao
 group by  tem.ano
        ,  tem.mes
        ,  tem.dia_da_semana
        ,  idVendedor
        ,  idCarro
;


CREATE view fato_locadora_cli as 
Select tem.ano
     , tem.mes
     , idCliente
     , sum(vlrDiaria) as total_vlrdiaria
     , sum(qtdDiaria) as total_qtddiaria
     , count (*)      as total_qtdlocacao
     from tb_locacao as loc
       inner join dim_tempo as tem
        on loc.dataLocacao = tem.dataLocacao
 group by  tem.ano
        ,  tem.mes
        ,  idCliente
;




