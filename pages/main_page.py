import allure

from helpers import allure_helper
from helpers.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Verify visibility of elements on the page')
    def check_elements_visibility(self):
        """Verify visibility of elements."""
        lst = [MainPageLocators.BANNER,
               MainPageLocators.BANNER_PAGINATION_BULLETS,
               MainPageLocators.HEADER_FEATURED,
               MainPageLocators.CAROUSEL_BRAND,
               MainPageLocators.CAROUSEL_PAGINATION_BULLETS]
        for i in lst:
            self.is_element_visible(*i)

    @allure.step('Click on selected button under the banner')
    def click_banner_bullet_active(self):
        """Click on selected button for switch banner."""
        if self.getting_attr('class', *MainPageLocators.BANNER_BULLET, 0) == \
                    'swiper-pagination-bullet swiper-pagination-bullet-active':
            self.click_on_element(*MainPageLocators.BANNER_BULLET, 0)
            self.is_element_visible(*MainPageLocators.BANNER_IPHONE)
        elif self.getting_attr('class', *MainPageLocators.BANNER_BULLET, 1) == \
                    'swiper-pagination-bullet swiper-pagination-bullet-active':
            self.click_on_element(*MainPageLocators.BANNER_BULLET, 1)
            self.is_element_visible(*MainPageLocators.BANNER_MACBOOK)

    @allure.step('Click on not selected button under the banner')
    def click_banner_bullet_inactive(self):
        """Click on not selected button for switch banner."""
        if self.getting_attr('class', *MainPageLocators.BANNER_BULLET, 0) == \
                    'swiper-pagination-bullet swiper-pagination-bullet-active':
            self.click_on_element(*MainPageLocators.BANNER_BULLET, 1)
            self.is_element_visible(*MainPageLocators.BANNER_MACBOOK)
        elif self.getting_attr('class', *MainPageLocators.BANNER_BULLET, 1) == \
                    'swiper-pagination-bullet swiper-pagination-bullet-active':
            self.click_on_element(*MainPageLocators.BANNER_BULLET, 0)
            self.is_element_visible(*MainPageLocators.BANNER_IPHONE)

    @allure.step('Click on the product with {index} in module Featured')
    def go_to_product_from_featured(self, index):
        """Click on the product in module Featured.
        Returns product name.

        :param index: index of element
        """
        name = self.get_text_of_element(*MainPageLocators.FEATURED_PRODUCT_NAME, index)
        self.click_on_element(*MainPageLocators.FEATURED_PRODUCT_LINK, index)
        return name

    @allure.step('Click on buttons for switching brands in carousel')
    def click_carousel_bullet(self):
        """Click on buttons for switching carousel."""
        with allure.step('Get all elements from carousel'):
            elements = self._element(*MainPageLocators.BRAND_IMAGE_IN_CAROUSEL, all=True)
        with allure.step('Click one by one on the carousel buttons'):
            for i in range(11):
                with allure.step(f'Click on the button with index {i}'):
                    self.click_on_element(*MainPageLocators.CAROUSEL_PAGINATION_BULLET, i)
                    for k in elements:
                        with allure.step('Get attribute value data-swiper-slide-index'):
                            attr = k.get_attribute('data-swiper-slide-index')
                            with allure.step(f'Verify that attribute {attr} equal to {i}'):
                                if attr == str(i):
                                    with allure.step('Get list of attributes class element'):
                                        actual_class = k.get_attribute('class').split()
                                        with allure.step(f'Verify that classes swiper-slide-active or swiper-slide-duplicate-active exists in {actual_class}'):
                                            allure_helper.attach(self.browser)
                                            assert 'swiper-slide-active' or 'swiper-slide-duplicate-active' \
                                                   in actual_class, f'Class - {actual_class}'
                                        break
