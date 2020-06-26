from selenium import webdriver
from selenium.webdriver.common.by import By
from spellchecker import SpellChecker
from selenium.webdriver import ActionChains
import re
import pytest
import unittest
import time

class Test_Learning(unittest.TestCase):

    #@pytest.fixture(autouse=True)
    #def setup(self):
    #    print("Running Before test")
    #    self.baseurl = "http://the-internet.herokuapp.com/"
    #    self.driver = webdriver.Chrome()
    #    self.driver.maximize_window()
    #    self.driver.implicitly_wait(10)
    #    self.driver.get(self.baseurl)
    #    yield
    #    print("Tear Down")
    #    self.baseurl = "http://the-internet.herokuapp.com/"
    #    self.driver = webdriver.Chrome()
    #    self.driver.maximize_window()
    #    self.driver.implicitly_wait(10)
    #    #request.cls.driver = driver
    #    yield self.driver
    #    self.driver.quit()


    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.driver = setUp

    def test_handlingtypo(self):
        print("Start")
        #self.baseurl = "http://the-internet.herokuapp.com/"
        #self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        #self.driver.implicitly_wait(10)
        #self.driver.get(self.baseurl)
        #self.driver = learningSetup
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element(By.LINK_TEXT,"Typos").click()
        spell = SpellChecker()
        text = self.driver.find_element(By.XPATH,"//*[@class='example']").text
        print(text)
        new = re.split('[, .\n]',text)
        print(new)
        misspelled = spell.unknown(new)
        print("{}".format(misspelled))


    def test_WYSIWYG_editor(self):
        print("Start")

        actions = ActionChains(self.driver)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element(By.LINK_TEXT,"WYSIWYG Editor").click()
        self.driver.find_element(By.XPATH,"//*[text()='File']").click()
        new_document = self.driver.find_element(By.XPATH,"//*[text()='New document']")
        actions.move_to_element(new_document).click().perform()
        print("New Document clicked")
        self.driver.find_element(By.XPATH,"//*[text()='Formats']").click()
        headings = self.driver.find_element(By.XPATH,"//*[@id='mceu_34']")
        actions.move_to_element(headings).click().perform()
        heading2 = self.driver.find_element(By.XPATH,"//*[@id='mceu_52']")
        actions.move_to_element(heading2).click().perform()
        iframe = self.driver.find_element(By.ID,"mce_0_ifr")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.ID,"tinymce").send_keys("The new born son")
        time.sleep(10)


    def test_table_validation(self):
        print("Validating a Table")
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element(By.LINK_TEXT,"Sortable Data Tables").click()
        rows = len(self.driver.find_elements_by_xpath('/html/body/div/div/div//table[@id="table1"]//tbody/tr'))
        cols = len(self.driver.find_elements_by_xpath('/html/body/div/div/div//table[@id="table1"]//tbody/tr[1]/td'))
        print(rows)
        print(cols)
        first_part = '/html/body/div/div/div//table[@id="table1"]//tbody/tr['
        second_part = ']/td[4]'
        third_part = ']/td[1]'
        for r in range(1,rows+1):
                #print("R="+str(r))
                fin_part = first_part+str(r)+third_part
                #print(fin_part)
                element = self.driver.find_element(By.XPATH,fin_part).text
                if element == "Conway":

                    for c in range(1,cols+1):
                        #print("C"+str(c))
                        final_part = first_part+str(r)+second_part
                        #print(final_part)
                        value = self.driver.find_element(By.XPATH,final_part).text
        print(value,end='  ')
        assert value == '$50.00'
        #print(" ")
#
