此系统面向家政行业，为其提供如下主要服务：
1、从业人员管理
2、顾客关系维护和沟通
3、通过手机端推广本公司

数据库：
create database weixin character set utf8;

create table tablename(id int(20) not null primary key auto_increment,status int(2),myrole int(2),joiner text) default charset=utf8;

数据库表：
+------------------------+
| Tables_in_jiazhengfuwu |
+------------------------+
| admin_user             |
| company_admin_user     |
+------------------------+
2 rows in set (0.00 sec)

数据库表结构：

desc admin_user; #系统总管理员，管理系统内的其它用户
+----------+--------+------+-----+---------+----------------+
| Field    | Type   | Null | Key | Default | Extra          |
+----------+--------+------+-----+---------+----------------+
| id       | int(2) | NO   | PRI | NULL    | auto_increment |
| username | text   | YES  |     | NULL    |                |
| password | text   | YES  |     | NULL    |                |
| cookies  | text   | YES  |     | NULL    |                |
| hands    | text   | YES  |     | NULL    |                |
+----------+--------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

desc company_admin_user; #公司用户，每个公司一个用户，该用户操作公司的管理界面
+--------------------+--------+------+-----+---------+----------------+
| Field              | Type   | Null | Key | Default | Extra          |
+--------------------+--------+------+-----+---------+----------------+
| id                 | int(2) | NO   | PRI | NULL    | auto_increment |
| username           | text   | YES  |     | NULL    |                |
| companyname        | text   | YES  |     | NULL    |                |
| telphone           | text   | YES  |     | NULL    |                |
| mobilephone        | text   | YES  |     | NULL    |                |
| companyaddress     | text   | YES  |     | NULL    |                |
| startdatetime      | int(2) | YES  |     | NULL    |                |
| enddatetime        | int(2) | YES  |     | NULL    |                |
| logindatetime      | int(2) | YES  |     | NULL    |                |
| password           | text   | YES  |     | NULL    |                |
| cookies            | text   | YES  |     | NULL    |                |
| hands              | text   | YES  |     | NULL    |                |
| logoutdatetime     | int(2) | YES  |     | NULL    |                |
| createuserdatetime | int(2) | YES  |     | NULL    |                |
+--------------------+--------+------+-----+---------+----------------+
14 rows in set (0.00 sec)

