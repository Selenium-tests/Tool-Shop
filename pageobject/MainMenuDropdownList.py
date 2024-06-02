import allure
from pageobject.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainMenuDropdownList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._partial_selector = 'a[data-test="'

        self._DROPDOWN_LIST_CONTAINER = (By.CSS_SELECTOR, '.dropdown-menu.show')
        self._TRIGGER_ELEMENT = (By.CSS_SELECTOR, 'a[data-test="nav-categories"]')

    @property
    def dropdown_list_container_locator(self):
        return self._DROPDOWN_LIST_CONTAINER

    @allure.step('Click the trigger element')
    def click_trigger_element(self):
        self.wait.until(EC.element_to_be_clickable(self._TRIGGER_ELEMENT)).click()

    @allure.step('Click the link')
    def click_link(self, partial_selector):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self._partial_selector + partial_selector + '"]'))).click()
