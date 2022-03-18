from selenium import webdriver

from test import PATH

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get('http://selenium.dev/')