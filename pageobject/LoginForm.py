import allure
from pageobject.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self._EMAIL_FIELD = (By.ID, 'email')
        self._PASSWORD_FIELD = (By.ID, 'password')
        self._LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
        self._LOGIN_ERROR = (By.CSS_SELECTOR, 'div.alert.alert-danger')

    def _fill_field(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    @allure.step('Enter an email')
    def enter_email(self, email):
        self._fill_field(self._EMAIL_FIELD, email)

    @allure.step('Enter a password')
    def enter_password(self, password):
        self._fill_field(self._PASSWORD_FIELD, password)

    @allure.step('Click the "Login" button')
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()

    @property
    def login_error_message_locator(self):
        return self._LOGIN_ERROR

    def login_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self._LOGIN_ERROR)).text
