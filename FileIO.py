#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: acai
#desc: 文件读写模块
#2017-06-06 created


import os
import codecs

logPath="logs"

def isExistsFile(filename):
	if(os.path.exists(filename) and os.path.isfile(filename)):
		return True
	return False

def WriteFile(filename,content="",mode='a'):
	flag=0
	#print(content)
	try:
		fileHandle = codecs.open(filename, mode, 'utf-8')
		fileHandle.write(content + '\r')
		fileHandle.close()
		flag=1
	except:
		return flag
		pass
	return flag

def LogErr(content,filename='errlogs.log'):
	if(not os.path.exists(logPath)):
		os.makedirs(logPath)
	WriteFile(logPath+"/"+filename,content)

def ReadFile(filename):
	readText=""
	fh = codecs.open(filename, "r", 'utf-8')
	try:
		readText = fh.read()
	except:
		errs=unicode("文件读取出错："+str(filename),"utf-8")
		print(errs)
	finally:
		fh.close()
	return readText

def DeleteFile(filename):
	if isExistsFile(filename):
  		os.remove(filename)
