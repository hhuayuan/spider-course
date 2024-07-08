#coding = utf-8
import requests
from selenium import webdriver

def getHTML(url):
    my_content = requests.get(url) # 这里返回的是对象
    print(my_content.status_code)
    if my_content:
        html_bytes = my_content.content
        html = html_bytes.decode()
        print(html)
    else:
        print('error: content was empty.')


def bySelenium(url):
    client = webdriver.Chrome()
    client.get(url)
    html = client.page_source
    print(html)
    client.quit()

def bySelenium2(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')  # 改变navigator.webdriver 属性值

    client = webdriver.Chrome(options=options)
    client.get(url)
    print(client.page_source)

    client.quit()

if __name__ == '__main__':
    apiUrl = 'http://localhost:5000/api'
    pageUrl = 'http://localhost:5000'
    # getHTML(apiUrl)
    # bySelenium(pageUrl)
    bySelenium2(pageUrl)