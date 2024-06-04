import pytest
import allure
from fixtures.General import driver, wait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.Login import login_form
from support.credentials import credentials
from support.FileNames import FileNames
from support.TestDataLoader import load_array
from support.JSONKeys import JSONKeys
from support.URL import URL

incorrect_email_testdata = load_array(FileNames.CREDENTIALS, JSONKeys.INCORRECT_EMAIL)
incorrect_password_testdata = load_array(FileNames.CREDENTIALS, JSONKeys.INCORRECT_PASSWORD)
incorrect_email_format_testdata = load_array(FileNames.CREDENTIALS, JSONKeys.INCORRECT_EMAIL_FORMAT)


def actions(l_form, email, password):
    l_form.enter_email(email)
    l_form.enter_password(password)
    l_form.click_login_button()


def check_error_message_visibility(wait, l_form):
    try:
        wait.until(EC.visibility_of_element_located(l_form.login_error_message_locator))
    except Exception as e:
        pytest.fail('The error message is not displayed')


def check_error_message_content(l_form, expected_message_content):
    assert l_form.login_error_message() == expected_message_content, 'Incorrect error message content'


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Login', 'Forms', 'Fields')
@allure.link(URL.LOGIN_PAGE, 'Login page')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Attempting to log in using an incorrect email address')
@pytest.mark.parametrize('email', incorrect_email_testdata)
def test_incorrect_email(wait, login_form, email):
    actions(login_form, email, credentials.get('password'))
    check_error_message_visibility(wait, login_form)
    check_error_message_content(login_form, 'Invalid email or password')


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Login', 'Forms', 'Fields')
@allure.link(URL.LOGIN_PAGE, 'Login page')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Attempting to log in using an incorrect password')
@pytest.mark.parametrize('password', incorrect_password_testdata)
def test_incorrect_password(wait, login_form, password):
    actions(login_form, credentials.get('email'), password)
    check_error_message_visibility(wait, login_form)
    check_error_message_content(login_form, 'Invalid email or password')


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Login', 'Forms', 'Fields')
@allure.link(URL.LOGIN_PAGE, 'Login page')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Attempting to log in using an incorrect email format')
@pytest.mark.parametrize('email', incorrect_email_format_testdata)
def test_incorrect_email_format(wait, login_form, email):
    actions(login_form, email, credentials.get('password'))
    check_error_message_visibility(wait, login_form)
    check_error_message_content(login_form, 'Email format is invalid')


@allure.label('owner', 'Paweł Aksman')
@allure.epic('E2E')
@allure.tag('Login', 'Forms', 'Fields')
@allure.link(URL.LOGIN_PAGE, 'Login page')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Logging in using correct credentials')
def test_correct_credentials(wait, login_form):
    actions(login_form, credentials.get('email'), credentials.get('password'))

    try:
        wait.until(EC.url_to_be(URL.ACCOUNT_PAGE))
    except Exception as e:
        pytest.fail('User is not logged in')
