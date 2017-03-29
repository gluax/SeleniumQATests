import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://hub.docker.com/')
input = driver.find_element_by_xpath('//form/div[1]/div/input')
input.send_keys('test')
#input = driver.find_element_by_xpath('//input[3]')
#input.send_keys('3')
#input = driver.find_element_by_xpath('//input[4]')
#input.send_keys('4')
time.sleep(5)
driver.quit()
