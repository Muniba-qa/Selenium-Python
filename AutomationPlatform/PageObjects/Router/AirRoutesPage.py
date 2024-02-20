import time
from selenium.webdriver.common.by import By
from NavigoPlatform.CommonBase.BasePage import BasePage


class AirRoutesPage(BasePage):
    LOC_Create_New_Route_Btn = (By.XPATH, "//span[text()='Create New Route']")
    LOC_Origin_CN_Drop_Down = (By.XPATH, "(//select[contains(@class,'text-sm w-full')])[1]")
    LOC_Origin_Airport_Name = (By.ID, "origin_airport_name")
    LOC_Origin_Airport_Code = (By.ID, "origin_airport_code")
    LOC_Origin_Airport_Map_Point = (By.XPATH, "//*[@id='DestinationFormMap']/div[2]/canvas[1]")
    LOC_Origin_Airport_Coordinates = (By.ID, "origin_airport_coorinates")
    LOC_Origin_Airport_Start_Time = (By.ID, "origin_time")
    LOC_Start_Time_Zone = (By.XPATH, "//div[contains(@class,'px-2 py-[6px]')]//select)[2]")
    LOC_Start_Next_Btn = (By.XPATH, "//span[text()='Next']")

    LOC_Dest_Cn_DropDown = (
        By.XPATH, "//*[@id='navigo.modal']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/select[1]")
    LOC_Dest_Airport_Name = (By.ID, "destination_airport_name")
    LOC_Dest_Airport_Code = (By.ID, "destination_airport_code")
    LOC_Dest_Airport_Coordinates = (By.ID, "destination_airport_coorinates")
    LOC_Dest_Airport_End_Time = (By.ID, "destination_time")
    LOC_Dest_End_Time_Zone = (
        By.XPATH, "//*[@id='navigo.modal']/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/select[1]")
    LOC_Dest_Next_Btn = (By.XPATH, "//span[text()='Next']")

    LOC_Price_Text = (By.ID, "cost")
    LOC_Create_Air_Route_Btn = (By.XPATH, "//*[@id='navigo.modal']/div/div[2]/div/div[3]/button[2]/span")

    LOC_Verify_Route = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[8]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_create_new_route_btn(self):
        self.click_element(self.LOC_Create_New_Route_Btn)

    def fill_all_origin_details(self):
        origin_cn_name = self.select_from_drop_down(self.LOC_Origin_CN_Drop_Down)
        self.input_element(self.LOC_Origin_Airport_Name, f'{origin_cn_name}+automation')
        self.input_element(self.LOC_Origin_Airport_Code, f'{origin_cn_name}+auto123')
        time.sleep(5)
        self.click_on_random_location(self.LOC_Origin_Airport_Map_Point)
        self.input_element(self.LOC_Origin_Airport_Start_Time, "14:30 PM")
        self.click_element(self.LOC_Start_Next_Btn)

    def fill_all_destination_details(self):
        dest_cn_name = self.select_from_drop_down(self.LOC_Dest_Cn_DropDown)
        self.input_element(self.LOC_Dest_Airport_Name, f'{dest_cn_name}+automation')
        self.input_element(self.LOC_Dest_Airport_Code, f'{dest_cn_name}+auto789')
        time.sleep(5)
        self.click_on_random_location(self.LOC_Origin_Airport_Map_Point)
        self.input_element(self.LOC_Dest_Airport_End_Time, "19:30 PM")
        self.click_element(self.LOC_Dest_Next_Btn)

    def enter_price_details(self):
        time.sleep(5)
        self.input_element(self.LOC_Price_Text, "2222")

    def click_on_create_air_route_btn(self):
        self.click_element(self.LOC_Create_Air_Route_Btn)
