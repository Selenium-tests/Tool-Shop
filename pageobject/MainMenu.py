from pageobject.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._partial_selector = 'a[data-test="'

    def click_link(self, partial_selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._partial_selector + partial_selector + '"]'))).click()
