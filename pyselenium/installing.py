from selenium import webdriver

driver = webdriver.Chrome()

url = "http://github.com/toygarpar"

driver.get(url)

#selenium temelleri


from selenium import webdriver
import time



driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(2) # iki saniye bekle
driver.maximize_window() # page ekranını büyüt
driver.save_screenshot("github.com-homepage.png") # take a screenshot of the github.com page

url = "http://github.com/toygarpar"
driver.get(url)



print(driver.title) #page title

if "toygarpar" in driver.title:
    driver.save_screenshot("github-toygarpar.png")


time.sleep(2)



driver.back()
driver.forward()
time.sleep(2)
driver.back()

time.sleep(2)

driver.close()



#selenium için selectors bilgisi -selectors.html içinde elemanlara nasıl ulaşacağız

#selenium ile sayfa etkileşimi

"""
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

"""