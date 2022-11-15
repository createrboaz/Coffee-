create database employee;
use employee;
create table dept(deptcode varchar(10),deptname varchar(50));
insert into dept values('d001','finance');
insert into dept values('d002','agriculture');
insert into dept values('d003','education');
insert into dept values('d004','health');
insert into dept values('d005','salary');
select * from dept;
select * from emptab2;
create table emptab2 (empid int, salary varchar(50),empname varchar(50), city varchar(20));
insert into emptab2 values(1001,100000, 'manya', 'delhi');
insert into emptab2 values(1002,10790, 'sanya', 'mumbai');
insert into emptab2 values(1003,10790, 'tanya', 'mumbai');
insert into emptab2 values(1004,10790, 'sanya', 'mumbai');
insert into emptab2 values(1005,10790, 'sanya', 'mumbai');
alter table emptab2 add deptcode varchar(10);
select empid,empname, salary  from dbo.emptab2 , dbo.dept where emptab2.deptcode=dept.deptcode;
update emptab2 set deptcode ='d001' where empid =1001;
update emptab2 set deptcode ='d001' where empid =1002;
update emptab2 set deptcode ='d001' where empid =1003;
update emptab2 set deptcode ='d001' where empid =1004;
update emptab2 set deptcode ='d001' where empid =1005;
ko

