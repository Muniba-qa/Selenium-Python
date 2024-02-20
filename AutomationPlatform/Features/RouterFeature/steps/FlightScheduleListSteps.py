import time

from behave import *
from NavigoPlatform.PageObjects.router.FlightScheduleListPage import FlightScheduleListPage


@then(u'Click on Tabs Flight Schedule List')
def click_on_tabs_flight_schedule_list(Context):
    Context.FlightSchedulePage = FlightScheduleListPage(Context.driver)
    Context.FlightSchedulePage.click_on_flight_schedules_tab()


@then(u'Create the New Flight Schedule')
def create_the_new_flight_schedule(Context):
    Context.FlightSchedulePage.click_on_create_new_flight_schedule_btn()
    Context.FlightSchedulePage.click_on_drop_menu_btn()
    Context.FlightSchedulePage.input_title()
    Context.FlightSchedulePage.click_on_swipe_right_btn()
    Context.FlightSchedulePage.click_on_date()
    Context.FlightSchedulePage.click_on_next_btn()
    Context.FlightSchedulePage.input_purchaser()


@then(u'Verify Flight Created or not')
def verify_flight_created(Context):
    Context.FlightSchedulePage.verify_flight_created()
