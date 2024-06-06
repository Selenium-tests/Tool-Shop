import pytest
from fixtures.General import driver
from pageobject.DropdownList import DropdownList
from pageobject.AccountMenu import AccountMenu
from support.Authentication import authentication


@pytest.fixture
def unexpanded_account_dropdown_list(driver):
    authentication(driver)
    dropdown_list = DropdownList(driver)
    return dropdown_list


@pytest.fixture
def expanded_account_dropdown_list(driver):
    authentication(driver)
    dropdown_list = DropdownList(driver)
    dropdown_list.click_trigger_element('nav-menu')
    return dropdown_list


@pytest.fixture
def account_menu(driver):
    authentication(driver)
    menu = AccountMenu(driver)
    return menu
