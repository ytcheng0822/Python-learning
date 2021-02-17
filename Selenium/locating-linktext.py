# 使用 Selenium 模組自動開啟網頁
from selenium import webdriver
import time

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.get("https://www.google.com/") # 開啟Google的網頁

# link_text 找到一串連結最後面的 text
driver.find_element_by_link_text("Gmail").click() # 找到 Gmail 的link_text,並且點擊

driver.back()  # 回到上一頁

# partial_link_text 找到一串連結最後面的部分 text
driver.find_element_by_partial_link_text("商店").click() # 找到 Google 商店 的partial_link_text,並且點擊

# time.sleep(5)

# driver.quit()