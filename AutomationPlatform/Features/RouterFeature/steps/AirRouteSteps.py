from behave import *
from NavigoPlatform.PageObjects.router.LoginPage import LoginPage
from NavigoPlatform.PageObjects.router.AirRoutesPage import AirRoutesPage


@then(u'Click on Create New Route button')
def click_on_create_new_btn(Context):
    try:
        Context.loginPage = LoginPage(Context.driver)
        Context.airRoutePage = AirRoutesPage(Context.driver)
        Context.airRoutePage.click_on_create_new_route_btn()
    except:
        assert False, "Not able to click on Create New button"


@then(u'Enter all the details of Origin Airport')
def origin_airport_details(Context):
    Context.airRoutePage.fill_all_origin_details()


@then(u'Enter all the details of Destination Airport')
def destination_airport_details(Context):
    Context.airRoutePage.fill_all_destination_details()
    Context.airRoutePage.enter_price_details()
    Context.airRoutePage.click_on_create_air_route_btn()
