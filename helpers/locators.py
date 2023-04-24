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
