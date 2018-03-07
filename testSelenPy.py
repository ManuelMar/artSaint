import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

q = "batman-1-6-scale-figure"
#For headless add arg : chrome_options = chrome_options
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://mondotees.com/search?q=")

searchBar = driver.find_element_by_name("q")
searchBar.clear()

searchBar.send_keys(q)
searchBar.send_keys(Keys.RETURN)

lists= driver.find_elements_by_class_name("search-result-title")
print ("Found"  + str(len(lists)) + "searches:")
lists[0].click();

addToCart = driver.find_element_by_name("add").click()
time.sleep(.5)
driver.get("https://mondotees.com/cart")

checkOut = driver.find_element_by_name("checkout")
checkOut.click()
#email = driver.find_element_by_name("checkout[email]")
#email.clear()
#email.send_keys("mgm264@cornell.edu")


print('Success search')
driver.get_screenshot_as_file("capture.png")
time.sleep(5) # Let the user actually see something!

assert "No results found." not in driver.page_source


driver.close()


#assert "mondotees" in driver.title
#icon = driver.find_element_by_css_selector('.icon-search.hdr-search').click()
#elem.clear()

#
