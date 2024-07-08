#coding=utf-8
import requests

my_content = requests.get('https://www.baidu.com') # 这里返回的是对象
print(my_content.status_code)
if my_content:
    text = my_content.text
    print(text)

    html_bytes = my_content.content
    html = html_bytes.decode()
    print(html)
else:
    print('error: content was empty.')