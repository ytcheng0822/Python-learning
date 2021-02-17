# 使用 Selenium 模組自動開啟網頁
from selenium import webdriver
import time

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.get("https://www.youtube.com/")  # 開啟youtube網頁


# 找到搜尋欄內的 name="search_query" 輸入Inty python tutorials, "\n"當作Enter
driver.find_element_by_name("search_query").send_keys("Inty python selenium\n")

# time.sleep(5)  # 執行5秒後

# driver.quit()  # 關閉網頁