import pytest
from selenium.webdriver.support.wait import WebDriverWait
from config.Driver import Provider
from support.DriverType import DriverType


@pytest.fixture(scope='function')
def driver():
    webdriver = Provider.get_driver(DriverType.CHROME)
    yield webdriver
    webdriver.quit()


@pytest.fixture
def wait(driver):
    web_driver_wait = WebDriverWait(driver, 10)
    return web_driver_wait
