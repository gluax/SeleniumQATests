import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class dHubTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    
    def test_search(self):
        self.driver.get('https://hub.docker.com/')
        search_bar = self.driver.find_element_by_class_name('SearchBar__searchInput___34nC3')
        search_bar.send_keys('nginx')
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        repNumber = self.driver.find_element_by_class_name('left')
        self.assertEqual(repNumber.text, 'Repositories (16426)')
    
    def test_sign_up_fail_uname(self):
        self.driver.get('https://hub.docker.com/')
        uname = self.driver.find_element_by_name('Choose a Docker ID')
        uname.send_keys('txt')
        e = self.driver.find_element_by_class_name('FancyInput__error___TIz2p')
        self.assertEqual(e.text, 'Username must be at least four characters long')
    '''
    def test_sign_up_fail_email(self):
        self.driver.get('https://hub.docker.com/')
        email = self.driver.find_element_by_class_name('FancyInput__default___1Iybp')
        email.send_keys('txt')
        button = self.driver.find_element_by_class_name('Button__button___2lhyK Button__variant-primary___3QTAR')
        button.click()
        e = self.driver.find_element_by_class_name('')
        self.assertEqual(e.text, '')
    
    def test_sign_up_fail_pass(self):
        self.driver.get('https://hub.docker.com/')
        passw = self.driver.find_element_by_name('password')
        passw.send_keys('test')
        button = self.driver.find_element_by_class_name('Button__button___2lhyK Button__variant-primary___3QTAR')
        time.sleep(2)
        #button.click()
        #e = self.driver.find_element_by_class_name('FancyInput__error___TIz2p')
        #self.assertEqual(e.text, 'Ensure this value has at least 6 characters (it has 3).')
    '''  
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
