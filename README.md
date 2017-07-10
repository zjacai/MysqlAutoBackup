# MysqlAutoBackup


所有路径必须不包含空格，否则可能出现bug，导致无法成功备份！

配置说明：

	backup_path = 备份文件保存路径，如：D:\dataBackup
	bin_path = mysqldump文件实际路径（可保留默认：mysqldump.exe，误删除本目录下的mysqldump.exe）
	dbhost = 数据库主机地址
	dbname = 数据库名
	dbuser = 数据库用户
	dbuserpw = 加密后的密码
	dbcharset = 数据库编码


加密密码生成方法：

	cmd下运行：MysqlAutoBackup.exe 密码
