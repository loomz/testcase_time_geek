#创建用户 user_开头，库名结尾，比如user_db_ddt
CREATE USER  'user_db_ddt_test'@'%' IDENTIFIED BY 'user_db_ddt_test';

#创建数据库 db_开头，业务名或者系统名结尾，如db_ddt_test
CREATE database db_ddt_test default character set utf8 collate utf8_general_ci;

#给用户授权
GRANT all privileges ON db_ddt_test.* TO 'user_db_ddt_test'@'%' identified  by 'user_db_ddt_test';

# 创建表，表名以t_开头t_模块名_功能，表名前面要带上库名，如db_ddt_test.t_user_ddt_test
CREATE TABLE IF NOT EXISTS db_ddt_test.`t_user_ddt_test`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `username` VARCHAR(20) NOT NULL COMMENT '用户名',
   `pwd` VARCHAR(20) NOT NULL COMMENT '密码',
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='ddt测试用户表';

# 数据
insert into db_ddt_test.t_user_ddt_test (username, pwd) values('cat', '345');
insert into db_ddt_test.t_user_ddt_test (username, pwd) values('wangmin', '123');
insert into db_ddt_test.t_user_ddt_test (username, pwd) values('tina', '999');


