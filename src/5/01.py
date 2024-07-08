#coding=utf-8
import requests

my_content = requests.get('http://localhost/') # 这里返回的是对象
print(my_content.status_code)
if my_content:
    html_bytes = my_content.content #.text
    html = html_bytes.decode()
    print(html)
else:
    print('error: content was empty.')
