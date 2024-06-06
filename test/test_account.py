import pytest
import allure
from fixtures.General import driver, wait
from fixtures.Account import unexpanded_account_dropdown_list, expanded_account_dropdown_list, account_menu
from selenium.webdriver.support import expected_conditions as EC
from support.TestDataLoader import load_dropdown_list_testdata
from support.JSONKeys import JSONKeys

account_dropdown_list_testdata = load_dropdown_list_testdata(JSONKeys.ACCOUNT_DROPDOWN_LIST)
account_menu_testdata = load_dropdown_list_testdata(JSONKeys.ACCOUNT_MENU)


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Account', 'Dropdown list', 'Expanding')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Expanding the account dropdown list')
def test_expanding_dropdown_list(wait, unexpanded_account_dropdown_list):
    unexpanded_account_dropdown_list.click_trigger_element('nav-menu')

    try:
        wait.until(EC.visibility_of_element_located(unexpanded_account_dropdown_list.dropdown_list_container_locator))
    except Exception as e:
        pytest.fail('The dropdown list is not expanded')


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Account', 'Dropdown list', 'Collapsing')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Collapsing the account dropdown list')
def test_collapsing_dropdown_list(wait, expanded_account_dropdown_list):
    expanded_account_dropdown_list.click_trigger_element('nav-menu')

    try:
        wait.until(EC.invisibility_of_element_located(expanded_account_dropdown_list.dropdown_list_container_locator))
    except Exception as e:
        pytest.fail('The dropdown list is not expanded')


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Account', 'Dropdown list', 'Links')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('The account dropdown list links')
@pytest.mark.parametrize('item_partial_selector, expected_url', account_dropdown_list_testdata)
def test_account_dropdown_list_links(expanded_account_dropdown_list, item_partial_selector, expected_url):
    expanded_account_dropdown_list.click_link(item_partial_selector)
    assert expanded_account_dropdown_list.driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {expanded_account_dropdown_list.driver.current_url}"


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Account', 'Menu', 'Links')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('The account menu links')
@pytest.mark.parametrize('item_partial_selector, expected_url', account_menu_testdata)
def test_account_menu_links(account_menu, item_partial_selector, expected_url):
    account_menu.click_link(item_partial_selector)
    assert account_menu.driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {account_menu.driver.current_url}"
