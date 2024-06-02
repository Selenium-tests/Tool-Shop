import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    web_driver = webdriver.Chrome()
    yield web_driver
    web_driver.quit()


@pytest.fixture
def wait(driver):
    web_driver_wait = WebDriverWait(driver, 10)
    return web_driver_wait
