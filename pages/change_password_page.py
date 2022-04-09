from .locators import AuthorisationPageLocators
from .locators import ChangePasswordPageLocators
from .authorisation_page import AuthorisationPage
from .user import ExistedUser
from .base_page import *

class ChangePasswordPage(AuthorisationPage): 
    def user_logged_in(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(ExistedUser.email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys(ExistedUser.password)
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.account_information), "The user has been authorised"
    def user_can_change_password_with_right_credentials(self):
        old_password_field = self.browser.find_element(*ChangePasswordPageLocators.old_password_field)
        old_password_field.send_keys(ExistedUser.password)
        new_password_field = self.browser.find_element(*ChangePasswordPageLocators.new_password_field)
        new_password_field.send_keys(ExistedUser.new_password)
        confirm_password_field = self.browser.find_element(*ChangePasswordPageLocators.confirm_password_field)
        confirm_password_field.send_keys(ExistedUser.new_password)
        change_password_btn = self.browser.find_element(*ChangePasswordPageLocators.change_password_btn)
        change_password_btn.click()
        assert self.is_element_present(*ChangePasswordPageLocators.result_msg), "The result message is absent"
        result_msg = self.browser.find_element(*ChangePasswordPageLocators.result_msg)
        assert result_msg.text == 'Password was changed', "The result message is not correct"
    def user_can_login_with_new_password(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(ExistedUser.email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys(ExistedUser.new_password)
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.account_information), "The user hasn't been authorised"
    def user_cannot_login_with_previous_password(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(ExistedUser.email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys(ExistedUser.password)
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.error_message_unsuccessfull_login), "The user has been authorised"

    def change_password_valid_old_password_valid_new_password_invalid_confirm_password(self):
        old_password_field = self.browser.find_element(*ChangePasswordPageLocators.old_password_field)
        old_password_field.send_keys(ExistedUser.new_password)
        new_password_field = self.browser.find_element(*ChangePasswordPageLocators.new_password_field)
        new_password_field.send_keys(ExistedUser.wrong_password)
        confirm_password_field = self.browser.find_element(*ChangePasswordPageLocators.confirm_password_field)
        confirm_password_field.send_keys(ExistedUser.wrong_password2)
        change_password_btn = self.browser.find_element(*ChangePasswordPageLocators.change_password_btn)
        change_password_btn.click()
        assert self.is_element_present(*ChangePasswordPageLocators.password_is_required_error_input), "The validation error input is absent"
        password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.password_is_required_error_msg)
        assert password_is_required_error_msg.text == 'The new password and confirmation password do not match.', "The error message is not correct"

    def change_password_invalid_old_password_valid_new_password_valid_confirm_password(self):
        old_password_field = self.browser.find_element(*ChangePasswordPageLocators.old_password_field)
        old_password_field.send_keys(ExistedUser.wrong_password)
        new_password_field = self.browser.find_element(*ChangePasswordPageLocators.new_password_field)
        new_password_field.send_keys(ExistedUser.wrong_password2)
        confirm_password_field = self.browser.find_element(*ChangePasswordPageLocators.confirm_password_field)
        confirm_password_field.send_keys(ExistedUser.wrong_password2)
        change_password_btn = self.browser.find_element(*ChangePasswordPageLocators.change_password_btn)
        change_password_btn.click()
        assert self.is_element_present(*ChangePasswordPageLocators.validation_error), "The validation error is absent"
        validation_error = self.browser.find_element(*ChangePasswordPageLocators.validation_error)
        assert validation_error.text == "Old password doesn't match", "The validation error message is not correct"
        
    def change_password_invalid_old_password_invalid_new_password_invalid_confirm_password(self):
        old_password_field = self.browser.find_element(*ChangePasswordPageLocators.old_password_field)
        old_password_field.send_keys(ExistedUser.wrong_password)
        new_password_field = self.browser.find_element(*ChangePasswordPageLocators.new_password_field)
        new_password_field.send_keys(ExistedUser.less6digitpassword)
        confirm_password_field = self.browser.find_element(*ChangePasswordPageLocators.confirm_password_field)
        confirm_password_field.send_keys(ExistedUser.wrong_password)
        change_password_btn = self.browser.find_element(*ChangePasswordPageLocators.change_password_btn)
        change_password_btn.click()
        assert self.is_element_present(*ChangePasswordPageLocators.password_is_required_error_input), "The validation error input is absent"
        password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.password_is_required_error_msg)
        assert password_is_required_error_msg.text == 'The new password and confirmation password do not match.', "The error message is not correct"
        invalid_password_msg  = self.browser.find_element(*ChangePasswordPageLocators.invalid_password_msg)
        assert invalid_password_msg.text == 'The password should have at least 6 characters.', "The error message about invalid password is not correct"

    def change_password_valid_old_password_empty_field_password_empty_field_confirm_password(self):
        old_password_field = self.browser.find_element(*ChangePasswordPageLocators.old_password_field)
        old_password_field.send_keys(ExistedUser.new_password)
        new_password_field = self.browser.find_element(*ChangePasswordPageLocators.new_password_field)
        new_password_field.send_keys('')
        confirm_password_field = self.browser.find_element(*ChangePasswordPageLocators.confirm_password_field)
        confirm_password_field.send_keys('')
        change_password_btn = self.browser.find_element(*ChangePasswordPageLocators.change_password_btn)
        change_password_btn.click()
        password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.password_is_required_error_msg)
        assert password_is_required_error_msg.text == 'Password is required.', "The error message is not correct"
        new_password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.new_password_is_required_error_msg)
        assert new_password_is_required_error_msg.text == 'New password is required.', "The error message is not correct"

    def change_password_with_empty_fields(self):
        old_password_field = self.browser.find_element(*ChangePasswordPageLocators.old_password_field)
        old_password_field.send_keys('')
        new_password_field = self.browser.find_element(*ChangePasswordPageLocators.new_password_field)
        new_password_field.send_keys('')
        confirm_password_field = self.browser.find_element(*ChangePasswordPageLocators.confirm_password_field)
        confirm_password_field.send_keys('')
        change_password_btn = self.browser.find_element(*ChangePasswordPageLocators.change_password_btn)
        change_password_btn.click()
        password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.password_is_required_error_msg)
        assert password_is_required_error_msg.text == 'Password is required.', "The error message is not correct"
        new_password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.new_password_is_required_error_msg)
        assert new_password_is_required_error_msg.text == 'New password is required.', "The error message is not correct"
        old_password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.old_password_is_required_error_msg)
        assert old_password_is_required_error_msg.text == 'Old password is required.', "The error message is not correct"

    def change_password_valid_old_password_new_password_and_confirm_password_with_spaces(self):
        old_password_field = self.browser.find_element(*ChangePasswordPageLocators.old_password_field)
        old_password_field.send_keys(ExistedUser.new_password)
        new_password_field = self.browser.find_element(*ChangePasswordPageLocators.new_password_field)
        new_password_field.send_keys(ExistedUser.spaces_password)
        confirm_password_field = self.browser.find_element(*ChangePasswordPageLocators.confirm_password_field)
        confirm_password_field.send_keys(ExistedUser.spaces_password)
        change_password_btn = self.browser.find_element(*ChangePasswordPageLocators.change_password_btn)
        change_password_btn.click()
        password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.password_is_required_error_msg)
        assert password_is_required_error_msg.text == 'Password is required.', "The error message is not correct"
        new_password_is_required_error_msg = self.browser.find_element(*ChangePasswordPageLocators.new_password_is_required_error_msg)
        assert new_password_is_required_error_msg.text == 'New password is required.', "The error message is not correct"
        

    
        