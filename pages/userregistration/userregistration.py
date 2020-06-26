from selenium.webdriver.common.by import By
from selenium import webdriver
from base.seleniumdriver import Selenium_Driver
import utilities.custom_logger as customLogger
import random
import logging


class Userregistration(Selenium_Driver):

    log = customLogger.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _signin_link = "//*[@class='login']"
    _email_address_create_account = "//*[@id='email_create']"
    _create_account_button = "SubmitCreate"
    _create_account_error = "//*[contains(text(),'Invalid email address')]"

    def click_on_signin_link(self):
        try:
            self.findElement(self._signin_link,"xpath").click()
            self.log.info("Signin Link clicked")
        except:
            self.log.error("Failed to click Signin Link")

# Enter Email Address in Create Account box
    def enter_email_address(self,text):
        try:
            email_field = self.findElement(self._email_address_create_account,"xpath")
            randno = random.randint(0,100)
            emailaddress = ("{}.{}@abcmail.com".format(text,randno))
            email_field.send_keys(emailaddress)
            self.log.info("Email address Entered")
        except:
            self.log.error("Failed to enter email address")


    def click_create_account(self):
        try:
            self.findElement(self._create_account_button,"name").click()
            self.log.info("Create Account Link clicked")
        except:
            self.log.error("Failed to click link")

    def unsuccessful_create_account(self):
        try:
            element = self.findElement(self._create_account_error,"xpath")
            self.log.info("Error message is found for Create Account")
            if element is not None:
                self.log.info("Validated error message Success")
                return True
            else:
                self.log.info("Validation error message - Failed")
                return False
        except:
            self.log.error("Unable to validate unsuccessful create account")