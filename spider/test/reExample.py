#-*- conding=utf-8 -*-

import re

# print(re.match('www','www,ooo,com'))
# print(re.match('com','www,ooo,com'))

# def double(match):
#     value = int(match.group('value'))
#     print(value)
#     return str(2*value)
# s = 'A23G4HFD567'
# print(re.sub(r'(?P<value>\d+)',double,s))

patt = re.compile(r'\W')
s = 'runoob,runoob,runoob'
list = re.split(patt,s)
print(list)
