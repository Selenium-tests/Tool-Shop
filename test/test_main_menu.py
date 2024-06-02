import pytest
from fixtures.General import driver, wait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.MainMenu import main_menu, unexpanded_dropdown_list, expanded_dropdown_list
from support.TestDataLoader import load_main_menu_testdata, load_main_menu_dropdown_list_testdata

main_menu_testdata = load_main_menu_testdata()
main_menu_dropdown_list_testdata = load_main_menu_dropdown_list_testdata()


@pytest.mark.parametrize('init_url, partial_selector, expected_url', main_menu_testdata)
def test_main_menu_links(main_menu, init_url, partial_selector, expected_url):
    main_menu.go_to_page(init_url)
    main_menu.click_link(partial_selector)
    assert main_menu.driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {main_menu.driver.current_url}"


def test_expanding_dropdown_list(unexpanded_dropdown_list, wait):
    unexpanded_dropdown_list.click_trigger_element()

    try:
        wait.until(EC.visibility_of_element_located(unexpanded_dropdown_list.dropdown_list_container_locator))
    except Exception as e:
        pytest.fail('The dropdown list is not expanded')


def test_collapsing_dropdown_list(expanded_dropdown_list, wait):
    expanded_dropdown_list.click_trigger_element()

    try:
        wait.until(EC.invisibility_of_element_located(expanded_dropdown_list.dropdown_list_container_locator))
    except Exception as e:
        pytest.fail('The dropdown list is not collapsed')


@pytest.mark.parametrize('partial_selector, expected_url', main_menu_dropdown_list_testdata)
def test_dropdown_list_links(expanded_dropdown_list, partial_selector, expected_url):
    expanded_dropdown_list.click_link(partial_selector)

    assert expanded_dropdown_list.driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {expanded_dropdown_list.driver.current_url}"
