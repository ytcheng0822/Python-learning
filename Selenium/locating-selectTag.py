from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.timeanddate.com/")

monthElements = driver.find_element_by_id("month")

month = Select(monthElements)

month.select_by_visible_text("February")

countryElements = driver.find_element_by_id("country")

conuntry = Select(countryElements)

conuntry.select_by_visible_text("Taiwan")

driver.find_element_by_xpath("//body/div[@id='main-content']/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[4]/input[1]").click()