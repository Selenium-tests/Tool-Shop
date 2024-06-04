import pytest
import allure
from fixtures.General import driver, wait
from fixtures.Account import unexpanded_account_dropdown_list, expanded_account_dropdown_list
from selenium.webdriver.support import expected_conditions as EC


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Account', 'Dropdown list', 'Expanding')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Expanding the account dropdown list')
def test_expanding_dropdown_list(driver, wait, unexpanded_account_dropdown_list):
    unexpanded_account_dropdown_list.click_trigger_element('nav-menu')

    try:
        wait.until(EC.visibility_of_element_located(unexpanded_account_dropdown_list.dropdown_list_container_locator))
    except Exception as e:
        pytest.fail('The dropdown list is not expanded')


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Account', 'Dropdown list', 'Collapsing')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Collapsing the main menu dropdown list')
def test_collapsing_dropdown_list(driver, wait, expanded_account_dropdown_list):
    expanded_account_dropdown_list.click_trigger_element('nav-menu')

    try:
        wait.until(EC.invisibility_of_element_located(expanded_account_dropdown_list.dropdown_list_container_locator))
    except Exception as e:
        pytest.fail('The dropdown list is not expanded')
