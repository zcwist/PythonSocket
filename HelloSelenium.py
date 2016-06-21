from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/kiwi/Downloads/chromedriver")
driver.get("http://localhost:8000")
# assert 'python' in driver.title
elem = driver.find_element_by_name('chat')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
# assert('No results found.' no in driver.page_source)
# driver.close()

