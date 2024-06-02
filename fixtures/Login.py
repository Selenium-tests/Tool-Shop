import pytest
from fixtures.General import driver
from pageobject.LoginForm import LoginForm
from support.URL import URL


@pytest.fixture
def login_form(driver):
    driver.get(URL.LOGIN_PAGE)
    l_form = LoginForm(driver)
    return l_form
