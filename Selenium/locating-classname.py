# 使用 Selenium 模組自動開啟網頁
from selenium import webdriver

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.get("https://www.douban.com/")  # 開啟豆瓣的網頁

# 尋找 class="lnk-music" ,並且點擊進入電影
driver.find_element_by_class_name("lnk-movie").click()

# class_name方法非常少用,因為大多數網站的class_name都不是唯一的