
from selenium.webdriver.common.by import By


class RegisterPageLocators():
     radio_btn_male = (By.CSS_SELECTOR, "#gender-male")
     radio_btn_female = (By.CSS_SELECTOR, "#gender-female")
     first_name_field = (By.CSS_SELECTOR, "#FirstName")
     last_name_field= (By.CSS_SELECTOR, "#LastName")
     email_field = (By.CSS_SELECTOR, "#Email")
     password_field = (By.CSS_SELECTOR, "#Password")
     confirm_password_field = (By.CSS_SELECTOR, "#ConfirmPassword")
     register_button = (By.CSS_SELECTOR, "#register-button")
     success_registration = (By.CSS_SELECTOR, "div.result")
     register_form = (By.CSS_SELECTOR, ".page.registration-page")

class AuthorisationPageLocators():
     log_in_form = (By.CSS_SELECTOR, ".returning-wrapper")
     form_title = (By.CSS_SELECTOR, "div.returning-wrapper div.title strong")
     email_field = (By.CSS_SELECTOR, "#Email")
     email_label = (By.CSS_SELECTOR, "label[for='Email']")
     password_field = (By.CSS_SELECTOR, "#Password")
     password_label = (By.CSS_SELECTOR, "label[for='Password']")
     remember_me_checkbox = (By.CSS_SELECTOR, "#RememberMe")
     remember_me_checkbox_label = (By.CSS_SELECTOR, "label[for='RememberMe']")
     forgot_password_link = (By.CSS_SELECTOR, "span.forgot-password a")
     log_in_btn = (By.CSS_SELECTOR, "input[class='button-1 login-button']")
     password_recovery_form = (By.CSS_SELECTOR, ".page.password-recovery-page")
     password_recovery_title = (By.CSS_SELECTOR, "div.page-title h1")
     email_address_field = (By.CSS_SELECTOR, "#register-button")
     recover_btn = (By.CSS_SELECTOR, ".button-1.password-recovery-button")
     label_email_address_field = (By.CSS_SELECTOR, "label[for='Email']") 
     password_recover_tootip = (By.CSS_SELECTOR, ".tooltip") 
     password_recover_result = (By.CSS_SELECTOR, "div.result")   
     required_maker_on_psw_recover_page = (By.CSS_SELECTOR, "div.page.password-recovery-page span.required")  
     account_information =  (By.CSS_SELECTOR, "a.account")  
     error_message_unsuccessfull_login = (By.CSS_SELECTOR, "div.validation-summary-errors span")
     error_message_wrong_credentials = (By.CSS_SELECTOR, "div.validation-summary-errors ul li")
     error_message_invalid_email = (By.CSS_SELECTOR, "span.field-validation-error span[for='Email']")