import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import random

driver = webdriver.Chrome()
driver.get('https://hub.docker.com/')
driver.get('https://hub.docker.com/')
driver.find_element_by_xpath('//section/ul[3]/li[3]/a').click()
uname = driver.find_element_by_xpath('//form/div[1]/input')
uname.send_keys('tester5683')
passw = driver.find_element_by_xpath('//form/div[2]/input')
passw.send_keys('qwertyuiop')
driver.find_element_by_xpath('//form/button').click()
rawr = driver.find_element_by_xpath('//h1')
print(rawr.text)
time.sleep(5)
driver.find_element_by_xpath('//section/ul[3]/li[5]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//section/ul[3]/li[5]/ul/li[7]/a').click()
time.sleep(5)
driver.quit()
