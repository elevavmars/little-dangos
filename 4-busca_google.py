from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Termo de pesquisa
term = input('Digite o que deseja pesquisar:\n')

# Iniciando Driver
browser = webdriver.Firefox()
browser.get('https://www.google.com/')

# Encontrando o elemento
elem = browser.find_element(
    By.XPATH,
    "//textarea[@aria-label='Search']"
)

# Enviando termo para pesquisa
elem.send_keys(term)
elem.send_keys(Keys.ENTER)
