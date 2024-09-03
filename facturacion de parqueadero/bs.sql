create schema francisco;


use fran;

create table usuari
(
    idCliente       int         not null primary key auto_increment,
    CORREO    varchar(50) not null,
    CONTRASEÑA varchar(50) not null,
     NOMBRES varchar(50) not null,
      APELLIDOS varchar(50) not null,
       TIPODOCUMENTO varchar(50) not null,
    NUMERODEDOCUMENTO   int         not null
    TELEFONO  int         not null
     PAIS varchar(50) not null,
     DIRECCION varchar(50) not null,

    
);
create table factura
(
    idFactura int not null primary key auto_increment,
    idCliente int not null
);



alter table factura
    add constraint fk_idClienteFactura foreign key (idCliente) references cliente (idCliente);