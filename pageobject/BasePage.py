from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    @property
    def driver(self):
        return self._driver

    @property
    def wait(self):
        return self._wait
