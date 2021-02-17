# 使用 Selenium 模組自動開啟網頁
from selenium import webdriver

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.get("https://tw.yahoo.com/")   # 進到yahoo的網站

driver.find_element_by_id("header-signin-link").click()  # 點擊登入的按鈕