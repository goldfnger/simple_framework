import allure

from helpers import allure_helper
from helpers.db_helper import del_user_from_bd
from helpers.locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Open Wishlist')
    def open_wishlist(self):
        """Open Wishlist."""
        self.click_on_element(*AccountPageLocators.WISH_LIST_LINK)

    @allure.step('Verify that product in wishlist')
    def check_item_in_wish_list(self, name):
        """Verify that product in wishlist.

        :param name: product name
        """
        elements = self._element(*AccountPageLocators.ITEM_NAMES, all=True)
        product_names = [i.text for i in elements]
        with allure.step(f'Verify that all product {product_names} contains name {name}'):
            allure_helper.attach(self.browser)
            assert name in product_names, f'Name {name}, product names in wishlist {product_names}'

    @allure.step('Perform logout from right block')
    def logout_from_right_block(self,):
        """Logout from right block."""
        self.click_on_element(*AccountPageLocators.LOGOUT_RIGHT_BLOCK)

    @allure.step('Verify text after logout')
    def check_text_after_logout(self):
        """Verify text after logout."""
        self.is_element_visible(*AccountPageLocators.TEXT_AFTER_LOGOUT)
        text = self.get_text_of_element(*AccountPageLocators.TEXT_AFTER_LOGOUT)
        with allure.step(
                'Verify that text after logout - You have been logged off your account. It is now safe to leave the computer.'):
            allure_helper.attach(self.browser)
            assert text == 'You have been logged off your account. It is now safe to leave the computer.', \
                f'Text after logout {text}'

    @allure.step('Verify right block after logout')
    def check_right_block_after_logout(self):
        """Verify right block after logout."""
        self.is_element_visible(*AccountPageLocators.REGISTER_RIGHT_BLOCK)
        self.is_element_visible(*AccountPageLocators.LOGIN_RIGHT_BLOCK)

    @allure.step('Perform login after logout')
    def click_my_account_after_logout(self, db_connection, email, fistname, del_user=True):
        """Perform login after logout."""
        self.click_on_element(*AccountPageLocators.MY_ACCOUNT_RIGHT_BLOCK)
        if del_user:
            del_user_from_bd(db_connection, email, fistname)
