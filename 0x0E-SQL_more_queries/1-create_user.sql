-- creates the MySQL server user user_0d_1
-- gives user_0d_1 all privilages
CREATE USER
	IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	To 'user_0d_1'@'localhost';
