from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "/Users/kiwi/Downloads/chromedriver"
path = "/home/kiwi/Downloads/chromedriver"


driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("http://localhost:8000")
# assert 'python' in driver.title
elem = driver.find_element_by_name('chat')

file = open("PresolvedEnScript.log","r")

for line in file:
	elem.send_keys(line)
	time.sleep(0.1)

elem.send_keys(Keys.RETURN)

# driver.close()

