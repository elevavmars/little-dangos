from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Acessando site
browser = webdriver.Firefox()
browser.get('https://registro.br')

# Lista de dominios
domains = [
    'botscompython.com.br',
    'meta.com',
    'databot.com',
    'pybootcamp.com'
]

file = open('domains.txt', 'w', encoding='utf-8')

# Manipulando elementos
for domain in domains:
    elem = browser.find_element(By.ID, 'is-avail-field')
    elem.clear()
    elem.send_keys(domain)
    elem.send_keys(Keys.ENTER)
    time.sleep(3)
# Buscando informações
    results = browser.find_elements(By.TAG_NAME, 'strong')
    text = f'Dominio {results[1].text} está {results[2].text}\n'
    print(text)
    file.write(text)

file.close()
browser.close()