from selenium.webdriver.common.by import By


class AlertsLocators:
    """Locators: Alerts"""

    LINK_LOGIN_ALERT = (By.CSS_SELECTOR, 'i + a')
    LINK_ALERT = (By.CSS_SELECTOR, 'a + a')
    DANGER_ALERT = (By.CSS_SELECTOR, '.alert.alert-danger.alert-dismissible')
    SUCCESS_ALERT = (By.CSS_SELECTOR, 'div.alert-success')


class HeaderPageLocators:
    """Locators: Header"""

    SEARCH_INPUT = (By.NAME, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
    LOGO = (By.CSS_SELECTOR, '#logo > a')
    MENU = (By.CSS_SELECTOR, '.navbar-collapse')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart > button.btn-block')
    TOP_LINKS = (By.ID, 'top-links')
    SEARCH_FIELD = (By.ID, 'search')
    MY_ACCOUNT_LINK = (By.XPATH, '//a[@title = "My Account"]')
    LOGIN_LINK = (By.XPATH, '//a[text() = "Login"]')
    CURRENCY_DROP_DOWN_BUTTON = (By.CSS_SELECTOR, '.pull-left button.dropdown-toggle')
    CURRENCY_VALUES_BUTTONS = (By.CSS_SELECTOR, '.pull-left button.dropdown-toggle + ul > li > button')
    CURRENCY_DROP_DONW = (By.CSS_SELECTOR, '.pull-left button.dropdown-toggle + ul')
    DROPDOWN_FOR_DESKTOPS = (By.XPATH, '//a[text()="Desktops"]//following-sibling::div')
    COMPONENTS_FOR_DROPDOWN = (By.XPATH, '//a[text()="Components"]//following-sibling::div')
    LAPTOPS_FOR_DROPDOWN = (By.XPATH, '//a[text()="Laptops & Notebooks"]//following-sibling::div')
    DESKTOPS_IN_MENU = (By.XPATH, '//a[text()="Desktops"]')
    COMPONENTS_IN_MENU = (By.XPATH, '//a[text()="Components"]')
    LAPTOPS_IN_MENU = (By.XPATH, '//a[text()="Laptops & Notebooks"]')


class MainPageLocators:
    """Locators: Base page"""

    BANNER = (By.CSS_SELECTOR, '#content .swiper-viewport:nth-child(1)')
    BANNER_PAGINATION_BULLETS = (
        By.CSS_SELECTOR, '.swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets')
    HEADER_FEATURED = (By.TAG_NAME, 'h3')
    CAROUSEL_BRAND = (By.CSS_SELECTOR, '#carousel0.swiper-container-horizontal')
    CAROUSEL_PAGINATION_BULLETS = (
        By.CSS_SELECTOR, '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets')
    CAROUSEL_PAGINATION_BULLET = (
        By.CSS_SELECTOR, '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets > .swiper-pagination-bullet')
    BANNER_MACBOOK = (By.XPATH, '//div[contains(@class, "swiper-slide-active")]/img[@alt="MacBookAir"]')
    BANNER_IPHONE = (By.XPATH, '//div[contains(@class, "swiper-slide-active")]/a/img[@alt="iPhone 6"]')
    BANNER_BULLET = (By.CSS_SELECTOR, 'div.slideshow0 > span.swiper-pagination-bullet')
    FEATURED_PRODUCT_LINK = (By.CSS_SELECTOR, 'h3 + div.row > div > div > div.image > a')
    FEATURED_PRODUCT_NAME = (By.CSS_SELECTOR, 'h3 + div.row > div > div > div.image +  div.caption > h4 > a')
    BRAND_IMAGE_IN_CAROUSEL = (By.CSS_SELECTOR, '#carousel0 .swiper-slide')


class ProductPageLocators:
    """Locators: Product page"""

    PRODUCT_HEADER = (By.CSS_SELECTOR, '.btn-group + h1')
    BUTTON_CART = (By.CSS_SELECTOR, '#product > div > #button-cart')
    IMAGES_BLOCK = (By.CLASS_NAME, 'thumbnails')
    RATING_BLOCK = (By.CLASS_NAME, 'rating')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, '#tab-description > p')
    MAIN_PRODUCT_IMAGE = (By.XPATH, '//ul[@class="thumbnails"]/li[1]')
    PRODUCT_IMAGE_IN_WINDOW = (By.CSS_SELECTOR, '.mfp-figure')
    TAB_CLASS = (By.XPATH, '//ul[@class="nav nav-tabs"]/li')
    TAB_DESCRIPTION_LINK = (By.XPATH, '//a[@href="#tab-description"]')
    TAB_SPECIFICATION_LINK = (By.XPATH, '//a[@href="#tab-specification"]')
    TAB_REVIEWS_LINK = (By.XPATH, '//a[@href="#tab-review"]')
    ITEM_TITLE = (By.CSS_SELECTOR, '.col-sm-4 > .btn-group + h1')
    WISH_LIST_BUTTON = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    COMPARE_BUTTON = (By.XPATH, '//div[@class="btn-group"]/button[@data-original-title="Compare this Product"]')
    WRITE_REVIEW_BUTTON = (By.XPATH, '//a[text()="Write a review"]')
    REVIEW_NAME_FIELD = (By.ID, 'input-name')
    REVIEW_FIELD = (By.ID, 'input-review')
    RATING_RADIO_BUTTON = (By.NAME, 'rating')
    REVIEW_BUTTON = (By.CSS_SELECTOR, 'div.pull-right > #button-review')
    RIGHT_BLOCK_INFO = (By.XPATH, '//div[@class="col-sm-4"]/ul[@class="list-unstyled"]')
    ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST = (By.XPATH, '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][1]/li')
    ELEMENTS_OF_RIGHT_BLOCK_INFO_SECOND = (By.XPATH, '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][2]/li')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][2]/li/h2')


class AdminPageLocators:
    """Locators: Admin page"""

    PANEL_HEADING = (By.CLASS_NAME, 'panel-heading')
    USERNAME_INPUT = (By.ID, 'input-username')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    HELP_BLOCK = (By.CLASS_NAME, 'help-block')
    NEED_LOGIN_TEXT = (By.XPATH, '//h1[contains(text(), "enter your login")]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.nav > li:nth-child(2) > a')
    LEFT_MENU_CATALOGUE = (By.CSS_SELECTOR, '#menu-catalog > a')
    LEFT_MENU_PRODUCTS = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) > a')
    PRODUCTS_TABLE = (By.CSS_SELECTOR, '.table-responsive')


class FooterPageLocators:
    """Locators: Footer"""

    LINKS = (By.CSS_SELECTOR, 'footer div.col-sm-3 > ul.list-unstyled > li > a')
