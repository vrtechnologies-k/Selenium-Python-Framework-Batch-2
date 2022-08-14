import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome", help="Executing My Tests on Different Browsers"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("--browser-name")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Ie()

    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
