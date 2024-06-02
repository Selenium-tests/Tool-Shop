from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from support.DriverType import DriverType


class Driver:
    @abstractmethod
    def _set_capabilities(self):
        pass

    @abstractmethod
    def create_driver(self):
        pass


class ChromeDriver(Driver, ABC):

    def _set_capabilities(self):
        options = ChromeOptions()
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}
        options.set_capability('goog:chromeOptions', capabilities)
        return options

    def create_driver(self):
        return webdriver.Chrome(self._set_capabilities())


class FirefoxDriver(Driver, ABC):

    def _set_capabilities(self):
        options = FirefoxOptions()
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['marionette'] = True
        options.set_capability('moz:firefoxOptions', capabilities)
        return options

    def create_driver(self):
        return webdriver.Firefox(self._set_capabilities())


class EdgeDriver(Driver, ABC):

    def _set_capabilities(self):
        options = EdgeOptions()
        capabilities = DesiredCapabilities.EDGE.copy()
        options.set_capability('ms:edgeOptions', capabilities)
        return options

    def create_driver(self):
        return webdriver.Edge(self._set_capabilities())


class Provider:
    @staticmethod
    def get_driver(driver_type):
        match driver_type:
            case DriverType.CHROME:
                return ChromeDriver().create_driver()
            case DriverType.FIREFOX:
                return FirefoxDriver().create_driver()
            case DriverType.EDGE:
                return EdgeDriver().create_driver()
            case _:
                raise ValueError(f'Unknown driver type: {driver_type}')
