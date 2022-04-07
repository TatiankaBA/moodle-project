import pytest
from selenium import webdriver
from .pages.authorisation_page import AuthorisationPage
from .pages.user import *
from .pages.links import *
from .pages.register_page import RegisterPage

#для прохождения теста пользователь должен быть незарегистрирован, необходимо изменыть для этого тестовые данные в файле user.py
@pytest.mark.skip
def test_new_user_successfully_registered(browser):
    link = AllLinks.register_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.new_user_registered()
    page.register_msg_success()



def test_registered_user_successfully_logged_in(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.existed_user_logged_in_successfully()

def test_right_email_wrong_password_login_failed(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.right_email_wrong_password_login_failed()

def test_wrong_email_right_password_login_failed(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.wrong_email_right_password_login_failed()

def test_wrong_email_wrong_password_login_failed(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.wrong_email_right_password_login_failed()

def test_empty_fields_login_failed(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.empty_fields_login_failed()






      
