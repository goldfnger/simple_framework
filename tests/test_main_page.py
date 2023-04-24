import allure
import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage


@allure.feature('Main page')
@pytest.mark.main_page
class TestMainPage:

    @allure.story('Page elements')
    @allure.title('Verify visibility of elements on the page')
    @allure.link('#', name='User story')
    def test_visibility_of_elements_on_main_page(self, browser, url):
        """ Test case for verification visibility of elements on the Main page.

        :param browser: browser fixture
        :param url: url fixture
        """
        page = MainPage(browser, url)
        page.open_url()
        page.check_elements_visibility()

    @allure.story('Page elements')
    @allure.title('Verify page title')
    @allure.link('#', name='User story')
    def test_check_title_on_main_page(self, browser, url):
        """Test case to make sure that tittle of main page is correct.

        :param browser: browser fixture
        :param url: url fixture
        """
        page = MainPage(browser, url)
        page.open_url()
        page.is_title_correct('Your Store')

    @allure.story('Verify banner rotation')
    @allure.title('Verify banner rotation on bullet click')
    @allure.link('#', name='User story')
    def test_banners_rotation(self, browser, url):
        """Test case to verify banners rotation

        :param browser: browser fixture
        :param url: url fixture
        """
        page = MainPage(browser, url)
        page.open_url()
        page.click_banner_bullet_active()
        page.click_banner_bullet_inactive()

    @allure.story('Go to other pages')
    @allure.title('Open the product with index {idx} from Featured')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('idx', [0, 1])
    def test_go_to_product_from_featured(self, browser, url, idx):
        """Test case to verify product opening on click from Featured block

        :param browser: browser fixture
        :param url: url fixture
        :param idx: element index
        """
        page = MainPage(browser, url)
        page.open_url()
        name = page.go_to_product_from_featured(idx)
        product_page = ProductPage(browser, browser.current_url)
        product_page.compare_item_title_on_pages(name)

    @allure.story('Verify banners and carousels rotation')
    @allure.title('Verify brands rotation in carousel on button click')
    @allure.link('#', name='User story')
    def test_carousel_rotation(self, browser, url):
        """Test case to verify brands rotation in carousel on button click

        :param browser: browser fixture
        :param url: url fixture
        """
        page = MainPage(browser, url)
        page.open_url()
        page.click_carousel_bullet()
