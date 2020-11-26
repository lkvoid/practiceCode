# -*-conding=utf-8-*-

import sqlite3

conn = sqlite3.connect('test.db')
print("打开数据库成功")
c = conn.cursor()
#######创建表###########
# c.execute('''CREATE TABLE COMPANY(
#         ID INT  PRIMARY KEY NOT NULL,
#         name TEXT NOT NULL,
#         AGE INT NOT NULL,
#         ADDRESS CHAR(50),
#         SALARY REAL);''')
# print("成功创建表COMPANY")

#######插入表###########
# c.execute('''INSERT into COMPANY(
#         ID,NAME,AGE,ADDRESS,SALARY)
#         VALUES(
#         1,'Paul',32,'California',20000.00)''')
#
# c.execute('''INSERT INTO COMPANY (
#         ID,NAME,AGE,ADDRESS,SALARY)
#         VALUES (
#         2, 'Allen', 25, 'Texas', 15000.00 )''')
#
# c.execute('''INSERT INTO COMPANY (
#         ID,NAME,AGE,ADDRESS,SALARY)
#         VALUES (
#         3, 'Teddy', 23, 'Norway', 20000.00 )''')
#
# c.execute('''INSERT INTO COMPANY (
#         ID,NAME,AGE,ADDRESS,SALARY)
#         VALUES (
#         4, 'Mark', 25, 'Rich-Mond ', 65000.00 )''')
# print("插入成功")

#######查询###########

sql1 = "SELECT ID,name,AGE,ADDRESS,SALARY from COMPANY"
data_list = c.execute(sql1)
print(data_list)
for row in data_list:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("AGE=",row[2])
    print("ADDRESS=",row[3])
    print("SALARY=",row[4])


conn.commit()
print("成功提交")
conn.close()
print("数据库已关闭")






