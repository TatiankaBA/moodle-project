from .base_page import BasePage
from .locators import AuthorisationPageLocators
from .locators import RegisterPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .user import User
from .register_page import *

class AuthorisationPage(RegisterPage):
    def new_user_registered(self):
        radio_btn = self.browser.find_element(*RegisterPageLocators.radio_btn_male)
        radio_btn.click()
        first_name_field = self.browser.find_element(*RegisterPageLocators.first_name_field)  
        first_name_field.send_keys(User.first_name)
        last_name_field = self.browser.find_element(*RegisterPageLocators.last_name_field)
        last_name_field.send_keys(User.last_name)
        email_field = self.browser.find_element(*RegisterPageLocators.email_field)
        email_field.send_keys(User.email)
        password_field =  self.browser.find_element(*RegisterPageLocators.password_field)
        password_field.send_keys(User.password)
        confirm_password_field = self.browser.find_element(*RegisterPageLocators.confirm_password_field)
        confirm_password_field.send_keys(User.password)
        register_btn = self.browser.find_element(*RegisterPageLocators.register_button)
        register_btn.click()

    def existed_user_logged_in_successfully(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(User.email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys(User.password)
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.account_information), "The user hasn't been authorised"
        
        

    def right_login_wrong_password_failed(self):
        pass

    def wrong_login_right_password_login_failed(self):
        pass
    def wrong_login_wrong_password_login_failed(self):
        pass
    def empty_fields_login_failed(self):
        pass