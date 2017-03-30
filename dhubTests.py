import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import random

class dHubTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_search(self):
        '''a good thing to automatically test because you can automate and make sure correct
        search results appear'''
        self.driver.get('https://hub.docker.com/')
        search_bar = self.driver.find_element_by_class_name('SearchBar__searchInput___34nC3')
        search_bar.send_keys('nginx')
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        offical = self.driver.find_element_by_class_name('undefined')
        self.assertEqual(offical.text, 'official')
    
    def test_sign_up_fail_uname(self):
        '''another good thing to automate to make sure no invalid usernames can be used
        to make an account'''
        self.driver.get('https://hub.docker.com/')
        uname = self.driver.find_element_by_xpath('//form/div[1]/div/input')
        uname.send_keys('txt')
        e = self.driver.find_element_by_class_name('FancyInput__error___TIz2p')
        self.assertEqual(e.text, 'Username must be at least four characters long')
       
    def test_sign_up_fail_passw(self):
        '''once again automate to make sure no possible invalid passwords can be 
        used to make an account'''
        self.driver.get('https://hub.docker.com/')
        passw = self.driver.find_element_by_xpath('//form/div[3]/div/input')
        passw.send_keys('test')
        self.driver.find_element_by_xpath('//form/div[4]/button').click()
        time.sleep(1)
        e = self.driver.find_element_by_xpath('//form/div[3]/div/div')
        self.assertEqual(e.text, 'Ensure this value has at least 6 characters (it has 4).')
    
    def test_sign_up(self):
        '''make sure a proper account names and user names and emails can be used to make an account '''
        self.driver.get('https://hub.docker.com/')
        uname = self.driver.find_element_by_xpath('//form/div[1]/div/input')
        uname.send_keys('tester'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)))
        email = self.driver.find_element_by_xpath('//form/div[2]/div/input')
        email.send_keys(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))+'@gmail.com')
        passw = self.driver.find_element_by_xpath('//form/div[3]/div/input')
        passw.send_keys('qwertyuiop')
        self.driver.find_element_by_xpath('//form/div[4]/button').click()
        time.sleep(2)
        sutext = self.driver.find_element_by_class_name('SignupForm__subtext___1JThA')
        self.assertEqual(sutext.text, 'Please check your email to activate your account.')

        
    def test_log_in_fail(self):''' '''
        '''good to automate as you never want someone to be able to log in
        when incorrect information is entered'''
        self.driver.get('https://hub.docker.com/')
        self.driver.find_element_by_xpath('//section/ul[3]/li[3]/a').click()
        uname = self.driver.find_element_by_xpath('//form/div[1]/input')
        uname.send_keys('tester568')
        passw = self.driver.find_element_by_xpath('//form/div[2]/input')
        passw.send_keys('qwertyuiop')
        self.driver.find_element_by_xpath('//form/button').click()
        time.sleep(1)
        e = self.driver.find_element_by_class_name('styles__error__1v2q-')
        #self.assertEqual(e, 'Incorrect authentication credentials.')
    
    def test_log_in(self):
        '''test to make sure accounts can properly log in and so that users will
        never have an issue logging in'''
        self.driver.get('https://hub.docker.com/')
        self.driver.find_element_by_xpath('//section/ul[3]/li[3]/a').click()
        uname = self.driver.find_element_by_xpath('//form/div[1]/input')
        uname.send_keys('tester5683')
        passw = self.driver.find_element_by_xpath('//form/div[2]/input')
        passw.send_keys('qwertyuiop')
        self.driver.find_element_by_xpath('//form/button').click()
        time.sleep(1)
        confirm = self.driver.find_element_by_xpath('//h1').text
        expand = self.driver.find_element_by_xpath('//section/ul[3]/li[5]/a')
        expand.click()
        logout = self.driver.find_element_by_xpath('//section/ul[3]/li[5]/ul/li[7]/a')
        logout.click()
        self.assertEqual(confirm, 'Welcome to Docker Hub')
       
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
