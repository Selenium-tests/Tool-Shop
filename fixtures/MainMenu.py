import pytest
from fixtures.General import driver
from pageobject.MainMenu import MainMenu
from pageobject.DropdownList import DropdownList
from support.URL import URL


@pytest.fixture
def main_menu(driver):
    menu = MainMenu(driver)
    return menu


@pytest.fixture
def unexpanded_dropdown_list(driver):
    driver.get(URL.HOME_PAGE)
    dropdown_list = DropdownList(driver)
    return dropdown_list


@pytest.fixture
def expanded_dropdown_list(driver):
    driver.get(URL.HOME_PAGE)
    dropdown_list = DropdownList(driver)
    dropdown_list.click_trigger_element('nav-categories')
    return dropdown_list
