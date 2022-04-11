import pytest
from selenium import webdriver
from .pages.links import AllLinks
from .pages.change_password_page import *
from .pages.base_page import *
# после каждого тесте в user.py необходимо поменять password на new_password. Установить новый пароль для new_password
@pytest.mark.functional_tests
def test_user_can_change_password_with_right_credentials(browser):
    link = AllLinks.login_url 
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_logged_in()
    link = AllLinks.change_password_url 
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_can_change_password_with_right_credentials()
@pytest.mark.functional_tests
def test_user_can_login_with_new_password(browser):
    link = AllLinks.login_url
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_can_login_with_new_password()   
@pytest.mark.functional_tests
def test_user_cannot_login_with_previous_password(browser):
    link = AllLinks.login_url
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_cannot_login_with_previous_password()   
@pytest.mark.functional_tests
def test_change_password_valid_old_password_valid_new_password_invalid_confirm_passoword_failed(browser):
    link = AllLinks.login_url
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_can_login_with_new_password()   
    link = AllLinks.change_password_url 
    page = ChangePasswordPage(browser,link)
    page.open()
    page.change_password_valid_old_password_valid_new_password_invalid_confirm_password()
@pytest.mark.functional_tests
def test_change_password_invalid_old_password_invalid_new_password_invalid_confirm_password_failed(browser):
    link = AllLinks.login_url
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_can_login_with_new_password()   
    link = AllLinks.change_password_url 
    page = ChangePasswordPage(browser,link)
    page.open()
    page.change_password_invalid_old_password_invalid_new_password_invalid_confirm_password()
@pytest.mark.functional_tests
def test_change_password_invalid_old_password_valid_new_password_valid_confirm_password_failed(browser):
    link = AllLinks.login_url
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_can_login_with_new_password()   
    link = AllLinks.change_password_url 
    page = ChangePasswordPage(browser,link)
    page.open()
    page.change_password_invalid_old_password_valid_new_password_valid_confirm_password()
@pytest.mark.functional_tests
def test_change_password_valid_old_password_empty_field_password_empty_field_confirm_password_failed(browser):
    link = AllLinks.login_url
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_can_login_with_new_password()   
    link = AllLinks.change_password_url 
    page = ChangePasswordPage(browser,link)
    page.open()
    page.change_password_valid_old_password_empty_field_password_empty_field_confirm_password()
@pytest.mark.functional_tests
def test_change_password_with_empty_fields_failed(browser):
    link = AllLinks.login_url
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_can_login_with_new_password()   
    link = AllLinks.change_password_url 
    page = ChangePasswordPage(browser,link)
    page.open()
    page.change_password_with_empty_fields()
@pytest.mark.new
def test_change_password_valid_old_password_new_password_and_confirm_password_with_spaces_failed(browser):
    link = AllLinks.login_url
    page = ChangePasswordPage(browser,link)
    page.open()
    page.user_can_login_with_new_password()   
    link = AllLinks.change_password_url 
    page = ChangePasswordPage(browser,link)
    page.open()
    page.change_password_valid_old_password_new_password_and_confirm_password_with_spaces()







