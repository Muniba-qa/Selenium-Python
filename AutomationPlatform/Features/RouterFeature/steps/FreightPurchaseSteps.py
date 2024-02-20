from behave import *
from NavigoPlatform.PageObjects.router.FreightPurchasePage import FreightPurchasePage


@when(u'Click on Tab Freight Purchase')
def click_on_tab_freight_purchase(Context):
    Context.FreightPurchase = FreightPurchasePage(Context.driver)
    Context.FreightPurchase.click_on_freight_purchase_tab()


@then(u'Create record if it is not available')
def create_record_if_not_available(Context):
    Context.Record = Context.FreightPurchase.check_records()
    if not Context.Record:
        Context.FreightPurchase.purchase_new_freight_btn()
        Context.FreightPurchase.create_new_freight_purchase()


@then(u'Verify the Flights are available')
def check_the_flights(Context):
    Context.FreightPurchase.check_flights()
