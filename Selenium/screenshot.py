from selenium import webdriver

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.google.com/")

driver.save_screenshot("D:/Users/user/OneDrive/桌面/截圖.png")

driver.close()