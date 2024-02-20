import os

from behave import *
from NavigoPlatform.Configurations import Config
from NavigoPlatform.PageObjects.router.LoginPage import LoginPage
from NavigoPlatform.PageObjects.router.DashboardPage import DashboardPage


@given(u'Launch the browser')
def launch_browser(context):
    # Config.HeadlessChromeBrowser(context)
    # Config.ChromeBrowser(context)
    # this is the logoic to access whether we want to execute chrome with non-headless or headless by running first
    # By Default it runs in headless and running export HEADLESS=false before behave cmd will run in non-headless mode
    headless_mode = os.environ.get("HEADLESS", "false").lower() == "true"
    Config.chrome_with_param_browser(context, headless_mode)


@when(u'Open the router app https://qa2-platform.navigo.global/apps/router/')
def open_login_page(context):
    context.loginPage = LoginPage(context.driver)


@then(u'The login portal has been opened')
def validate_login_page(Context):
    try:
        Context.loginPage.validate_title()
    except:
        assert False, "Test is failed in validate login page title"


@then(u'Provide valid username and password')
def enter_login_creds(Context):
    Context.loginPage.enter_login_credentials()


@then(u'Provide the Credentials "{User}" and "{Pwd}"')
def enter_login_creds_user_permissions(Context, User, Pwd):
    try:
        Context.loginPage.enter_username(User)
        Context.loginPage.enter_password(Pwd)
    except:
        assert False, "Test is failed in validating invalid login"


@then(u'Click on the Login button')
def enter_login(Context):
    try:
        Context.loginPage.enter_login()
    except:
        assert False, "Test is failed in enter login"


@then(u'Login is successful and dashboard is opened')
def validate_dashboard_page(context):
    context.DashboardPage = DashboardPage(context.driver)
    context.DashboardPage.validate_router_page_loaded()


@then(u'Provide the username "{User}" and password "{Pwd}"')
def validate_multiple_login_creds(Context, User, Pwd):
    try:
        Context.loginPage.enter_username(User)
        Context.loginPage.enter_password(Pwd)
    except:
        assert False, "Test is failed in validating invalid login"


@then(u'Login is failed and invalid credential error is displayed')
def validate_invalid_login(Context):
    try:
        Context.loginPage.validate_invalid_creds()
    except:
        assert False, "Test is failed in validating invalid login"


@then(u'Provide the password "{Pwd}"')
def enter_login_creds(Context, Pwd):
    try:
        Context.loginPage.enter_password(Pwd)
    except:
        assert False, "Test is failed in enter password"



@then(u'Provide the username "{User}"')
def enter_login_creds(Context, User):
    try:
        Context.loginPage.enter_username(User)
    except:
        Context.driver.close()
        assert False, "Test is failed in enter username"


@then(u'Login is failed and empty username error is displayed')
def validate_empty_username(context):
    try:
        context.loginPage.validate_empty_username()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty username"


@then(u'Login is failed and empty password error is displayed')
def validate_empty_passeword(context):
    try:
        context.loginPage.validate_empty_password()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty password"


@then(u'Close the browser')
def step_impl(Context):
    Context.driver.close()
