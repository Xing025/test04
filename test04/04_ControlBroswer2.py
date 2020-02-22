#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('http://182.92.197.48:8080/forum')
time.sleep(3)

#by_css_selector用法
# 定位文章标题“零基础如何学软件测试”并点击进入页面
driver.find_element_by_css_selector("h2.fly-tip>a").click()
time.sleep(3)
#刷新页面
driver.refresh()
time.sleep(3)
#返回前一页
driver.back()
time.sleep(3)
#前进历史中前一页，若历史中没有前一页就无反应
driver.forward()
time.sleep(3)
#关闭浏览器
driver.quit()