from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.userregistration.userregistration import Userregistration
import unittest
import pytest
import utilities.datadriven.testdata as data_set_up
from utilities.datadriven.testdata import data_set_up
from utilities.TestStatus import Test_Status

class Test_user_registration(unittest.TestCase):



    @pytest.fixture(autouse=True)
    def classMethod(self,one_time_setup):
        self.ur = Userregistration(self.driver)
        self.ts = Test_Status(self.driver)

    #driver = webdriver.Chrome()
    #ur = Userregistration(driver)
    #baseurl = "http://automationpractice.com/index.php"
    #driver.get(baseurl)
    #driver.implicitly_wait(10)
    #driver.maximize_window()
    #driver.quit()

    #def setUp(self):
    #    self.data = data_set_up('test_create_account_sucessful')
    #    print(self.data)

    def test_create_account_sucessful(self):
       self.baseurl = "http://automationpractice.com/index.php"
       data = data_set_up('test_create_account_sucessful')
       print(data)
       self.driver.get(self.baseurl)
       #self.driver.implicitly_wait(10)
       #self.driver.maximize_window()
       print("Running Test1")
       result1 = self.ur.verify_page_title(self.data[0])
       print(result1)
       self.ts.mark_test(result1,"Incorrect Page Title")
       #assert result1 == True
       self.ur.click_on_signin_link()
       result2 = self.ur.isElementPresent("SubmitCreate","name")
       self.ts.mark_test(result2,"Element Submit is not present")
       # assert result2 == True
       self.ur.enter_email_address(self.data[1])
       self.ts.mark_final_test('test_create_account_sucessful',result2,"Final")
        #self.ur.click_create_account()
        #result3 = self.ur.verify_page_title("Login")
        #assert result3 == True


    def test_create_account_unsucessful(self):
        self.baseurl = "http://automationpractice.com/index.php"
        self.driver.get(self.baseurl)
        data = data_set_up('test_create_account_unsucessful')
        print(data)
        #self.driver.implicitly_wait(10)
        #self.driver.maximize_window()
        print("Running Test2")
        result1 = self.ur.verify_page_title(self.data[0])
        #assert result1 == True
        self.ts.mark_test(result1,"Title is incorrect on Homepage")
        self.ur.click_on_signin_link()
        result2 = self.ur.isElementPresent("SubmitCreate","name")
        #assert result2 == True
        self.ts.mark_test(result2,"Submit button is not present")
        self.ur.click_create_account()
        self.driver.find_element(By.XPATH,"//*[contains(text(),'Invalid email address')]")
        result3 = self.ur.unsuccessful_create_account()
        self.ts.mark_final_test('test_create_account_unsucessful',result3,"The error message displayed is invalid")
        #assert result3 == True




