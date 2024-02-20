import time
from datetime import date
from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations import Config


class CreateNewFlightSchedulePage(BasePage):
    LOC_Flight_Schedule_Tab = (By.XPATH, "//div[text()='Flight Schedules']")
    LOC_Create_New_Flight_Schedule = (By.XPATH, "//span[text()='Create New Flight Schedule']")
    LOC_Air_Route_Drop_Down = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/select")
    LOC_Title = (By.ID, "title")
    LOC_Calender_Next_arrow = (By.XPATH, "//img[contains(@class,'rotate-180 h-7')]")
    LOC_Calender_Date_Btn = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div[1]/div/"
                                       "div[1]/div[2]/div/button[18]")
    LOC_Total_Value = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div/span")
    LOC_Next_Btn = (By.XPATH, "//span[text()='Next']")
    LOC_Air_Route_Name = (By.XPATH, "(//div[@class='my-4']//span)[2]")

    LOC_Purchaser_Name = (By.ID, "name")
    LOC_Addition_Name_Line = (By.ID, "name2")
    LOC_Address = (By.ID, "address")
    LOC_Apartment_number = (By.ID, "apartment_number")
    LOC_Post_Office_Box = (By.ID, "post_office_box")
    LOC_City = (By.ID, "city")
    LOC_State = (By.ID, "state")
    LOC_Postal_code = (By.ID, "postal_code")
    LOC_Cn_Drop_Down = (By.ID, "country")
    LOC_Email = (By.ID, "email")
    LOC_Phone_number = (By.ID, "phone_number")
    LOC_Complete_Purchase_btn = (By.XPATH, "//span[text()='Complete Purchase']")

    LOC_Purchase_Completed = (By.XPATH, "//span[text()='Purchase Completed']")
    LOC_Close_Btn = (By.XPATH, "//span[text()='Close']")

    Air_route_drop_down_text = "Brazil+auto123 (Brazil) - Suriname+auto789 (Suriname) [14:30 UTC to 19:30 UTC]"

    Purchase_Name = "Navigo Auto mode"
    Additional_Name_Line = "Navigo Auto test products"
    Address = "5773, old street , lavington raod"
    Apartment_Number = "555"
    Post_Office_box = "912314"
    City = "California Test"
    State = "Navigo Test State"
    Postal_code = "84739"
    Email = "test.testing@gmail.com"
    Phone_number = "+1(123)4567890"
    Str_Purchase_Completed = "Purchase Completed"
    logs = Config.get_logs()

    def click_on_flight_schedule_tab(self):
        self.click_on_element(self.LOC_Flight_Schedule_Tab)
        time.sleep(2)

    def click_on_create_new_flight_schedule_btn(self):
        self.click_on_element(self.LOC_Create_New_Flight_Schedule)
        time.sleep(8)

    def click_on_air_route_drop_down(self):
        # self.select_drop_down_by_visible_text(self.LOC_Air_Route_Drop_Down,
        #                                       CreateNewFlightSchedulePage.Air_route_drop_down_text)
        air_route = self.select_from_drop_down(self.LOC_Air_Route_Drop_Down)

    def add_title_for_the_air_route(self):
        cur_time = date.today()
        self.input_element(self.LOC_Title, f'Test Auto mode flight schedule {cur_time}')

    def click_on_calendar_nxt_arrow(self):
        self.click_on_element(self.LOC_Calender_Next_arrow)
        time.sleep(2)
        self.click_on_element(self.LOC_Calender_Next_arrow)
        time.sleep(1)

    def click_on_calendar_date(self):
        self.click_on_element(self.LOC_Calender_Date_Btn)
        time.sleep(2)

    def check_for_total_value(self):
        if self.is_element_displayed(self.LOC_Total_Value):
            total_value = self.get_element_by_text(self.LOC_Total_Value)
            CreateNewFlightSchedulePage.logs.info(total_value)
        else:
            self.take_screenshot()

    def click_on_next(self):
        self.click_on_element(self.LOC_Next_Btn)
        time.sleep(2)
        if self.is_element_displayed(self.LOC_Air_Route_Name):
            assert True
        else:
            self.take_screenshot()
            assert False

    def enter_purchaser_details(self):
        self.input_element(self.LOC_Purchaser_Name, CreateNewFlightSchedulePage.Purchase_Name)
        self.input_element(self.LOC_Addition_Name_Line, CreateNewFlightSchedulePage.Additional_Name_Line)
        self.input_element(self.LOC_Address, CreateNewFlightSchedulePage.Address)
        self.input_element(self.LOC_Apartment_number, CreateNewFlightSchedulePage.Apartment_Number)
        self.input_element(self.LOC_Post_Office_Box, CreateNewFlightSchedulePage.Post_Office_box)
        self.input_element(self.LOC_City, CreateNewFlightSchedulePage.City)
        self.input_element(self.LOC_State, CreateNewFlightSchedulePage.State)
        self.input_element(self.LOC_Postal_code, CreateNewFlightSchedulePage.Postal_code)
        time.sleep(2)
        cn_selected = self.select_from_drop_down(self.LOC_Cn_Drop_Down)
        self.input_element(self.LOC_Email, CreateNewFlightSchedulePage.Email)
        self.input_element(self.LOC_Phone_number, CreateNewFlightSchedulePage.Phone_number)

    def click_on_complete_purchase(self):
        self.click_on_element(self.LOC_Complete_Purchase_btn)

    def check_for_confirmation(self):
        if self.is_text_present(self.LOC_Purchase_Completed, CreateNewFlightSchedulePage.Str_Purchase_Completed):
            assert True
        else:
            self.take_screenshot()
            assert False, f'{CreateNewFlightSchedulePage.Str_Purchase_Completed} is not present'

    def close_conformation_dialog(self):
        self.click_on_element(self.LOC_Close_Btn)
