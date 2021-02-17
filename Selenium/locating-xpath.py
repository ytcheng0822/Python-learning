# # 使用 Selenium 模組自動開啟網頁
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.get("http://www.op.gg/")

driver.find_element_by_xpath("//a[contains(text(),'英雄分析')]").click()

sleep(3)

driver.find_element_by_xpath("//a[contains(text(),'統計')]").click()

sleep(3)

driver.find_element_by_xpath("//a[contains(text(),'汎')]").click()

sleep(5)

driver.quit()


