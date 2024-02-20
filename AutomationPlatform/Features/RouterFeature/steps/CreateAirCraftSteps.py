import time

from behave import *
from NavigoPlatform.PageObjects.router.CreateAircraftPage import CreateAirCraftPage


@then(u'Click on Tabs Aircraft and Available Aircraft')
def click_on_tab_aircraft_and_available_aircraft(Context):
    Context.airCraftPage = CreateAirCraftPage(Context.driver)
    Context.airCraftPage.click_on_aircraft_tab()
    Context.airCraftPage.click_on_available_aircraft_tab()


@then(u'Click on Create New Aircraft Btn')
def click_on_create_new_aircraft_btn(Context):
    Context.airCraftPage.click_on_create_new_aircraft_btn()


@then(u'Enter all Aircraft Details')
def fill_aircraft_data(Context):
    Context.airCraftPage.fill_aircraft_details()


@then(u'Upload Seat Schematics file')
def upload_seat_schematics_file(Context):
    Context.airCraftPage.upload_seat_schematics()


@then(u'Goto Seat Availability Tab and upload Seat which is less than total number of available Seats')
def upload_seats_file(Context):
    Context.airCraftPage.upload_seats()


@then(u'Save Aircraft')
def save_aircraft_btn(Context):
    time.sleep(3)
    Context.airCraftPage.click_on_save_aircraft()


@then(u'Verify its been Create or not')
def verify_created_aircraft(Context):
    Context.airCraftPage.verify_created_aircraft()

