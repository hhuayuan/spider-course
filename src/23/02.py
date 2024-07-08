#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def bySelenium(url):
    client = webdriver.Chrome()
    client.get(url)
    # 等待页面加载完成
    time.sleep(2)

    # 定位滑块和滑块背景元素
    slider = client.find_element(By.ID, 'slider')
    slider_background = client.find_element(By.CLASS_NAME, 'slider-container')
    # 获取滑块和滑块背景的宽度
    slider_width = slider.size['width']
    background_width = slider_background.size['width']
    # 计算需要滑动的距离
    distance = background_width - slider_width
    # 创建一个 ActionChains 对象
    actions = ActionChains(client)

    # 模拟点击并按住滑块
    actions.click_and_hold(slider).perform()

    # 拖动滑块到指定距离
    actions.move_by_offset(30, 0).perform()
    actions.move_by_offset(40, 3).perform()
    actions.move_by_offset(20, 2).perform()
    actions.move_by_offset(distance - 90, 0).perform()
    # actions.move_by_offset(distance, 0).perform()

    # 释放滑块
    actions.release().perform()
    # 等待验证完成
    time.sleep(3)  # 等待验证结果，时间根据实际情况调整

    html = client.page_source
    print(html)
    client.quit()


if __name__ == '__main__':
    pageUrl = 'http://localhost:5000'
    bySelenium(pageUrl)