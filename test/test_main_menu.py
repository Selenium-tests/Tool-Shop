import pytest
from selenium import webdriver
from pageobject.MainMenu import MainMenu


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize("init_url, partial_selector, expected_url", [
    ('https://practicesoftwaretesting.com/#/contact', 'nav-home', 'https://practicesoftwaretesting.com/#/'),
    ('https://practicesoftwaretesting.com/#/', 'nav-contact', 'https://practicesoftwaretesting.com/#/contact'),
    ('https://practicesoftwaretesting.com/#/', 'nav-sign-in', 'https://practicesoftwaretesting.com/#/auth/login')
])
def test_links(browser, init_url, partial_selector, expected_url):
    main_menu = MainMenu(browser)
    browser.get(init_url)
    main_menu.click_link(partial_selector)
    assert browser.current_url == expected_url, f"Expected URL to be {expected_url}, but got {browser.current_url}"

