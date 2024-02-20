import os
import time

from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By


class CreateAirCraftPage(BasePage):
    # AirCraft Details section
    LOC_Aircraft_Tab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[3]")
    LOC_Available_Aircraft_Tab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]")
    LOC_Create_New_Aircraft_Btn = (
        By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button")
    LOC_Aircraft_Make = (By.ID, "make")
    LOC_Aircraft_Model = (By.ID, "model")
    LOC_Aircraft_Title = (By.ID, "title")
    LOC_Aircraft_Tail = (By.ID, "tail_number")
    LOC_Aircraft_Weight = (By.ID, "weight")
    LOC_Aircraft_Length = (By.ID, "length")
    LOC_Aircraft_Seats_Total = (By.ID, "seats_total")
    LOC_Aircraft_Number_Of_Engines = (By.ID, "number_of_engines")
    LOC_Aircraft_Engine_Type = (By.ID, "engine_type")
    LOC_Aircraft_Max_Speed = (By.ID, "max_speed")
    LOC_Aircraft_Max_Payload = (By.ID, "maximum_payload")
    LOC_Air_Schematics_Browse_Files = (By.ID, "file-input")

    # Seat Availability Section
    LOC_Seat_Availabilty_Tab = (By.XPATH, "//*[@id='navigo.modal']/div/div[2]/div/div[1]/div[2]")
    LOC_Browse_Seat_Selection = (By.ID, "file-input")
    LOC_Save_Aircraft_Btn = (By.XPATH, "//*[@id='navigo.modal']/div/div[3]/div[2]/button/span")
    LOC_Verify_Aircraft_Name = (By.XPATH,
                             "//*[@id='root']/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[1]/span")
    # LOC_Verify_Aircraft_Name = (By.XPATH, "(//td[contains(@class,'px-3 py-3')]//span)[1]")
    # LOC_Verify_Aircraft_Name = (By.XPATH, "(//span[contains(@class,'text-font font-roboto')])[2]")

    # Freight Section
    LOC_Freight_Tab = (By.XPATH, "//div[text()='Freight']")
    LOC_Freight_Space_Availability = (By.ID, "hasFreight")
    LOC_Total_MaxAircraft_Space = (By.ID, "weight_capacity_gr")
    LOC_MainDeck_Toggle = (By.XPATH, "(//input[@id='main'])[1]")
    LOC_Overhead_BinTotal = (By.ID, "bin_total")
    LOC_MainDeck_Maximum_Payload = (By.ID, "bin_max_payload")
    # Lower Deck Forward
    LOC_Lower_Deck_Forward_Toggle = (By.XPATH, "(//input[@id='fordward'])[1]")
    LOC_LowerDeck_Forward_Height = (By.ID, "lower_deck_fordward_height")
    LOC_LowerDeck_Forward_Width = (By.ID, "lower_deck_fordward_width")
    LOC_LowerDeck_Forward_Depth = (By.ID, "lower_deck_fordward_depth")
    LOC_LowerDeck_Forward_Door_Height = (By.ID, "lower_deck_fordward_door_height")
    LOC_LowerDeck_Forward_Door_Width = (By.ID, "lower_deck_fordward_door_width")
    LOC_LowerDeck_Forward_Max_Payload = (By.ID, "lower_deck_fordward_max_payload")
    # Lower Deck Aft
    LOC_LowerDeck_Aft_Toggle = (By.XPATH, "(//input[@id='aft'])[1]")
    LOC_LowerDeck_Aft_Height = (By.ID, "lower_deck_aft_height")
    LOC_LowerDeck_Aft_Width = (By.ID, "lower_deck_aft_width")
    LOC_LowerDeck_Aft_Depth = (By.ID, "lower_deck_aft_depth")
    LOC_LowerDeck_Aft_Door_Height = (By.ID, "lower_deck_aft_door_height")
    LOC_LowerDeck_Aft_Door_Width = (By.ID, "lower_deck_aft_door_width")
    LOC_LowerDeck_Aft_Max_Payload = (By.ID, "lower_deck_aft_max_payload")

    LOC_Save_Aircraft_Btn_With_Freight = (By.XPATH, "//span[text()='Save Aircraft']")

    Aircraft_title_name = " "

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_aircraft_tab(self):
        self.click_element(self.LOC_Aircraft_Tab)

    def click_on_available_aircraft_tab(self):
        self.click_element(self.LOC_Available_Aircraft_Tab)

    def click_on_create_new_aircraft_btn(self):
        self.click_element(self.LOC_Create_New_Aircraft_Btn)

    def fill_aircraft_details(self):
        selected_aircraft_make = self.select_from_drop_down(self.LOC_Aircraft_Make)
        selected_aircraft_model = self.select_from_drop_down(self.LOC_Aircraft_Model)
        CreateAirCraftPage.Aircraft_title_name = f'{selected_aircraft_make}+{selected_aircraft_model}+automode'
        self.input_element(self.LOC_Aircraft_Title, f'{CreateAirCraftPage.Aircraft_title_name}')
        tail_number = self.generate_random_number()
        self.input_element(self.LOC_Aircraft_Tail, tail_number)
        self.input_element(self.LOC_Aircraft_Weight, "88888")
        self.input_element(self.LOC_Aircraft_Length, "66666")
        self.input_element(self.LOC_Aircraft_Seats_Total, "450")
        self.input_element(self.LOC_Aircraft_Number_Of_Engines, "4")
        self.input_element(self.LOC_Aircraft_Engine_Type, "automode dual type")
        self.input_element(self.LOC_Aircraft_Max_Speed, "555")
        # self.input_element(self.LOC_Aircraft_Max_Payload, "999999")

    def upload_seat_schematics(self):
        path_to_schematics_file = os.path.join(os.path.abspath('NavigoPlatform/TestData/Seat_schematics.png'))
        self.upload_file(self.LOC_Air_Schematics_Browse_Files, path_to_schematics_file)

    def upload_seats(self):
        path_to_seats_file = os.path.join(os.path.abspath('NavigoPlatform/TestData/75_seats.txt'))
        self.click_element(self.LOC_Seat_Availabilty_Tab)
        self.upload_file(self.LOC_Browse_Seat_Selection, path_to_seats_file)

    def click_on_save_aircraft(self):
        self.click_element(self.LOC_Save_Aircraft_Btn)

    def verify_created_aircraft(self):
        if self.get_text(self.LOC_Verify_Aircraft_Name, CreateAirCraftPage.Aircraft_title_name):
            expected_aircraft_name = self.get_element_text(self.LOC_Verify_Aircraft_Name)
            assert expected_aircraft_name == CreateAirCraftPage.Aircraft_title_name
        else:
            assert False, f'Created {CreateAirCraftPage.Aircraft_title_name} is not present'

    def click_on_freight_tab(self):
        self.click_element(self.LOC_Freight_Tab)

    def select_freight_space_available(self):
        self.select_space_from_drop_down(self.LOC_Freight_Space_Availability, "yes")

    def add_max_payload_cap(self):
        self.input_element(self.LOC_Total_MaxAircraft_Space, "999999")

    def enable_main_deck_toggle(self):
        self.click_element(self.LOC_MainDeck_Toggle)
        time.sleep(1)

    def add_overhead_bin_box_dimensions(self):
        self.input_element(self.LOC_Overhead_BinTotal, "888888")
        self.input_element(self.LOC_MainDeck_Maximum_Payload, '999999')

    def enable_lower_deck_forward_toggle(self):
        self.click_element(self.LOC_Lower_Deck_Forward_Toggle)
        time.sleep(1)

    def add_lower_deck_forward_details(self):
        self.input_element(self.LOC_LowerDeck_Forward_Height, "500")
        self.input_element(self.LOC_LowerDeck_Forward_Width, "500")
        self.input_element(self.LOC_LowerDeck_Forward_Depth, "500")
        self.input_element(self.LOC_LowerDeck_Forward_Door_Height, "800")
        self.input_element(self.LOC_LowerDeck_Forward_Door_Width, "600")
        self.input_element(self.LOC_LowerDeck_Forward_Max_Payload, "9999")

    def enable_lower_deck_aft_toggle(self):
        self.click_element(self.LOC_LowerDeck_Aft_Toggle)
        time.sleep(1)

    def add_lower_deck_aft_details(self):
        self.input_element(self.LOC_LowerDeck_Aft_Height, "400")
        self.input_element(self.LOC_LowerDeck_Aft_Width, "400")
        self.input_element(self.LOC_LowerDeck_Aft_Depth, "400")
        self.input_element(self.LOC_LowerDeck_Aft_Door_Height, "700")
        self.input_element(self.LOC_LowerDeck_Aft_Door_Width, "500")
        self.input_element(self.LOC_LowerDeck_Aft_Max_Payload, "9999")

    def save_aircraft_freight(self):
        self.click_element(self.LOC_Save_Aircraft_Btn_With_Freight)
