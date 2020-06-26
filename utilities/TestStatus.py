from selenium import webdriver
from base.seleniumdriver import Selenium_Driver
import utilities.custom_logger as customLogger
import logging

class Test_Status(Selenium_Driver):

    log = customLogger.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.resultset = []

    def test_result(self,result,message):
        try:
            if result is not None:

                if result:
                    self.resultset.append("Pass")
                    self.log.info("*****Verification Passed*****")
                else:
                    self.resultset.append("Fail")
                    self.log.error("*****Verification Failed*****")
                    self.screenShot(message)
            else:
                self.resultset.append("Fail")
                self.log.error("*****Verification Failed*****")
                self.screenShot(message)
        except:
            self.resultset.append("Fail")
            self.log.error("*****Verification Failed*****")
            self.screenShot(message)

    def mark_test(self,result,message):
        self.test_result(result,message)

    def mark_final_test(self,testname,result,message):

        self.test_result(result, message)

        if 'Fail' in self.resultset:
            self.log.error("***Test Case Failed ***")
            self.resultset.clear()
            assert True == False
        else:
            self.log.error("***Test Case Passed ***")
            self.resultset.clear()
            assert True == True

