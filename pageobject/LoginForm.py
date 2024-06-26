import allure
from pageobject.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self._EMAIL_ERROR = (By.ID, 'email-error')
        self._PASSWORD_ERROR = (By.ID, 'password-error')
        self._LOGIN_ERROR = (By.CSS_SELECTOR, 'div.alert.alert-danger')

    locators = {
        'email_field': ('ID', 'email'),
        'password_field': ('ID', 'password'),
        'login_button': ('CSS', 'input[type="submit"]'),
    }

    def _fill_field(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    @allure.step('Enter an email')
    def enter_email(self, email):
        self._fill_field(self.email_field, email)

    @allure.step('Enter a password')
    def enter_password(self, password):
        self._fill_field(self.password_field, password)

    @allure.step('Click the "Login" button')
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def email_error_message_locator(self):
        return self._EMAIL_ERROR

    def email_error_message_content(self):
        return self.wait.until(EC.visibility_of_element_located(self._EMAIL_ERROR)).text

    def password_error_message_locator(self):
        return self._PASSWORD_ERROR

    def password_error_message_content(self):
        return self.wait.until(EC.visibility_of_element_located(self._PASSWORD_ERROR)).text

    def login_error_message_locator(self):
        return self._LOGIN_ERROR

    def login_error_message_content(self):
        return self.wait.until(EC.visibility_of_element_located(self._LOGIN_ERROR)).text
