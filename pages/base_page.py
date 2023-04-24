import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from helpers import allure_helper
from helpers.waits import Element, Elements, Clickable

from pages.common.alert import Alert
from pages.common.footer import Footer
from pages.common.header import Header


class BasePage:
    def __init__(self, browser, url, db_connection=None, wait=10):
        """
        :param browser: fixture to run driver
        :param url: fixture with resource URL
        :param db_connection: fixture to connect to BD
        """
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, wait)
        self.db_connection = db_connection
        self.alert = Alert(self.browser)
        self.footer = Footer(self.browser)
        self.header = Header(self.browser)

    def open_url(self, path='/'):
        """
        :param path: path
        """
        with allure.step(f'Go to link {self.url}{path}'):
            return self.browser.get(f'{self.url}{path}')

    @allure.step('Find a element by locator {locator} and path {el_path}, index {index}')
    def _element(self, locator, el_path, index=0, all=False):
        """Returns search result by elements after waiting

        :param locator: locator type
        :param el_path: path to element
        :param index: element index
        :param all: marker for single or multiple element/s search
        """
        try:
            if all:
                return self.wait.until(Elements(locator, el_path))
            return self.wait.until(Element(locator, el_path, index))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Element with locator {locator} is not found, by path {el_path} and index {index}')

    @allure.step('Verify that Element {locator}, {el_path} with index {index} is displayed on the page')
    def is_element_visible(self, locator, el_path, index=0):
        """Returns the result of waiting for element visibility

        :param locator: locator type
        :param el_path: path to element
        :param index: element index
        """
        element = self._element(locator, el_path, index)
        try:
            assert element.is_displayed()
        except AssertionError:
            allure_helper.attach(self.browser)
            f'Element {locator} {el_path} {index} is not displayed on the page'

    @allure.step('Click on Element with locator {locator}, by path {el_path} and index {index}')
    def click_on_element(self, locator, el_path, index=0):
        """Returns click on the found element

        :param locator: locator type
        :param el_path: path to element
        :param index: element index
        """
        element = self._element(locator, el_path, index)
        try:
            self.wait.until(Clickable(element))
            return element.click()
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Could not click on element {locator} {el_path} {index}')

    @allure.step('Get Element text with locator {locator}, by path {el_path} and index {index}')
    def get_text_of_element(self, locator, el_path, index=0):
        """Returns text of the found element

        :param locator: locator type
        :param el_path: path to element
        :param index: element index
        """
        element = self._element(locator, el_path, index)
        try:
            return element.text
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Could not get element text {locator} {el_path} {index}')

    @allure.step('Verify that Title {title} is correct')
    def is_title_correct(self, title):
        """Verification of page title"""
        try:
            return self.wait.until(EC.title_is(title))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Title is not matching: {self.browser.title}, expected {title}')

    @allure.step('Get page title')
    def get_title(self):
        """Returns page title"""
        try:
            return self.browser.title
        except Exception as e:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Could not receive title of page')

    @allure.step('Find dropdown by path {el_path}')
    def select_products(self, locator, el_path, index=0):
        """Returns found dropdown list

        :param locator: locator type
        :param el_path: path to element
        :param index: element index
        """
        try:
            return Select(self._element(locator, el_path, index))
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Dropdown list with locator {locator} is not found, by path {el_path} and index {index}')

    @allure.step('Get attribute {attr} for element {el_path} with index {index}')
    def getting_attr(self, attr, locator, el_path, index=0):
        """Returns attribute for found element

        :param locator: locator type
        :param el_path: path to element
        :param attr: element attribute
        :param index: element index
        """
        element = self._element(locator, el_path, index)
        try:
            return element.get_attribute(attr)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Element {locator} {el_path} {index} does not have an attribute {attr}')

    @allure.step('Enter text {value} in input {el_path} with index {index}')
    def input_text(self, locator, el_path, value, index=0):
        """Возвращает ввод текста в найденный инпут.

        :param locator: locator type
        :param el_path: path to element
        :param value: value for input
        :param index: element index
        """
        element = self._element(locator, el_path, index)
        try:
            element.clear()
            return element.send_keys(value)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Could not enter text {value} in element {locator} {el_path} {index}')

    @allure.step('Scroll until {el} element')
    def scroll_to_element(self, el):
        """Returns scroll for element"""
        try:
            return self.browser.execute_script('return arguments[0].scrollIntoView(true);', el)
        except Exception as e:
            raise AssertionError(f'Error {e}')

    @allure.step('Get css property {css_property} for element {locator} {el_path} with index {index}')
    def get_css_property(self, locator, el_path, css_property, index=0):
        """Returns value for css property of the found element.

        :param locator: locator type
        :param el_path: path to element
        :param css_property: css property
        :param index: element index
        """
        element = self._element(locator, el_path, index)
        try:
            return element.value_of_css_property(css_property)
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Element {locator} {el_path} {index} does not have css property {css_property}')

    @allure.step('Move cursor on element {locator} {el_path} with index {index}')
    def mouse_move_to_element(self, locator, el_path, index=0):
        """Moves cursor on element

        :param locator: locator type
        :param el_path: path to element
        :param index: element index
        """
        element = self._element(locator, el_path, index)
        try:
            return ActionChains(self.browser).move_to_element(element).perform()
        except TimeoutException:
            allure_helper.attach(self.browser)
            raise AssertionError(f'Could not move cursor on element {locator} {el_path} {index}')
