import pytest
from .base_page import BasePage
from .locators import RegisterPageLocators
import faker
import time


class RegisterPage(BasePage):

#проверка успешной регистрации при выборе в radio button мужского и женского пола
    def register_new_user(self,gender):
        radio_btn = self.browser.find_element(*gender)
        radio_btn.click()
        f = faker.Faker()
        first_name = f.first_name()
        last_name = f.last_name()
        email = f.email()      
        password = f.password(length = 6, special_chars=True, digits=True, upper_case=True, lower_case=True)
        first_name_field = self.browser.find_element(*RegisterPageLocators.first_name_field)
        first_name_field.send_keys(first_name)
        last_name_field = self.browser.find_element(*RegisterPageLocators.last_name_field)
        last_name_field.send_keys(last_name)
        email_field = self.browser.find_element(*RegisterPageLocators.email_field)
        email_field.send_keys(email)
        time.sleep(10)
        password_field =  self.browser.find_element(*RegisterPageLocators.password_field)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*RegisterPageLocators.confirm_password_field)
        confirm_password_field.send_keys(password)
        register_btn = self.browser.find_element(*RegisterPageLocators.register_button)
        register_btn.click()


#проверка, что текст текста об успешной регистрации верен

    def register_msg_success(self):
        message = self.browser.find_element(*RegisterPageLocators.success_registration)
        assert message.text == 'Your registration completed', "The success message text is absent or not correct"
        
#тестирование UI, все элементы формы регистрации на месте

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.register_form), "Register form is not presented"



