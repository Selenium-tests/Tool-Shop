from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory


class BasePage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def go_to_page(self, url):
        self._driver.get(url)

    @property
    def driver(self):
        return self._driver

    @property
    def wait(self):
        return self._wait
