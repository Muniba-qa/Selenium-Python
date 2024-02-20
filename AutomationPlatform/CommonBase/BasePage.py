import random
import time

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, \
    NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, \
    InvalidSelectorException as EX
from NavigoPlatform.Configurations.Config import TestConfig

"""This class is the parent of all the page classes"""
"""It contains all the common action methods and utilities for all the pageObjects"""


class BasePage:

    def __init__(self, Driver):
        self.Driver = Driver

    def wait_time(self, wait_time):
        wait.WebDriverWait(self.Driver, wait_time)

    def click_on_random_location(self, By_Locator):
        Element = WebDriverWait(self.Driver, 10).until(EC.element_to_be_clickable(By_Locator))
        Element.click()
        # js_code = """
        # var mapElement = document.getElementsByTagName('canvas');
        # var clickEvent = new MouseEvent('click', {
        #     clientX: 30,  // Replace with the desired X coordinate
        #     clientY: 130   // Replace with the desired Y coordinate
        #     });
        #     mapElement[0].dispatchEvent(clickEvent);
        #     """

        # Execute the JavaScript code
        # self.driver.execute_script(js_code)

    def click_element(self, By_Locator):
        try:
            Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(By_Locator))
            self.Driver.execute_script("arguments[0].click();", Element)
        except EX as e:
            print("Exception! Can't click on the element")

    def click(self, By_Locator):
        WebDriverWait(self.Driver, 10).until(EC.element_to_be_clickable(By_Locator)).click()

    def input_element(self, By_Locator, Text):
        try:
            WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(By_Locator)).send_keys(Text)
        except EX as e:
            print("Exception! Can't click on the element")

    def get_element_text(self, By_Locator):
        Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(By_Locator))
        return Element.text

    def get_text(self, By_Locator, Text):
        Element = WebDriverWait(self.Driver, 10).until(EC.text_to_be_present_in_element(By_Locator, Text))
        return Element

    def get_title(self):
        return self.Driver.title

    def get_element_attribute(self, By_Locator, AttributeName):
        Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(By_Locator))
        return Element.get_attribute(AttributeName)

    def verify_element_displayed(self, By_Locator):
        try:
            Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(By_Locator))
            return Element.is_displayed()
        except:
            return False

    def select_from_drop_down(self, By_Locator):
        time.sleep(2)
        Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(By_Locator))
        Dropdown_Element = Element
        select = Select(Dropdown_Element)
        TestConfig.logger.info(select)
        options = select.options
        time.sleep(2)
        Selected_Option = random.choice(options)
        Selected_Choice = Selected_Option.text
        select.select_by_visible_text(Selected_Choice)
        print("Selected flight model and make: ", Selected_Choice)
        TestConfig.logger.info(Selected_Choice)
        return Selected_Choice

    def upload_file(self, By_Locator, Path_To_File):
        FileUpload = WebDriverWait(self.Driver, 10).until(EC.presence_of_element_located(By_Locator))
        FileUpload.send_keys(Path_To_File)

    def generate_random_number(self):
        # Generate a random 4-digit number
        RandomNumber = random.randint(1000, 9999)
        print(RandomNumber)
        return RandomNumber

    def get_all_elements_text(self, By_Locator):
        Elements = WebDriverWait(self.Driver, 10).until(EC.visibility_of_all_elements_located(By_Locator))
        AllElementsText = []
        for Element in Elements:
            AllElementsText.append(Element.text)
        return AllElementsText

