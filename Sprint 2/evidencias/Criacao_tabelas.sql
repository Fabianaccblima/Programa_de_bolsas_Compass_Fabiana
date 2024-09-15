-- SQLite

create table tb_cliente (
  idCliente int primary key,
  nomeCliente varchar (100),
  cidadeCliente varchar (40),
  estadoCliente varchar(40),
  paisCliente varchar (40)

);

create table tb_vendedor (
   idVendedor int primary key,
   nomeVendedor varchar (15),
   sexoVendedor smallint,
   estadoVendedor varchar (40)

);

create table tb_combustivel (
  idcombustivel int primary key,
  tipoCombustivel varchar (20)

);


create table tb_carro(
  idCarro  int  primary key,
  marcaCarro varchar (50),
  modeloCarro varchar(50),
  anoCarro int,
  idcombustivel int,
  classiCarro varchar (50),
  CONSTRAINT fk_comb FOREIGN KEY(idcombustivel) REFERENCES tb_combustivel(idcombustivel)
);


create Table tb_locacao (
  idLocacao int primary key,
  idCliente int,
  idCarro  int,
  kmCarro  int,
  idVendedor int, 
  dataLocacao datetime,
  vlrDiaria decimal(18,2),
  qtdDiaria int,
  horaLocacao time,
  dataEntrega time,
  horaEntrega time,


  CONSTRAINT fk_cli FOREIGN KEY(idCliente) REFERENCES tb_cliente(idCliente),
  CONSTRAINT fk_car FOREIGN KEY(idCarro) REFERENCES tb_carro(idCarro),
  CONSTRAINT fk_vend FOREIGN KEY(idVendedor) REFERENCES tb_vendedor(idVendedor)
);

 