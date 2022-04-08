import pytest
from selenium import webdriver
from .pages.authorisation_page import AuthorisationPage
from .pages.user import *
from .pages.links import *
from .pages.register_page import RegisterPage
from .pages.locators import AuthorisationPageLocators
from .pages.base_page import *


@pytest.mark.ui
def test_log_in_form_is_present(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    assert page.is_element_present(*AuthorisationPageLocators.log_in_form), "The login form is absent"  
@pytest.mark.ui
def test_form_title_is_present(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    assert page.is_element_present(*AuthorisationPageLocators.form_title), "The form title is absent" 
@pytest.mark.ui
def test_form_title_text_is_correct(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    form_title = page.browser.find_element(*AuthorisationPageLocators.form_title)
    assert form_title.text == 'Returning Customer', "The form title's text is not correct" 
@pytest.mark.ui
def test_email_field_is_present(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    assert page.is_element_present(*AuthorisationPageLocators.email_field), "The email field is absent" 
@pytest.mark.ui
def test_email_field_label_is_correct(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    email_field_label = page.browser.find_element(*AuthorisationPageLocators.email_label)
    assert email_field_label.text == 'Email:', "The email field label is not correct" 
@pytest.mark.ui
def test_passwprd_field_is_present(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    assert page.is_element_present(*AuthorisationPageLocators.password_field), "The email field is absent" 
@pytest.mark.ui
def test_password_field_label_is_correct(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    password_label = page.browser.find_element(*AuthorisationPageLocators.password_label)
    assert password_label.text == 'Password:', "The password field label is not correct" 
@pytest.mark.ui
def test_remember_me_checkbox_is_present(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    assert page.is_element_present(*AuthorisationPageLocators.remember_me_checkbox), "The email field is absent" 
@pytest.mark.ui
def test_remember_me_checkbox_label_is_correct(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    remember_me_checkbox_label = page.browser.find_element(*AuthorisationPageLocators.remember_me_checkbox_label)
    assert remember_me_checkbox_label.text == 'Remember me?', "The 'remember me' label is not correct" 
@pytest.mark.ui
def test_forgot_password_link_is_present(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    assert page.is_element_present(*AuthorisationPageLocators.forgot_password_link), "The forgot password link is absent" 
@pytest.mark.ui
def test_forgot_password_link_text_is_correct(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    forgot_password_link = page.browser.find_element(*AuthorisationPageLocators.forgot_password_link)
    assert forgot_password_link.text == 'Forgot password?', "The forgot password link text is not correct" 
@pytest.mark.ui
def test_forgot_password_link_right_href(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    forgot_password_link_href = page.browser.find_element(*AuthorisationPageLocators.forgot_password_link)
    assert forgot_password_link_href.get_attribute('href') == AllLinks.password_recovery, 'The forgot password link is not correct' 

#the user shouldn't exist to run tests correctly, first create new user data in the file 'user.py'
@pytest.mark.skip
def test_new_user_successfully_registered(browser):
    link = AllLinks.register_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.new_user_registered()
    page.register_msg_success()
@pytest.mark.functional_tests
def test_registered_user_successfully_logged_in(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.existed_user_logged_in_successfully()
@pytest.mark.functional_tests
def test_right_email_wrong_password_login_failed(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.right_email_wrong_password_login_failed()
@pytest.mark.functional_tests
def test_wrong_email_right_password_login_failed(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.wrong_email_right_password_login_failed()
@pytest.mark.functional_tests
def test_wrong_email_wrong_password_login_failed(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.wrong_email_right_password_login_failed()
@pytest.mark.functional_tests
def test_empty_fields_login_failed(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.empty_fields_login_failed()
@pytest.mark.functional_tests
def test_error_msg_invalid_email_appeared(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.error_msg_invalid_email_appeared()
@pytest.mark.functional_tests
def test_error_msg_invalid_email_disappeared(browser):
    link = AllLinks.login_url
    page = AuthorisationPage(browser,link)
    page.open()
    page.error_msg_invalid_email_disappeared()






      
