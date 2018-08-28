#!/bin/bash

export PATH=$PATH:/opt/jdk7/bin:/opt/jdk7/jre/bin:/usr/lib64/qt-3.3/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/pyrules/oracle11g
export ORACLE_HOME=/usr/local/pyrules/oracle11g

/usr/local/bin/python /usr/local/pyrules/bin/firewall_rules.py
