from selenium import webdriver
from selenium.webdriver.common.by import By
import utilities.custom_logger as customlogger
import logging
from traceback import print_stack
import time
import os

class Selenium_Driver():

    log = customlogger.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

# Get By.Type

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.error("Locator type " + locatorType + " not correct/supported")
        return False

# Method to find_element

    def findElement(self,locator,locator_id='id'):
        try:
            locatortype = locator_id.lower()
            bytype = self.getByType(locatortype)
            element = self.driver.find_element(bytype,locator)
            self.log.info("Element found" +locator)
        except:
            self.log.error("Element not found" +locator)
        return element

# Verify Page Title

    def getpagetitle(self):
        try:
            element = self.driver.title
            self.log.info("Page Title Found")
            self.log.info(element)
            return element
        except:
            self.log.error("Unable to fetch page title")


    def verify_page_title(self,title):
        try:
            actual_page_title = self.getpagetitle()
            self.log.info(actual_page_title)
            if title.lower() in actual_page_title.lower():
                self.log.info("Page title verified")
                return True
            else:
                self.log.error("Page title not verified")
                return False
        except:
            self.log.error("Error identifying title")
            return False

# Is Element Present

    def isElementPresent(self,locator,locatorId='id'):
        try:
            element = self.findElement(locator,locatorId)
            if element is not None:
                self.log.info("Element is found" +locator)
                return True
            else:
                self.log.info("Element not found" +locator)
                return False
        except:
            self.log.error("Error finding element" + locator)
            return False