#! /usr/bin/python3
#-*- conding=utf-8 -*-

# test

import re,sqlite3
savepath = './doubantop250.db'
conn = sqlite3.connect(savepath)
print("打开{name}成功".format(name=savepath))
c = conn.cursor()
drop_sql = '''DROP TABLE TOP250'''
create_sql = '''CREATE TABLE TOP250(
            ID INT  PRIMARY KEY NOT NULL,
            cname TEXT,
            ename TEXT,
            actors TEXT,
            mark REAL,
            qoute TEXT, 
            link TEXT,
            pic TEXT);'''

