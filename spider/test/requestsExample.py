#/usr/bin/python3
#-*-conding=utf-8-*-

import requests

url = "http://www.baidu.com"
url2 = "http://www.httpbin.org"
url3 = "http://github.com"

r_get = requests.get(url2)
# r_post = requests.post(url2+ "/post",data={'key':'value'})
# r_delete = requests.delete(url2+ "/delete")

print(r_get.text)
# print(r.headers)
# print(r.encoding)
# print(r.json())

# print(r_get.status_code)    #响应状态码
# print(r_post.text)          #返回内容
# print(r_post.headers)       #响应头

# Cookie
# r = requests.get(url2+"/cookies",cookies = dict(cookies_are='working'))
# print(r.text)

####################
# 重定向与请求历史,github将网址重定向到https，状态吗为301
# r = requests.get(url3)
# print(r.url)
# print(r.status_code)
# print(r.history)
# 使用head启用重定向
# r = requests.head(url3,allow_redirects=True)
# print(r.url)
# print(r.history)

####################
# 超时
# r = requests.get(url3,timeout = 4)

####################
# 异常


####################
# 高级用法

