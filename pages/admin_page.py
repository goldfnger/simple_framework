import allure

from helpers.locators import AdminPageLocators
from pages.base_page import BasePage


class AdminPage(BasePage):

    @allure.step('Verify visibility of elements on the page')
    def check_elements_visibility(self):
        """Verify visibility of elements."""
        lst = [AdminPageLocators.PANEL_HEADING,
               AdminPageLocators.USERNAME_INPUT,
               AdminPageLocators.PASSWORD_INPUT,
               AdminPageLocators.LOGIN_BUTTON]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Login in admin panel with username {name} and password {passw}')
    def login(self, name, passw):
        """Admin login.

        :param name: user name
        :param passw: user password
        """
        self.input_text(*AdminPageLocators.USERNAME_INPUT, name)
        self.input_text(*AdminPageLocators.PASSWORD_INPUT, passw)
        self.click_on_element(*AdminPageLocators.LOGIN_BUTTON)

    @allure.step('Press logout button')
    def logout(self):
        """Find and press on logout button."""
        self.click_on_element(*AdminPageLocators.LOGOUT_BUTTON)

    @allure.step('Verify successful logout from admin panel')
    def check_successful_logout_text(self):
        """Verify visibility of elements after logout."""
        self.is_element_visible(*AdminPageLocators.NEED_LOGIN_TEXT)

    @allure.step('Go to product table')
    def get_product_table(self):
        """Go to product table."""
        with allure.step('Click on Catalog in left menu'):
            self.click_on_element(*AdminPageLocators.LEFT_MENU_CATALOGUE)
        with allure.step('Click on Products in left menu'):
            self.click_on_element(*AdminPageLocators.LEFT_MENU_PRODUCTS)

    @allure.step('Verify that table is displayed')
    def check_products_table(self):
        """Verify visibility of table."""
        self.is_element_visible(*AdminPageLocators.PRODUCTS_TABLE)
