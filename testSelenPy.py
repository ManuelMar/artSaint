import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://mondotees.com")
#assert "mondotees" in driver.title
icon = driver.find_element_by_css_selector('.icon-search.hdr-search').click()
#elem.clear()
searchBar = driver.find_element_by_name("q")
searchBar.clear()

searchBar.send_keys("batman-1-6-scale-figure")
searchBar.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
#time.sleep(5) # Let the user actually see something!

driver.close()
