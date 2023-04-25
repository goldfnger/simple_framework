import allure
import mysql.connector
import pytest
import requests
import time
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOp
from selenium.webdriver.firefox.options import Options as FFOp
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers import allure_helper


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item):
    """Hook to set a test status"""
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def url_data(url_link, timeout=15):
    """Waiting for video availability"""
    while timeout:
        response = requests.get(url_link)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url_link:
                return response.content
            else:
                return response.text
    return None


def pytest_addoption(parser):
    parser.addoption(
        '--url', action='store', default='localhost', help='Set a url for app')
    parser.addoption(
        '--headless', action='store', default=True, help='Run tests in a headless mode by default')
    parser.addoption(
        '--browser-name', action='store', default="chrome", choices=['chrome', 'firefox'],
        help='Set a browser: chrome, firefox')
    parser.addoption(
        '--tester', action='store', required=True, help='Set the name of Tester who execute run')
    parser.addoption(
        '--browser-version', action='store', help='Set a browser version - to run with selenoid')
    parser.addoption(
        '--local', action='store_true',
        help='Set this flag for local run, without flag will run remotely')
    parser.addoption(
        '--executor', action='store',
        help='If --local False - specify selenoid host, if True - skip parameter')


@pytest.fixture
def url(request):
    """Returns URL from commandline"""
    get_url = request.config.getoption('--url')
    return f'http://{get_url}'


@pytest.fixture
def browser(request, db_connection):
    headless = request.config.getoption('--headless')
    browser_name = request.config.getoption('--browser-name')
    browser_version = request.config.getoption('--browser-version')
    executor = request.config.getoption('--executor')
    local = request.config.getoption('--local')
    test_name = request.node.name
    tester_name = request.config.getoption('--tester')

    capabilities = {
        'browserName': browser_name,
        'browserVersion': browser_version,
        'screenResolution': '1920x1080',
        'name': test_name,
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': False}}

    if local:
        if browser_name == 'chrome':
            options = ChOp()
            options.headless = headless
            driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        elif browser_name == 'firefox':
            options = FFOp()
            options.headless = headless
            driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        else:
            raise pytest.UsageError('To run locally --browser_name - chrome or firefox')
        allure_helper.attach_capabilities(driver)
        allure_helper.add_allure_env(browser_name, browser_version, local, tester_name)
        request.addfinalizer(driver.quit)
        driver.maximize_window()
        return driver
    else:
        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub', desired_capabilities=capabilities)
        allure_helper.attach_capabilities(driver)
        allure_helper.add_allure_env(browser_name, browser_version, local, tester_name)

        def finalizer():
            video = f'http://{executor}:8080/video/{driver.session_id}.mp4'
            driver.quit()
            # In case of error attach video to report
            if request.node.status != 'passed':
                allure.attach(
                    name='video_for_' + driver.session_id,
                    body=url_data(video),
                    attachment_type=allure.attachment_type.MP4)
            # Delete video from selenoid
            if url_data(video):
                requests.delete(video)

        request.addfinalizer(finalizer)
        driver.maximize_window()
        return driver


@pytest.fixture(scope='session')
def db_connection(request):
    db_host = request.config.getoption('--url')
    config = SimpleNamespace(
        DB_NAME='bitnami_opencart',
        HOST=db_host,
        PORT='3306',
        USER='bn_opencart',
        PASSWORD=''
    )
    connection = mysql.connector.connect(
        user=config.USER,
        password=config.PASSWORD,
        host=config.HOST,
        port=config.PORT,
        database=config.DB_NAME
    )
    request.addfinalizer(connection.close)
    return connection
