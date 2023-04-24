import allure
from selenium.webdriver.support.wait import WebDriverWait

from helpers.allure_helper import attach
from helpers.locators import AlertsLocators
from helpers.waits import Element


class Alert:
    def __init__(self, browser):
        self.browser = browser

    @property
    def success_alert(self):
        return WebDriverWait(self.browser, 5).until(Element(*AlertsLocators.SUCCESS_ALERT))

    @property
    def danger_alert(self):
        return WebDriverWait(self.browser, 5).until(Element(*AlertsLocators.DANGER_ALERT))

    @allure.step('Verify that alert with error is displayed')
    def check_danger_alert(self):
        """Verification of element visibility"""
        assert self.danger_alert.is_displayed()

    @allure.step('Click on Login button in alert')
    def click_login_from_alert(self):
        """Click on Login button in Alert"""
        self.success_alert.find_element(*AlertsLocators.LINK_LOGIN_ALERT).click()

    @allure.step('Click on button in alert')
    def click_link_from_alert(self):
        """Click on Comparison button in Alert"""
        self.success_alert.find_element(*AlertsLocators.LINK_ALERT).click()

    @allure.step('Verify error message')
    def check_error_text(self, txt):
        """Verify error message"""
        error_text = self.danger_alert.text
        with allure.step(f'Verify that error description - {txt}'):
            attach(self.browser)
            assert error_text == txt, \
                f'Error description {error_text}'

    @allure.step('Verify visibility of successful alert')
    def check_success_alert(self):
        """Display successful Alert"""
        assert self.success_alert.is_displayed()
