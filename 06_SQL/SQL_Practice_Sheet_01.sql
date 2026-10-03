use nit;
create table customers(
id int primary key,
name varchar(100),
age int,
address varchar(255),
salary int);


desc customers;

insert into customers(id,name,age,address,salary)values("1","Ramesh","32","Ahmedabad","2000.00");
insert into customers value("2","Khilan","25","Delhi","1500.00");
insert into customers value("3","Kaushik","23","Kota","2000.00");
insert into customers value("4","Chaitali","25","Mumbai","6500.00");
insert into customers value("5","Hardik","27","Bhopal","8500.00");
insert into customers value("6","Komal","22","Mp","4500.00");
insert into customers value("7","Muffy","24","Indore","10000.00");

select * from customers;

select * from customers where salary > 5000;

select * from customers where salary = 2000;

select * from customers where salary != 2000;

select * from customers where salary <> 2000;

select * from customers where salary >= 6500;

select * from customers;

select * from customers where age >=25 AND salary >=6500;

select * from customers where age >= 25 OR salary >= 6500;

select  * from customers where age is not null;

select * from customers where name like 'Ko%'

select * from customers where age in (25,27);

select * from customers where age between 25 AND 27;

select age from customers
where exists (select age from customers where salary > 6500);

select * from customers
where age > all (select age from customers where salary > 6500);

select * from customers
where age > any (select age from customers where salary > 6500);

select * from customers;

select * from customers where salary=10000;

select (15+6) as addition

select count(*) as "records" from customers;

select current_timestamp;

select getdate();

create database testdb;

show databases;

drop database testdb;

show databases;

use nit;

create table salary as(
select id, salary
 from customers);
 
 create table customers(
  id int             not null,
  name varchar(20)   not null,
  age int            not null,
  address char (25),
  salary decimal (18,2),
  primary key (id)
  );
 
 desc customers;
 
 drop table customers;
 
 desc customers;
 
 create table customers(
id int primary key,
name varchar(100),
age int,
address varchar(255),
salary int);
 
INSERT INTO customers VALUES (value1,value2,value3,value4,value5,value6,value7); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (1, 'Ramesh', 32, 'Ahmedabad', 2000.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (2, 'Khilan', 25, 'Delhi', 1500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (3, 'kaushik', 23, 'Kota', 2000.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (4, 'Chaitali', 25, 'Mumbai', 6500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (5, 'Hardik', 27, 'Bhopal', 8500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (6, 'Komal', 22, 'MP', 4500.00 );
INSERT INTO CUSTOMERS  
VALUES (7, 'Muffy', 24, 'Indore', 10000.00 );

desc customers;

select * from customers;

select id,name,salary from customers;

select * from customers;

select id,name,salary
from customers
where salary > 2000;

select id,name,salary

select id, name, salary
from customers
where name='Hardik';

select * from customers;

select id, name, salary
from customers
where salary > 2000 AND age < 25;

select * from customers;

select id , name ,salary
from customers
where salary > 2000 OR age < 25;

select * from customers;

update customers
set address='Pune'
where id=6;
 
 select * from customers;
 
 update customers
 set address='Pune',salary=1000.00;
 
 select * from customers; 
 
 delete from customers
 where id=6;

select * from customers;
 
 