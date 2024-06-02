import pytest
from fixtures.General import driver
from pageobject.MainMenu import MainMenu
from pageobject.MainMenuDropdownList import MainMenuDropdownList
from support.URL import URL


@pytest.fixture
def main_menu(driver):
    menu = MainMenu(driver)
    return menu


@pytest.fixture
def unexpanded_dropdown_list(driver):
    driver.get(URL.HOME_PAGE)
    dropdown_list = MainMenuDropdownList(driver)
    return dropdown_list


@pytest.fixture
def expanded_dropdown_list(driver):
    driver.get(URL.HOME_PAGE)
    dropdown_list = MainMenuDropdownList(driver)
    dropdown_list.click_trigger_element()
    return dropdown_list
