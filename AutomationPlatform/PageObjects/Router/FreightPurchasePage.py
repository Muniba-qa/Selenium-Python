import time

from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By


class FreightPurchasePage(BasePage):
    LOC_Freight_Purchase_Tab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[4]")
    LOC_Freight_Purchase_Records = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/td')
    LOC_Purchase_New_Freight_Btn = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div/button')
    LOC_Select_Available_Flight = (By.XPATH, '//*[@id="flight"]')
    LOC_Available_Flights = (By.XPATH, '//*[@id="flight"]/option[2]')
    LOC_All_Dates = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/button')
    LOC_Swipe_Right = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[2]/div/div/div/button[3]')
    LOC_Select_Date = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/button[31]')
    LOC_Next_Btn = (By.XPATH, '//*[@id="navigo.modal"]/div/div[2]/div/div[3]/button[2]')
    LOC_Select_Measurement = (By.XPATH, '//*[@id="measurement"]')
    LOC_Select_Shipment_Type = (By.XPATH, '//*[@id="shipmentType"]')
    LOC_Description = (By.XPATH, '//*[@id="description"]')
    LOC_Weight = (By.XPATH, '//*[@id="weight_gr"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_freight_purchase_tab(self):
        self.click_element(self.LOC_Freight_Purchase_Tab)

    def check_records(self):
        return self.verify_element_displayed(self.LOC_Freight_Purchase_Records)

    def purchase_new_freight_btn(self):
        self.click_element(self.LOC_Purchase_New_Freight_Btn)

    def create_new_freight_purchase(self):
        self.select_from_drop_down(self.LOC_Select_Available_Flight)
        self.click_element(self.LOC_Swipe_Right)
        self.click(self.LOC_Select_Date)
        self.click(self.LOC_Next_Btn)
        self.select_from_drop_down(self.LOC_Select_Measurement)
        self.input_element(self.LOC_Description, "Laptop Temp")
        self.input_element(self.LOC_Weight, "5")
        self.click(self.LOC_Next_Btn)

    def check_flights(self):
        return self.verify_element_displayed(self.LOC_Available_Flights)








