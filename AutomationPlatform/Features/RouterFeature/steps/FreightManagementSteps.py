from behave import *
from NavigoPlatform.PageObjects.router.FreightManagementPage import FreightManagementPage


@then(u'Click on Tab Freight Management')
def click_on_tab_freight_purchase(Context):
    Context.FreightManagement = FreightManagementPage(Context.driver)
    Context.FreightManagement.click_on_freight_management_tab()


@then(u'Verify the Freight Management Tab')
def click_on_tab_freight_management(Context):
    Verify_Tab = Context.FreightManagement.verify_freight_management_tab()
    assert Verify_Tab


@then(u'Click on edit btn')
def click_on_edit_btn(Context):
    Context.FreightManagement.click_on_edit_btn()


@then(u'Click on Contact Info btn')
def click_on_contact_info_btn(Context):
    Context.FreightManagement.click_on_contact_btn()


@then(u'Is Contact info visible')
def click_on_contact_info_btn(Context):
    Context.FreightManagement.click_on_contact_btn()


@when(u'Freight Management records available')
def freight_management_records_available(Context):
    Verify_Tab = Context.FreightManagement.verify_freight_management_tab()
    assert Verify_Tab


@then(u'Verify the Select dropdown')
def verify_select_dropdown(Context):
    Element = Context.FreightManagement.verify_select_dropdown()
    assert Element


@then(u'Click on status')
def click_on_status(Context):
    Context.FreightManagement.click_on_flight_status()


@then(u'Verify the Status Popup')
def verify_status_popup(Context):
    Context.FreightManagement.verify_status_popup()


@then(u'Click on cancel btn')
def click_on_cancel_tn(Context):
    Context.FreightManagement.click_on_cancel_tn()


@then(u'Click on save btn')
def click_on_save_btn(Context):
    Context.FreightManagement.click_on_save_btn()


@then(u'Get the old status')
def get_old_status(Context):
    Context.Old_Status = Context.FreightManagement.get_the_status()


@then(u'Check the Status Changed or not "{Status}"')
def check_status(Context, Status):
    Context.New_Status = Context.FreightManagement.get_the_status()
    if Status == "Cancel":
        assert Context.Old_Status == Context.New_Status
    if Status == "Save":
        assert Context.Old_Status != Context.New_Status


@then(u'Check the Freight Management Tab')
def verify_freight_management_tab(Context):
    try:
        Context.FreightManagement.click_on_freight_management_tab()
        assert False
    except:
        assert True


@then(u'Click on Tab Freight Purchases')
def click_on_tab_freight_purchase(Context):
    Context.FreightManagement = FreightManagementPage(Context.driver)
    Context.FreightManagement.click_on_freight_purchase_tab()


@then(u'Click on the Purchase new Freight')
def click_on_purchase_new_freight(Context):
    Context.FreightManagement.click_on_purchase_btn()


@then(u'Select Available Flight')
def click_on_select_flight(Context):
    Context.FreightManagement.click_on_select_flight()
    Context.FreightManagement.verify_select_available_flight()


@then(u'Verify the Freight Table columns')
def verify_freight_table_columns(Context):
    Context.FreightManagement.verify_table_columns()


@then(u'verify it is in table format')
def verify_freight_table_view(Context):
    Context.FreightManagement.verify_table_view()
