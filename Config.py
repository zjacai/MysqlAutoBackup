#/usr/bin/python
# coding=utf-8
#author: 佚名
#desc: 配置文件读写模块


import ConfigParser
import codecs

class AppConfig:
    __cp = ConfigParser.SafeConfigParser()
    __confile = "myapp.conf"
    def __init__(self,filename):
        self.__confile=filename
        with codecs.open(filename, "r", encoding="utf-8") as f:
            try:
                self.__cp.readfp(f)
            except:
                print "read %s error!" %(filename)

    def read_config(self,section,key):
        try:
            val = self.__cp.get(section, key)
        except:
            val = ""
        return  val

    def write_config(self,section,key,value):
        self.__cp.set(section,key,value)
        self.__cp.write(open(self.__confile, "w"))