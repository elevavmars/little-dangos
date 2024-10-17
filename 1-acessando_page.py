from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



browser = webdriver.Firefox()
print(browser)

browser.get('http://www.amazon.com.br')

# Acessando elementos
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys('monitor')
elem.send_keys(Keys.ENTER)




# browser.quit()