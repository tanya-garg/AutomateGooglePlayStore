from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time


class Driver:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/Tanya.a.garg/PycharmProjects/chromedriver_win32 (2)/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # method to navigate to the URL
    def navigate(self, url):
        if isinstance(url, str):
            self.driver.get(url)
        else:
            raise TypeError("URL must be a string.")

    # Get web element based on the locator value
    def getelements(self,locator):
        try:
            element = self.driver.find_elements(By.XPATH,locator)
            return element
        except:
            self.log.info("Element not found")


    # Get web element based on the locator value
    def getelement(self, locator):
        try:
            element = self.driver.find_element(By.XPATH, locator)
            return element
        except Exception as e:
            print(e)
            #self.log.info("Element not found")

    # Method to find web element occurance
    def findelement(self,locator):
        try:
            elementtofind = None
            elementtofind = self.driver.find_elements(By.XPATH,locator)
            # If element occurance found then return True
            if len(elementtofind) > 0:
                return True
            else:
                return False
                self.log.info("Element not found")
        except:
            self.log.info("Some error occured, element not found")
            return False

    # Method to perform element click
    def elementClick(self,locator):
        try:
            self.driver.execute_script("arguments[0].click();",locator)
           # print("clicked")
            # self.getelement(locator).click()
            return True
        except Exception as e:
            print(e)
            return False

    # Method for scrolling of web page
    def webScroll(self, direction):

        try:
            if direction == 'up':
                self.driver.execute_script("window.scrollBy(0,-1000);")
                return True
            elif direction == 'down':
                self.driver.execute_script("window.scrollBy(0,1000);")
                return True
            elif direction == 'right':
                self.driver.execute_script("window.scrollBy(1000,0);")
                return True
            else:
                self.driver.execute_script("window.scrollBy(-1000,0);")
                return True
        except:
            self.log.error("Scrolling failed")
            return False

    # Method to wait for an element
    def waitforelement(self, locator):
        try:
            elementowait = None
            # wait object with certain seconds and ignoring conditions
            nwait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                  ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                      ElementNotSelectableException])
            # Wait for an element until the expected conditions are met
            elementowait = nwait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return elementowait

        except Exception as e:
            print("Element was not found, wait limit exceeded: " + str(e.args))
            return False