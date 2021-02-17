# 使用 Selenium 模組自動開啟網頁
from selenium import webdriver

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.get("https://leetcode.com/")  # 開啟leetcode的網頁

elements=driver.find_elements_by_tag_name("span")  # 尋找原始碼中所有的 <span> 標籤

# print(elements.text)  # 將找到的標籤內容文字印出來

for element in elements:
    if "Sign in" in element.text:    # 如果標籤內容文字有 Sign in
        element.click()              # 就點擊一下
    
# driver.quit()