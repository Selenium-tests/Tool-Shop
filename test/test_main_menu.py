import pytest
import allure
from fixtures.General import driver, wait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.MainMenu import main_menu, unexpanded_dropdown_list, expanded_dropdown_list
from support.TestDataLoader import load_main_menu_testdata, load_main_menu_dropdown_list_testdata

main_menu_testdata = load_main_menu_testdata()
main_menu_dropdown_list_testdata = load_main_menu_dropdown_list_testdata()


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Main menu', 'Links')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('The main menu links')
@pytest.mark.parametrize('init_url, partial_selector, expected_url', main_menu_testdata)
def test_main_menu_links(main_menu, init_url, partial_selector, expected_url):
    main_menu.go_to_page(init_url)
    main_menu.click_link(partial_selector)
    assert main_menu.driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {main_menu.driver.current_url}"


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Main menu', 'Dropdown list', 'Expanding')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Expanding the main menu dropdown list')
def test_expanding_dropdown_list(unexpanded_dropdown_list, wait):
    unexpanded_dropdown_list.click_trigger_element('nav-categories')

    try:
        wait.until(EC.visibility_of_element_located(unexpanded_dropdown_list.dropdown_list_container_locator))
    except Exception as e:
        pytest.fail('The dropdown list is not expanded')


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Main menu', 'Dropdown list', 'Collapsing')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Collapsing the main menu dropdown list')
def test_collapsing_dropdown_list(expanded_dropdown_list, wait):
    expanded_dropdown_list.click_trigger_element('nav-categories')

    try:
        wait.until(EC.invisibility_of_element_located(expanded_dropdown_list.dropdown_list_container_locator))
    except Exception as e:
        pytest.fail('The dropdown list is not collapsed')


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Main menu', 'Dropdown list', 'Links')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('The main menu dropdown list links')
@pytest.mark.parametrize('item_partial_selector, expected_url', main_menu_dropdown_list_testdata)
def test_dropdown_list_links(expanded_dropdown_list, item_partial_selector, expected_url):
    expanded_dropdown_list.click_link(item_partial_selector)

    assert expanded_dropdown_list.driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {expanded_dropdown_list.driver.current_url}"
