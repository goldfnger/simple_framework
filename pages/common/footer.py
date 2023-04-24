import allure
from selenium.webdriver.support.wait import WebDriverWait

from helpers.allure_helper import attach
from helpers.locators import FooterPageLocators
from helpers.waits import Elements


class Footer:
    def __init__(self, browser):
        self.browser = browser

    @property
    def footer_links(self):
        return WebDriverWait(self.browser, 5).until(Elements(*FooterPageLocators.LINKS))

    @allure.step('Verify link in footer')
    def check_footer_links(self, lst):
        """Verification of link in footer.

        :param lst: list of links
        """
        links_text = [i.text for i in self.footer_links]
        with allure.step(f'Verify that links {links_text} matches {lst}'):
            attach(self.browser)
            assert links_text == lst, f'List of links - {links_text}'
