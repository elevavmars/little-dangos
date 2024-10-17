from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Acessando site
browser = webdriver.Firefox()
browser.get('https://registro.br')

# Buscando elementos
elem = browser.find_element(By.ID, 'is-avail-field')
elem.clear()
elem.send_keys('botscompython.com.br')
elem.send_keys(Keys.ENTER)
time.sleep(5)
# browser.save_screenshot('dominio.png')

# Buscando informações
results = browser.find_elements(By.TAG_NAME, 'strong')

print(f'Dominio {results[1].text} está {results[2].text}.')
 
# import pdb
# pdb.set_trace()

# browser.quit()