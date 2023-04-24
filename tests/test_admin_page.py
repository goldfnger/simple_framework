import allure
import pytest

from helpers.urls import URLS
from pages.admin_page import AdminPage


@allure.feature('Admin page')
@pytest.mark.admin_page
class TestAdminPage:
    """Admin page test suite."""

    @allure.story('Page elements')
    @allure.title('Verify visibility of elements on the page')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_admin_login_page(self, browser, url):
        """ Test case for verification visibility of elements on the Catalogue page.

        :param browser: browser fixture
        :param url: url fixture
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.check_elements_visibility()

    @allure.story('Admin page authorization')
    @allure.title('Valid credentials')
    @allure.link('#', name='User story')
    def test_login_valid(self, browser, url):
        """Test case for admin login verification with valid credentials.

        :param browser: browser fixture
        :param url: url fixture
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.check_elements_visibility()
        page.login('user', 'bitnami')
        page.is_title_correct('Dashboard')

    @allure.story('Admin page authorization')
    @allure.title('Invalid credentials')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('login, passw',
                             [('test', 'test'), ('123', '')])
    def test_login_failed(self, browser, url, login, passw):
        """Test case for admin login verification with invalid credentials.

        :param browser: browser fixture
        :param url: url fixture
        :param login: user login
        :param passw: user password
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.login(login, passw)
        page.alert.check_danger_alert()

    @allure.story('Admin page logout')
    @allure.title('Admin page logout')
    @allure.link('#', name='User story')
    def test_logout(self, browser, url):
        """Test case for admin logout verification .

        :param browser: browser fixture
        :param url: url fixture
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.login('user', 'bitnami')
        page.logout()
        page.check_successful_logout_text()

    @allure.story('Admin page elements')
    @allure.title('Display of table with products in admin page')
    @allure.link('#', name='User story')
    def test_get_products_table(self, browser, url):
        """Test case for checking the display of a table with products in the admin panel.

        :param browser: browser fixture
        :param url: url fixture
        """
        page = AdminPage(browser, url)
        page.open_url(path=URLS.ADMIN_PAGE)
        page.login('user', 'bitnami')
        page.get_product_table()
        page.check_products_table()
