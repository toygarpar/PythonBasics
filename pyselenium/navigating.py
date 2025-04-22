from selenium import webdriver
import time


driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)


searchInput = driver.find_element_by_xpath('//*[@id="query-builder-test"]')

time.sleep(1)

searchInput.send_keys("python")



time.sleep(2)

driver.close()

searchInput.send_keys(Keys.ENTER)

time.sleep(2)

driver.close()