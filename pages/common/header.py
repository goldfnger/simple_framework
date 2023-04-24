import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from helpers.allure_helper import attach
from helpers.locators import HeaderPageLocators
from helpers.styles import Border, Colors, Cursor, Gradients, SIZES
from helpers.waits import Element, Elements


class Header:
    def __init__(self, browser):
        self.browser = browser

    @property
    def logo(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.LOGO))

    @property
    def cart_button(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.CART_BUTTON))

    @property
    def search_input(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.SEARCH_INPUT))

    @property
    def search_button(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.SEARCH_BUTTON))

    @property
    def account_link(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.MY_ACCOUNT_LINK))

    @property
    def login_link(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.LOGIN_LINK))

    @property
    def currency_dropdown_button(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.CURRENCY_DROP_DOWN_BUTTON))

    @property
    def currency_dropdown(self):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.CURRENCY_DROP_DONW))

    @property
    def currency_dropdown_values(self):
        return WebDriverWait(self.browser, 5).until(Elements(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS))

    def currency_dropdown_value(self, idx):
        return WebDriverWait(self.browser, 5).until(Element(*HeaderPageLocators.CURRENCY_VALUES_BUTTONS, idx))

    @allure.step('Verify visibility of elements on the page')
    def check_elements_visibility(self):
        """Verification of elements visibility"""
        lst = [HeaderPageLocators.LOGO,
               HeaderPageLocators.MENU,
               HeaderPageLocators.CART_BUTTON,
               HeaderPageLocators.TOP_LINKS,
               HeaderPageLocators.SEARCH_FIELD]
        for i in lst:
            el = WebDriverWait(self.browser, 5).until(Element(*i))
            attach(self.browser)
            assert el.is_displayed(), f'Element {i} is not displayed on the page'

    @allure.step('Make search with value {value}')
    def search(self, value):
        """Enter text in search field

        :param value: search value
        """
        self.search_input.clear()
        self.search_input.send_keys(value)
        self.search_button.click()

    @allure.step('Go to login page')
    def go_to_login_page(self):
        """Verification of Login page availability """
        self.account_link.click()
        self.login_link.click()

    @allure.step('Verify styles of Cart button')
    def check_cart_button_css(self):
        """Verification of styles for Cart button without hover"""
        lst = []
        with allure.step('Get element styles'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border-top-color', 'border-right-color', 'border-bottom-color',
                         'border-left-color', 'border-radius', 'cursor']:
                lst.append(self.cart_button.value_of_css_property(prop))
        with allure.step(f'Verify font {SIZES.SIZE_12}'):
            assert lst[0] == SIZES.SIZE_12, f'Text size - {lst[0]}'
        with allure.step(f'Verify line spacing interval {SIZES.SIZE_18}'):
            assert lst[1] == SIZES.SIZE_18, f'Line spacing interval - {lst[1]}'
        with allure.step(f'Verify text color {Colors.WHITE}'):
            assert lst[2] == Colors.WHITE, f'Text color - {lst[2]}'
        with allure.step(f'Verify background color {Colors.DARK_GRAY}'):
            assert lst[3] == Colors.DARK_GRAY, f'Background color - {lst[3]}'
        with allure.step(f'Verify background image {Gradients.LIGHT_BLACK}'):
            assert lst[4] == Gradients.LIGHT_BLACK, f'Background image - {lst[4]}'
        with allure.step(f'Verify color of upper border {Colors.LIGHT_BLACK}'):
            assert lst[5] == Colors.LIGHT_BLACK, f'Color of upper border - {lst[5]}'
        with allure.step(f'Verify color of right border {Colors.LIGHT_BLACK}'):
            assert lst[6] == Colors.LIGHT_BLACK, f'Color of right border - {lst[6]}'
        with allure.step(f'Verify color of bottom border {Colors.BLACK}'):
            assert lst[7] == Colors.BLACK, f'Color of bottom border - {lst[7]}'
        with allure.step(f'Verify color of left border {Colors.LIGHT_BLACK}'):
            assert lst[8] == Colors.LIGHT_BLACK, f'Color of left border - {lst[8]}'
        with allure.step(f'Verify radius {SIZES.SIZE_4}'):
            assert lst[9] == SIZES.SIZE_4, f'Radius - {lst[9]}'
        with allure.step(f'Verify cursor {Cursor.POINTER}'):
            assert lst[10] == Cursor.POINTER, f'Cursor - {lst[10]}'

    @allure.step('Verify styles of Cart button with hover')
    def check_cart_button_css_hover(self):
        """Verification of styles for Cart button with hover"""
        ActionChains(self.browser).move_to_element(self.cart_button).perform()
        lst = []
        with allure.step('Get element styles'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border-top-color', 'border-right-color', 'border-bottom-color',
                         'border-left-color', 'border-radius', 'cursor']:
                lst.append(self.cart_button.value_of_css_property(prop))
        with allure.step(f'Verify font {SIZES.SIZE_12}'):
            assert lst[0] == SIZES.SIZE_12, f'Text size - {lst[0]}'
        with allure.step(f'Verify line spacing interval {SIZES.SIZE_18}'):
            assert lst[1] == SIZES.SIZE_18, f'Line spacing interval - {lst[1]}'
        with allure.step(f'Verify text color {Colors.WHITE}'):
            assert lst[2] == Colors.WHITE, f'Text color - {lst[2]}'
        with allure.step(f'Verify background color {Colors.LIGHT_BLACK}'):
            assert lst[3] == Colors.LIGHT_BLACK, f'Background color - {lst[3]}'
        with allure.step(f'Verify background image {Gradients.MEDIUM_BLACK}'):
            assert lst[4] == Gradients.MEDIUM_BLACK, f'Background image - {lst[4]}'
        with allure.step(f'Verify color of upper border {Colors.LIGHT_BLACK}'):
            assert lst[5] == Colors.LIGHT_BLACK, f'Color of upper border - {lst[5]}'
        with allure.step(f'Verify color of right border {Colors.LIGHT_BLACK}'):
            assert lst[6] == Colors.LIGHT_BLACK, f'Color of right border - {lst[6]}'
        with allure.step(f'Verify color of bottom border {Colors.BLACK}'):
            assert lst[7] == Colors.BLACK, f'Color of bottom border - {lst[7]}'
        with allure.step(f'Verify color of left border {Colors.LIGHT_BLACK}'):
            assert lst[8] == Colors.LIGHT_BLACK, f'Color of left border - {lst[8]}'
        with allure.step(f'Verify radius {SIZES.SIZE_4}'):
            assert lst[9] == SIZES.SIZE_4, f'Radius - {lst[9]}'
        with allure.step(f'Verify cursor {Cursor.POINTER}'):
            assert lst[10] == Cursor.POINTER, f'Cursor - {lst[10]}'

    @allure.step('Verify styles of Cart button on click')
    def check_cart_button_css_click(self):
        """Verification of styles for Cart button on click"""
        self.cart_button.click()
        lst = []
        with allure.step('Get element styles'):
            for prop in ['font-size', 'line-height', 'color', 'background-color', 'background-image',
                         'border', 'border-radius', 'cursor']:
                lst.append(self.cart_button.value_of_css_property(prop))
        with allure.step(f'Verify font {SIZES.SIZE_12}'):
            assert lst[0] == SIZES.SIZE_12, f'Text size - {lst[0]}'
        with allure.step(f'Verify line spacing interval {SIZES.SIZE_18}'):
            assert lst[1] == SIZES.SIZE_18, f'Line spacing interval - {lst[1]}'
        with allure.step(f'Verify text color {Colors.MEDIUM_GRAY}'):
            assert lst[2] == Colors.MEDIUM_GRAY, f'Text color - {lst[2]}'
        with allure.step(f'Verify background color {Colors.WHITE}'):
            assert lst[3] == Colors.WHITE, f'Background color - {lst[3]}'
        with allure.step(f'Verify background image - none'):
            assert lst[4] == 'none', f'Background image - {lst[4]}'
        with allure.step(f'Verify style of frame {Border.LIGHT_GRAY}'):
            assert lst[5] == Border.LIGHT_GRAY, f'Frame - {lst[5]}'
        with allure.step(f'Verify radius {SIZES.SIZE_4}'):
            assert lst[6] == SIZES.SIZE_4, f'Radius - {lst[6]}'
        with allure.step(f'Verify cursor {Cursor.POINTER}'):
            assert lst[7] == Cursor.POINTER, f'Cursor - {lst[7]}'
        with allure.step('Verify that dropdown opened'):
            attach(self.browser)
            assert self.check_cart_button_dropdown_open() == 'true', 'Dropdown is not open'

    def check_cart_button_dropdown_open(self):
        """Verification of dropdown display for the Cart button"""
        return self.cart_button.get_attribute('aria-expanded')

    @allure.step('Click on dropdown list with currencies')
    def click_on_currency_drop_down(self):
        """Click on the list with currencies to make sure that dropdown is expanded"""
        self.currency_dropdown_button.click()
        display_css = self.currency_dropdown.value_of_css_property('display')
        with allure.step(f'Verify value of attribute {display_css} - block'):
            attach(self.browser)
            assert display_css == 'block', f'Value of attribute - {display_css}'

    @allure.step('Verify currencies values in dropdown list')
    def check_currency_values(self, lst):
        """Verify currency values

        :param lst: list with name of currencies
        """
        names = [i.text for i in self.currency_dropdown_values]
        for i in names:
            with allure.step(f'Verify that name {i} is in {lst}'):
                attach(self.browser)
                assert i in lst, f'Actual result - {names}, Expected result - {lst}'

    @allure.step('Select currency {value}')
    def choose_currency(self, value):
        """Currency selection.

        :param value: currency value
        """
        self.click_on_currency_drop_down()
        for i in range(len(self.currency_dropdown_values)):
            element = self.currency_dropdown_value(i).text
            if element == value:
                with allure.step(f'Click on currency {value}'):
                    self.currency_dropdown_value(i).click()
