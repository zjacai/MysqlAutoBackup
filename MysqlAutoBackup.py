#!/usr/bin/env python
#encoding=utf-8
#author: acai
#desc: Mysql auto backup


import os, sys, datetime
import rc4
import Config
import FileIO

p,f=os.path.split(sys.argv[0])
fn,fext=os.path.splitext(f)
configfile='%s.conf'%fn

os.chdir(p)

public_key="acai"
_rc4=rc4.rc4(public_key)

currPath=p + "\dataBackup"

def MysqlBackup():
	try:
		conf = Config.AppConfig(configfile)
		backup_path = conf.read_config("backupset","backup_path")
		backup_path = backup_path if(backup_path) else currPath
		if(not os.path.exists(backup_path)):
			os.makedirs(backup_path)
		bin_path = conf.read_config("backupset","bin_path")
		if(not FileIO.isExistsFile(bin_path)):
			error=u"%s mysqdump文件不存在，无法备份，请重新指定bin文件路径" % (str(datetime.datetime.now())[:16])
			print(error)
			FileIO.LogErr(error,"log.txt")
			sys.exit(1)
		dbhost = conf.read_config("backupset","dbhost")
		dbname = conf.read_config("backupset","dbname")
		dbuser = conf.read_config("backupset","dbuser")
		rc4passwd = conf.read_config("backupset","dbuserpw")
		dbuserpw = _rc4.decode(rc4passwd)
		dbcharset = conf.read_config("backupset","dbcharset")

	except Exception, e:
		error=u"%s Error: %s." % (str(datetime.datetime.now())[:16],e)
		print(error)
		sys.exit(1)

	now = str(datetime.datetime.now())[:10]
	backupname="%s\\%s_%s.sql"%(backup_path, dbname, now)

	backup_command = """%s -B %s -h"%s" -u"%s" -p"%s" --default_character-set=%s --opt>"%s"\n""" % (bin_path,dbname, dbhost, dbuser, dbuserpw, dbcharset, backupname)

	try:
		os.system(backup_command)
		error=u"%s %s 备份成功！" % (str(datetime.datetime.now())[:16], backupname)
		print(error)
		FileIO.LogErr(error,"log.txt")
	except Exception, e:
		error=u"%s 备份出错！" % str(datetime.datetime.now())[:16]
		print(error)
		FileIO.LogErr(error,"log.txt")
		sys.exit(1)

	print "Done!"

if __name__ == "__main__":
	_rc4=rc4.rc4(public_key)
	if len(sys.argv) >= 2:
	    pwd_org = sys.argv[1]
	    pwd_new = _rc4.encode(pwd_org)
	    print(pwd_new)
	else:
		MysqlBackup()
