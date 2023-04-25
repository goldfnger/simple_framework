import allure

from helpers import allure_helper
from helpers.locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):

    @allure.step('Verify visibility of elements on the page')
    def check_elements_visibility(self):
        """Verify visibility of elements on the page."""
        lst = [RegisterPageLocators.HEADER,
               RegisterPageLocators.TEXT_FOR_LOGIN,
               RegisterPageLocators.FIRST_NAME_FIELD,
               RegisterPageLocators.LAST_NAME_FIELD,
               RegisterPageLocators.EMAIL_FIELD,
               RegisterPageLocators.TEL_FIELD,
               RegisterPageLocators.PASSW_FIELD,
               RegisterPageLocators.CONFIRM_FIELD,
               RegisterPageLocators.PRIVACY_POLICY,
               RegisterPageLocators.CONTINUE_BUTTON,
               RegisterPageLocators.RIGHT_MENU]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step(
        'Register a user: email {email}, firstname {firstname}, '
        'lastname {lastname}, phone {tel}, password {password}, confirmation password {confirm}, '
        'newsletter agreement {radio_idx}')
    def register_user(
            self, firstname, lastname, email, tel, password, confirm, radio_idx, checkbox=True):
        """User registration process.

        :param firstname: firstname
        :param lastname: lastname
        :param email: email
        :param password: password
        :param confirm: confirm password
        :param radio_idx: newsletter agreement
        :param checkbox: tos agreement
        """
        if firstname:
            self.input_text(*RegisterPageLocators.FIRST_NAME_FIELD, firstname)
        if lastname:
            self.input_text(*RegisterPageLocators.LAST_NAME_FIELD, lastname)
        if email:
            self.input_text(*RegisterPageLocators.EMAIL_FIELD, email)
        if tel:
            self.input_text(*RegisterPageLocators.TEL_FIELD, tel)
        if password:
            self.input_text(*RegisterPageLocators.PASSW_FIELD, password)
        if confirm:
            self.input_text(*RegisterPageLocators.CONFIRM_FIELD, confirm)
        if radio_idx == 0 or radio_idx == 1:
            self.click_on_element(*RegisterPageLocators.SUBSCRIBE_RADIO, radio_idx)
        if checkbox:
            self.click_on_element(*RegisterPageLocators.AGREE_CHECKBOX)
        self.click_on_element(*RegisterPageLocators.CONTINUE_BUTTON)

    @allure.step('Verify that error displayed - firstname is required')
    def check_fail_register_without_firstname(self):
        """ Verify that error displayed if firstname is missing. """
        self.is_element_visible(*RegisterPageLocators.FIRST_NAME_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.FIRST_NAME_ERROR)
        with allure.step('Verify that error text with empty firstname - First Name must be between 1 and 32 characters!'):
            allure_helper.attach(self.browser)
            assert error_text == 'First Name must be between 1 and 32 characters!', \
                f'Error text {error_text}'

    @allure.step('Verify that error displayed - lastname is required')
    def check_fail_register_without_lastname(self):
        """ Verify that error displayed if lastname is missing. """
        self.is_element_visible(*RegisterPageLocators.LAST_NAME_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.LAST_NAME_ERROR)
        with allure.step(
                'Verify that error text with empty lastname - Last Name must be between 1 and 32 characters!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Last Name must be between 1 and 32 characters!', \
                f'Error text {error_text}'

    @allure.step('Verify that error displayed - email is required')
    def check_fail_register_without_email(self):
        """ Verify that error displayed if email is missing. """
        self.is_element_visible(*RegisterPageLocators.EMAIL_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.EMAIL_ERROR)
        with allure.step(
                'Verify that error text with empty email - E-Mail Address does not appear to be valid!'):
            allure_helper.attach(self.browser)
            assert error_text == 'E-Mail Address does not appear to be valid!', \
                f'Error text {error_text}'

    @allure.step('Verify that error displayed - phone is required')
    def check_fail_register_without_telephone(self):
        """ Verify that error displayed if phone is missing. """
        self.is_element_visible(*RegisterPageLocators.TEL_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.TEL_ERROR)
        with allure.step(
                'Verify that error text with empty phone - Telephone must be between 3 and 32 characters!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Telephone must be between 3 and 32 characters!', \
                f'Error text {error_text}'

    @allure.step('Verify that error displayed - password is required')
    def check_fail_register_without_password(self):
        """ Verify that error displayed if password is missing. """
        self.is_element_visible(*RegisterPageLocators.PASSWORD_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.PASSWORD_ERROR)
        with allure.step(
                'Verify that error text with empty password - Password must be between 4 and 20 characters!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Password must be between 4 and 20 characters!', \
                f'Error text {error_text}'

    @allure.step('Verify that error displayed - password confirmation is required')
    def check_fail_register_without_confirm(self):
        """ Verify that error displayed if password confirmation is missing. """
        self.is_element_visible(*RegisterPageLocators.CONFIRM_ERROR)
        error_text = self.get_text_of_element(*RegisterPageLocators.CONFIRM_ERROR)
        with allure.step(
                'Verify that error text with empty password confirmation - Password confirmation does not match password!'):
            allure_helper.attach(self.browser)
            assert error_text == 'Password confirmation does not match password!', \
                f'Error text {error_text}'
