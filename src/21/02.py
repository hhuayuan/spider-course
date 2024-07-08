#coding = utf-8
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getHTML(url):
    my_headers = {'Cookie':'session=.eJydTkmKwzAQ_IrosxnaUmuxXzH3IYSWuhUbnAXLOYX8fQT5QU5FUesLznXjtmiD-e8F5ugAV22NLwoD_G7KTc12v5j1Zo674VK6aI5lbebRPT9weg9f5k5DH9-1LTAf-1M7WwVmCCkzWedRapAxeRcxTRSzhjwhJ1-tSCrqxGWxkQv37m7T5FGnqEGKtWhHq0jVTxgDYopxxIyhSurNpVKmkusYHVHKnosvTEzBY6AS-v3zs-n-ecNyXW_w_gd40lpC.ZlYIHw.M1gQ5S5aIhhwvfaplSjnwxXBvgM; HttpOnly; Path=/'}
    my_content = requests.get(url, headers=my_headers) # 这里返回的是对象
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
    client.find_element(By.ID, 'username').send_keys('admin')
    client.find_element(By.ID, 'password').send_keys('admin')
    client.find_element(By.XPATH, "//button[@type='submit']").click()
    # 等待页面加载完成
    wait = WebDriverWait(client, 10)
    wait.until(EC.title_contains('数据页面'))

    html = client.page_source
    print(html)
    client.quit()


if __name__ == '__main__':
    pageUrl = 'http://localhost:5000'
    # getHTML(pageUrl)
    bySelenium(pageUrl)