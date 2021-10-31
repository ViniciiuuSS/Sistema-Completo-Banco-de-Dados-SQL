create database Loja
default character set utf8
default collate utf8_general_ci;

create table produtos (
idProd int not null auto_increment,
nome varchar(70) not null,
preco float not null,
primary key(idProd)
);

drop table produtos;

insert into produtos values
(default,'Teclado','80'),
(default,'Mouse','300'),
(default,'Monitor','800');

select * from produtos;