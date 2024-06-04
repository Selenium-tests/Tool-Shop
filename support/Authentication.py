from pageobject.LoginForm import LoginForm
from support.credentials import credentials
from support.URL import URL


def authentication(driver):
    driver.get(URL.LOGIN_PAGE)
    login_form = LoginForm(driver)
    login_form.enter_email(credentials.get('email'))
    login_form.enter_password(credentials.get('password'))
    login_form.click_login_button()
