show databases;
create database nit;
show databases;
use nit;
create table student (
name varchar (30),
id int not null primary key, 
address varchar (50), 
marks int);
select * from student;
insert into student(marks, id, name, address)values(78, 12, 'prakash', 'hyd');
select * from student;

insert into student values('kodi', 40, 'bng', 66);

insert into student values 
('alex', 45, 'hyd', 79),
('cathy',17, 'delhi', 90),
('dolly' ,48, 'pune' , 67), 
('chancy' , 78, 'mumbai', 34);
select * from student;
select name,id from student;
insert into student values('sam', 12, 'hyd', 56);
select * from student;