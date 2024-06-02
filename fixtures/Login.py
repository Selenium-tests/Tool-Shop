import pytest
from fixtures.General import driver
from pageobject.LoginForm import LoginForm


@pytest.fixture
def login_form(driver):
    l_form = LoginForm(driver)
    return l_form