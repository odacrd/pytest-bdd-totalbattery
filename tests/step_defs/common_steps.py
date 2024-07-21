from pytest_bdd import scenario, given, when, then
from tests.pages.home_page import HomePage
import pytest
import time

@pytest.fixture()
def xdriver(driver):
    return driver

@pytest.fixture()
def context():
    return {}


@given("the user has navigated to the Total Battery Home page")
def step_function(xdriver, context):
    xdriver.get("https://totalbattery.com/")
    home_page = HomePage(xdriver)
    time.sleep(5)
    assert home_page.home_tab_text == "Home"
    assert home_page.applications_tab_text == "Applications"
    context['home_page'] = home_page