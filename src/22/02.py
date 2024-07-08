#coding = utf-8
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    client.find_element(By.XPATH, "//button").click()
    # 等待页面加载完成
    time.sleep(3)

    html = client.page_source
    print(html)
    client.quit()


if __name__ == '__main__':
    pageUrl = 'http://localhost:5000/api/1716915496/8776a433a2bcc8fb5860ec4b68eed240'
    # getHTML(pageUrl)
    bySelenium('http://localhost:5000')