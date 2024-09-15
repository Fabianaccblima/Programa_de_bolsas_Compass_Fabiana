INSERT INTO tb_cliente
select DISTINCT
       idCliente
     , nomeCliente
     , cidadeCliente
     , estadoCliente
     , paisCliente
  from tb_locacao_old
;
  