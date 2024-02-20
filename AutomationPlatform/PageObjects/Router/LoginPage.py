from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig


class LoginPage(BasePage):
    LOC_Txt_Username = (By.ID, "username")
    LOC_Txt_Password = (By.ID, "password")
    LOC_Btn_Login = (By.ID, "kc-login")
    LOC_Msg_Invalid_Creds = (By.CLASS_NAME, "kc-feedback-text")
    User = TestConfig.USERNAME
    Pwd = TestConfig.PASSWORD

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self):
        self.input_element(self.LOC_Txt_Username, LoginPage.User)
        self.input_element(self.LOC_Txt_Password, LoginPage.Pwd)

    def enter_username(self, User):
        self.input_element(self.LOC_Txt_Username, User)

    def enter_password(self, Pwd):
        self.input_element(self.LOC_Txt_Password, Pwd)

    def enter_login(self):
        self.click_element(self.LOC_Btn_Login)

    def validate_title(self):
        assert self.get_title() == "Navigo Platform"

    def validate_invalid_creds(self):
        assert self.get_element_text(self.LOC_Msg_Invalid_Creds) == "Invalid username or password."

    def validate_empty_username(self):
        assert self.get_element_text(self.LOC_Msg_Invalid_Creds) == "Invalid username or password."

    def validate_empty_password(self):
        assert self.get_element_text(self.LOC_Msg_Invalid_Creds) == "Invalid username or password."

