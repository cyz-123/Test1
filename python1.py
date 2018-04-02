#coding:utf-8
from selenium import webdriver
'''
======================================================
本文件是用与测试币币交易
======================================================
'''
driver=webdriver.Chrome()#打开谷歌浏览器
driver.maximize_window()
driver.get('http://192.168.2.103:8686/')#访问网站
