# 使用 Selenium 模組自動開啟網頁
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.google.com/")

sleep(3)

driver.close()