#coding = utf-8
import requests
import lxml

my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
              "Referer":"http://localhost"}
my_content = requests.get('http://localhost/sub.html', headers=my_headers) # 这里返回的是对象
print(my_content.status_code)
if my_content:
    html_bytes = my_content.content
    html = html_bytes.decode()
    print(html)
else:
    print('error: content was empty.')
