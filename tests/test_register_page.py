import allure
import pytest

from helpers.db_helper import check_user_in_db, check_user_not_in_db
from helpers.urls import URLS
from pages.account_page import AccountPage
from pages.register_page import RegisterPage


@allure.feature('Registration page')
@pytest.mark.register_page
class TestRegisterPage:

    @allure.story('Page elements')
    @allure.title('Verify visibility of elements on the page')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_register_page(self, browser, url):
        """ Test case for verification visibility of elements on the Registration page.

        :param browser: browser fixture
        :param url: url fixture
        """
        page = RegisterPage(browser, url)
        page.open_url(path=URLS.REGISTER_PAGE)
        page.check_elements_visibility()

    @allure.story('Verify registration of new user')
    @allure.title('Successful registration')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                             [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0),
                              ('User', 'Lastname', 'a1@test.ru', '11111111', '12345', '12345', 1)])
    def test_success_register_new_user(
            self, browser, url, db_connection, firstname, lastname, email, tel, password, confirm, radio_idx):
        """Test case to make sure that new user is successfully registered.

            :param browser: browser fixture
            :param url: url fixture
            :param db_connection: DB connection fixture
            :param firstname: username
            :param lastname: lastname
            :param email: user email
            :param tel: user phone
            :param password: user password
            :param confirm: user confirm password
            :param radio_idx: newsletter agreement
            """
        page = RegisterPage(browser, url)
        page.open_url(path=URLS.REGISTER_PAGE)
        page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx)
        account_page = AccountPage(browser, browser.current_url)
        account_page.is_title_correct('Your Account Has Been Created!')
        check_user_in_db(db_connection, firstname, lastname, email, tel, radio_idx)

    @allure.story('Verify registration of new user')
    @allure.title('Empty fields')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx',
                             [(None, 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0),
                              ('Test1', None, 'test@test12.com', '89991112233', 'test', 'test', 0),
                              ('Test1', 'Test2', None, '89991112233', 'test', 'test', 0),
                              ('Test1', 'Test2', 'test@test12.com', None, 'test', 'test', 0),
                              ('Test1', 'Test2', 'test@test12.com', '89991112233', None, 'test', 0),
                              ('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', None, 0)])
    def test_register_new_user_empty_fields(
            self, browser, url, db_connection, firstname, lastname, email, tel, password, confirm, radio_idx):
        """Test case to verify new user registration - empty fields.

            :param browser: browser fixture
            :param url: url fixture
            :param db_connection: DB connection fixture
            :param firstname: username
            :param lastname: lastname
            :param email: user email
            :param tel: user phone
            :param password: user password
            :param confirm: user confirm password
            :param radio_idx: newsletter agreement
            """
        page = RegisterPage(browser, url)
        page.open_url(path=URLS.REGISTER_PAGE)
        page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx)
        page_after_register = RegisterPage(browser, browser.current_url)
        page_after_register.is_title_correct('Register Account')
        if not email:
            check_user_not_in_db(db_connection, firstname=firstname, lastname=lastname, tel=tel)
            page_after_register.check_fail_register_without_email()
        else:
            check_user_not_in_db(db_connection, email)
            if not firstname:
                page_after_register.check_fail_register_without_firstname()
            if not lastname:
                page_after_register.check_fail_register_without_lastname()
            if not tel:
                page_after_register.check_fail_register_without_telephone()
            if not password:
                page_after_register.check_fail_register_without_password()
            if not confirm:
                page_after_register.check_fail_register_without_confirm()

    @allure.story('Verify registration of new user')
    @allure.title('Privacy policy is not accepted')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('firstname, lastname, email, tel, password, confirm, radio_idx, privacy',
                             [('Test1', 'Test2', 'test@test12.com', '89991112233', 'test', 'test', 0, False)])
    def test_register_new_user_without_accept_privacy_policy(
            self, browser, url, db_connection, firstname, lastname, email, tel, password, confirm, radio_idx, privacy):
        """Test case to verify new user registration - privacy policy is not accepted.

            :param browser: browser fixture
            :param url: url fixture
            :param db_connection: DB connection fixture
            :param firstname: username
            :param lastname: lastname
            :param email: user email
            :param tel: user phone
            :param password: user password
            :param confirm: user confirm password
            :param radio_idx: newsletter agreement
            :param privacy: privacy policy check box
            """
        page = RegisterPage(browser, url)
        page.open_url(path=URLS.REGISTER_PAGE)
        page.register_user(
            firstname, lastname, email, tel, password, confirm, radio_idx, privacy)
        page_after_register = RegisterPage(browser, browser.current_url)
        page_after_register.is_title_correct('Register Account')
        check_user_not_in_db(db_connection, email)
        page_after_register.alert.check_error_text('Warning: You must agree to the Privacy Policy!')
