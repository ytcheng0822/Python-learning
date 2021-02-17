# 使用 Selenium 模組自動開啟網頁
from selenium import webdriver

driver=webdriver.Chrome("C:/Users/User/chromedriver.exe")

driver.get("https://www.google.com/")   # 進到Google的網站

# 搜尋龍華科技大學
# driver.find_element_by_css_selector("div.L3eUgb:nth-child(2) div.o3j99.ikrT4e.om7nvf:nth-child(3) div.A8SBwf:nth-child(1) div.RNNXgb:nth-child(2) div.SDkEP div.a4bIc > input.gLFyf.gsfi:nth-child(3)").send_keys("龍華科技大學\n")

# 進入校園入口網
# driver.find_element_by_css_selector("body.srp.vasq:nth-child(2) div.main:nth-child(9) div.GyAeWb:nth-child(12) div.D6j0vc:nth-child(2) div.eqAnXb:nth-child(3) div.g:nth-child(1) table.jmjoTe:nth-child(3) tr.mslg.dmenKe:nth-child(2) td:nth-child(1) div.usJj9c h3.r > a.l").click()

# 輸入id
# driver.find_element_by_css_selector("#muid").send_keys("id")

# 輸入password
# driver.find_element_by_css_selector("#mpassword").send_keys("password")

# driver.find_element_by_css_selector("div.L3eUgb:nth-child(2) div.o3j99.ikrT4e.om7nvf:nth-child(3) div.A8SBwf:nth-child(1) div.RNNXgb:nth-child(2) div.SDkEP div.a4bIc > input.gLFyf.gsfi:nth-child(3)").send_keys("85porn\n")

# driver.find_element_by_css_selector("body.srp.vasq:nth-child(2) div.main:nth-child(9) div.GyAeWb:nth-child(12) div.D6j0vc:nth-child(2) div.eqAnXb:nth-child(3) div.g:nth-child(1) div.tF2Cxc div.yuRUbf a:nth-child(1) div.TbwUpd.NJjxre:nth-child(3) > cite.iUh30.Zu0yb.tjvcx").click()

# driver.find_element_by_css_selector("div.sticky-top:nth-child(4) nav.navbar.navbar-expand-md.navbar-dark.bg-dark div.container div.collapse.navbar-collapse ul.navbar-nav.mr-auto:nth-child(1) li.nav-item:nth-child(4) > a.nav-link").click()