from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Iniciando Driver
browser = webdriver.Firefox()
browser.get('https://www.google.com/')