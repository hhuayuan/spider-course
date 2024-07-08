#coding=utf-8
import requests
from lxml import etree

my_content = requests.get('http://localhost') # 这里返回的是对象
print(my_content.status_code)
if my_content:
    html_bytes = my_content.content
    html = html_bytes.decode()
    # print(html)
    root = etree.HTML(html)
    bodys = root.xpath("body")
    if len(bodys) > 0:
        print(bodys[0].text)
else:
    print('error: content was empty.')

