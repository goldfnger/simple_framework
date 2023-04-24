import allure

from helpers.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):

    @allure.step('Verify visibility of elements on the page')
    def check_elements_visibility(self):
        """Verify visibility of elements on the page."""
        lst = [ProductPageLocators.PRODUCT_HEADER,
               ProductPageLocators.BUTTON_CART,
               ProductPageLocators.IMAGES_BLOCK,
               ProductPageLocators.RATING_BLOCK,
               ProductPageLocators.PRODUCT_DESCRIPTION]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Click on main product image')
    def click_main_product_image(self):
        """Click on main product image."""
        self.click_on_element(*ProductPageLocators.MAIN_PRODUCT_IMAGE)

    @allure.step('Verify that image is opened in pop up window')
    def check_main_image_in_window(self):
        """Verify that image is opened in pop up window."""
        self.is_element_visible(*ProductPageLocators.PRODUCT_IMAGE_IN_WINDOW)

    @allure.step('Open tab Specification')
    def click_on_tab_specification(self):
        """Click on tab Specification."""
        self.click_on_element(*ProductPageLocators.TAB_SPECIFICATION_LINK)
        with allure.step('Verify that tab Specification is active'):
            assert self.getting_attr(
                'class', *ProductPageLocators.TAB_CLASS, 1) == 'active',\
                'Tab Specification is not active'

    @allure.step('Open tab Reviews')
    def click_on_tab_reviews(self):
        """Click on tab Reviews."""
        self.click_on_element(*ProductPageLocators.TAB_REVIEWS_LINK)
        with allure.step('Verify that tab Reviews is active'):
            assert self.getting_attr('class', *ProductPageLocators.TAB_CLASS, 2) == 'active',\
                'Tab Reviews is not active'

    @allure.step('Open tab Description')
    def click_on_tab_description(self):
        """Click on tab Description."""
        self.click_on_element(*ProductPageLocators.TAB_DESCRIPTION_LINK)
        with allure.step('Verify that tab Description is active'):
            assert self.getting_attr(
                'class', *ProductPageLocators.TAB_CLASS, 0) == 'active',\
                'Tab Description is not active'

    @allure.step('Verify product title - {name}')
    def compare_item_title_on_pages(self, name):
        """Gets product name with passed selector and compare title on the pages

        :param name: product title
        """
        name_on_product_page = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        with allure.step(f'Verify that title in {name_on_product_page} matches {name}'):
            assert name == name_on_product_page,  \
                f'Title - {name}, on product page - {name_on_product_page}'

    @allure.step('Add product in Wishlist')
    def add_to_wishlist(self):
        """Add product in wishlist. Returns title of added product.
        """
        name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        self.click_on_element(*ProductPageLocators.WISH_LIST_BUTTON)
        return name

    @allure.step('Add product in Comparison')
    def add_to_compare(self):
        """Add product in comparison. Returns title of added product.
        """
        name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        self.click_on_element(*ProductPageLocators.COMPARE_BUTTON)
        return name

    @allure.step('Add product in Cart')
    def add_to_cart(self):
        """Add product in Cart. Returns title of added product.
        """
        name = self.get_text_of_element(*ProductPageLocators.ITEM_TITLE)
        self.click_on_element(*ProductPageLocators.BUTTON_CART)
        return name

    @allure.step('Write a review on product: author {name}, review {value}, rate index {idx}')
    def write_review(self, name, value, idx):
        """After filled up form and submit returns author name and text of review.

        :param name: author name
        :param value: text review
        :param idx: rate index
        """
        self.click_on_element(*ProductPageLocators.WRITE_REVIEW_BUTTON)
        self.input_text(*ProductPageLocators.REVIEW_NAME_FIELD, name)
        self.input_text(*ProductPageLocators.REVIEW_FIELD, value)
        if idx:
            self.click_on_element(*ProductPageLocators.RATING_RADIO_BUTTON, idx)
        self.click_on_element(*ProductPageLocators.REVIEW_BUTTON)

    @allure.step('Verify for information blocks')
    def check_visibility_of_info_blocks(self):
        """Verify for information blocks."""
        self.is_element_visible(*ProductPageLocators.RIGHT_BLOCK_INFO, index=0)
        self.is_element_visible(*ProductPageLocators.RIGHT_BLOCK_INFO, index=1)

    @allure.step('Verify fiels in first info block')
    def check_fields_in_first_info_block(self):
        """Verify fiels in first info block."""
        brand = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=0)
        with allure.step(f'Verify that brand name {brand} starts with Brand:'):
            assert brand.startswith('Brand:'), f'Brand info - {brand}'

        product_code = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=1)
        with allure.step(f'Verify that product code {product_code} starts with Product Code:'):
            assert product_code.startswith('Product Code:'), f'Code info - {product_code}'

        reward = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=2)
        with allure.step(f'Verify that reward field {reward} starts with Reward Points:'):
            assert reward.startswith('Reward Points:'), f'Reward info - {reward}'

        availability = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST, index=3)
        with allure.step(f'Verify that availability field {availability} starts with Availability:'):
            assert availability.startswith('Availability:'), f'Availability info - {availability}'

    @allure.step('Verify visibility of price')
    def check_visibility_of_price(self):
        """Verify visibility of price."""
        self.is_element_visible(*ProductPageLocators.PRODUCT_PRICE)

    @allure.step('Verify fields in second info block')
    def check_fields_in_second_info_block(self):
        """Verify fields in second info block."""
        tax = self.get_text_of_element(*ProductPageLocators.ELEMENTS_OF_RIGHT_BLOCK_INFO_SECOND, index=1)
        with allure.step(f'Verify that tax field {tax} starts with Ex Tax:'):
            assert tax.startswith('Ex Tax:'), f'Tax info - {tax}'
