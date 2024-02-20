from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    TXT_Router_Dashboard = (By.XPATH, "//*[@id='root']/div[1]/div[1]/div[2]/div[1]/button/span/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_router_page_loaded(self):
        print("hi there", self.get_element_text(self.TXT_Router_Dashboard) == "Router")
        assert self.get_element_text(self.TXT_Router_Dashboard) == "Router"
