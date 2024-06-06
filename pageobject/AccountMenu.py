import allure
from pageobject.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AccountMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self._partial_selector = 'a[data-test="'

    @allure.step('Click the link')
    def click_link(self, partial_selector):
        print('SEL: ' + self._partial_selector + partial_selector + '"]')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._partial_selector + partial_selector + '"]'))).click()
