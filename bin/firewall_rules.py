#!/usr/bin/python
#coding=utf-8
import cx_Oracle
import sys
import urllib
import os
import csv
import random
import time
import hashlib
import datetime

#var = 1
#while var == 1:
#connect db select infomation section
#注意这里要设置默认的拒绝策略和白名单：
#iptables -A INPUT --source 196.128.1.0/24  --dport 80  -j REJECT
#iptables -I INPUT --source-mac      --dport  80  -j REJECT
#############################配置白名单列表#################################

orcl = cx_Oracle.connect('exam_admin2009/oracleadmin@192.168.0.1:1521/nc')
curs = orcl.cursor()

printHeader = True

sql = "select * from tab where tname='EXAM_KTXX_WHITE'"
curs.execute(sql)

for row_data in curs:
        outputFile = open('/usr/local/pyrules/conf/mac_white_new.table','wb') # 'wb'
        output = csv.writer(outputFile)
        sql = "select mac from exam_ktxx_white "
        curs2 = orcl.cursor()
        curs2.execute(sql)

        for row_data in curs2: # add table rows
            output.writerow(row_data)

        outputFile.close()

os.popen('dos2unix /usr/local/pyrules/conf/mac_white_new.table 2&> /dev/null')

#if  file  
def getHash(f):                       #定义函数md5
   line=f.readline()
   hash=hashlib.md5()
   while(line):
       hash.update(line)
       line=f.readline()
   return hash.hexdigest()


if os.access("/usr/local/pyrules/conf/mac_white_old.table", os.F_OK):  #判断文件是否存在

        f1=open("/usr/local/pyrules/conf/mac_white_new.table","rb")
        f2=open("/usr/local/pyrules/conf/mac_white_old.table","rb")

        str1=getHash(f1)
        str2=getHash(f2)
        if str1 == str2:  #判断文件是否相同
               print "white is same file"      #相同不执行任何操作，不需要添加和删除规则
        else:      #如果不相同读取old文件内容执行delete，然后读取new重新添加规则
            file = open("/usr/local/pyrules/conf/mac_white_old.table")
            while 1:
                 lines = file.readlines(200)
                 if not lines:
                     break
                 for line in lines:
                     mac = line
                     strmac = str(mac)
                     os.popen('iptables -D INPUT -p tcp --dport 80 -m mac -j ACCEPT --mac-source %s'% (strmac))
                     os.popen('service iptables save')
#删除规则
#添加规则

            file = open("/usr/local/pyrules/conf/mac_white_new.table")
            while 1:
                 lines = file.readlines(200)
                 if not lines:
                     break
                 for line in lines:
                     mac = line
                     strmac = str(mac)
                     os.popen('iptables -I INPUT -p tcp --dport 80 -m mac -j ACCEPT --mac-source %s'% (strmac))
                     os.popen('service iptables save')
            os.popen('cp /usr/local/pyrules/conf/mac_white_new.table  /usr/local/pyrules/conf/mac_white_old.table')

else:    #如果没有old文件，这是对于新创建的时候执行的。
#set iptables rules section
        file = open("/usr/local/pyrules/conf/mac_white_new.table")
        while 1:
             lines = file.readlines(200)
             if not lines:
                 break
             for line in lines:
               	 mac = line
                 strmac = str(mac)
                 os.popen('iptables -I INPUT -p tcp --dport 80 -m mac -j ACCEPT --mac-source %s'% (strmac))
                 os.popen('service iptables save')
        os.popen('cp /usr/local/pyrules/conf/mac_white_new.table  /usr/local/pyrules/conf/mac_white_old.table')

##############配置维考台机信任列表##########################################
orcl = cx_Oracle.connect('exam_admin2009/oracleadmin@192.168.0.1:1521/nc')
curs = orcl.cursor()

printHeader = True

sql = "select * from tab where tname='EXAM_KTXX'"
curs.execute(sql)

for row_data in curs:
        outputFile = open('/usr/local/pyrules/conf/mac_list_new.table','wb') # 'wb'
        output = csv.writer(outputFile)
        sql = "select mac from exam_ktxx "
        curs2 = orcl.cursor()
        curs2.execute(sql)

        for row_data in curs2: # add table rows
            output.writerow(row_data)

        outputFile.close()

os.popen('dos2unix /usr/local/pyrules/conf/mac_list_new.table 2&> /dev/null')

#if  file  
def getHash(f):                       #定义函数md5
   line=f.readline()
   hash=hashlib.md5()
   while(line):
       hash.update(line)
       line=f.readline()
   return hash.hexdigest()


if os.access("/usr/local/pyrules/conf/mac_list_old.table", os.F_OK):  #判断文件是否存在

        f1=open("/usr/local/pyrules/conf/mac_list_new.table","rb")
        f2=open("/usr/local/pyrules/conf/mac_list_old.table","rb")

        str1=getHash(f1)
        str2=getHash(f2)
        if str1 == str2:  #判断文件是否相同
               print "ktj is same file"      #相同不执行任何操作，不需要添加和删除规则
        else:      #如果不相同读取old文件内容执行delete，然后读取new重新添加规则
            file = open("/usr/local/pyrules/conf/mac_list_old.table")
            while 1:
                 lines = file.readlines(200)
                 if not lines:
                     break
                 for line in lines:
                     mac = line
                     strmac = str(mac)
                     os.popen('iptables -D INPUT -p tcp --dport 80 -m mac -j ACCEPT --mac-source %s'% (strmac))
                     os.popen('service iptables save')
#删除规则
#添加规则

            file = open("/usr/local/pyrules/conf/mac_list_new.table")
            while 1:
                 lines = file.readlines(200)
                 if not lines:
                     break
                 for line in lines:
                     mac = line
                     strmac = str(mac)
                     os.popen('iptables -I INPUT -p tcp --dport 80 -m mac -j ACCEPT --mac-source %s'% (strmac))
                     os.popen('service iptables save')
            os.popen('cp /usr/local/pyrules/conf/mac_list_new.table  /usr/local/pyrules/conf/mac_list_old.table')

else:    #如果没有old文件，这是对于新创建的时候执行的。
#set iptables rules section
        file = open("/usr/local/pyrules/conf/mac_list_new.table")
        while 1:
             lines = file.readlines(200)
             if not lines:
                 break
             for line in lines:
               	 mac = line
                 strmac = str(mac)
                 os.popen('iptables -I INPUT -p tcp --dport 80 -m mac -j ACCEPT --mac-source %s'% (strmac))
                 os.popen('service iptables save')

        os.popen('cp /usr/local/pyrules/conf/mac_list_new.table  /usr/local/pyrules/conf/mac_list_old.table')

#time.sleep(20)

time_stamp = datetime.datetime.now()
print "time_stamp       " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S')  
