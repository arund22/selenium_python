import pytest
from selenium import webdriver
import xlutils


@pytest.fixture(scope="class")
def setUp(request):
    print("Running SetUp for Driver")
    baseurl = "http://the-internet.herokuapp.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def one_time_setup(browser,request):
    print("Running Before test")
    if browser == 'chrome':
        print("Running test of Chrome")
        baseurl = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseurl)
    elif browser == 'firefox':
        print("Running test of Firefox")
        baseurl = "http://automationpractice.com/index.php"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseurl)
    if request.cls is not None:
        request.cls.driver=driver
    yield driver
    print("Tear Down")
    driver.quit()

@pytest.fixture(scope='class')
def module_browser(request):
    """Fixture lasts for an entire file of tests."""
    driver = webdriver.Chrome()
    def fin():
        driver.quit()
    request.addfinalizer(fin())
    return driver

@pytest.fixture(scope='function')
def function_browser(request):
    """Fixture lasts for just a test function."""
    baseurl = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    def fin():
        driver.quit()
    request.addfinalizer(fin())
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of OS")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption('--browser')