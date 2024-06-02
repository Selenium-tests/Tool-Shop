import pytest
from fixtures.General import driver, wait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.Login import login_form
from support.credentials import credentials
from support.TestDataLoader import load_credentials_testdata
from support.JSONKeys import JSONKeys


incorrect_email_testdata = load_credentials_testdata(JSONKeys.INCORRECT_EMAIL)
incorrect_password_testdata = load_credentials_testdata(JSONKeys.INCORRECT_PASSWORD)


def actions(l_form, email, password):
    l_form.enter_email(email)
    l_form.enter_password(password)
    l_form.click_login_button()


@pytest.mark.parametrize('email, password', incorrect_email_testdata)
def test_incorrect_email(login_form, email, password):
    actions(login_form, email, credentials.get('password'))


@pytest.mark.parametrize('email, password', incorrect_password_testdata)
def test_incorrect_password(login_form, email, password):
    actions(login_form, credentials.get('email'), password)