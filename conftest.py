import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser) -> None:
    parser.addoption('--language', action='store', default='en',
                     help="Choose site language. Default: en")
    parser.addoption('--browser', action='store', default='Chrome',
                     help="Choose browser for tests Chrome/Firefox. Default: Chrome")


@pytest.fixture(scope="function")
def browser(request) -> None:
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    browser = None
    browser_name = str(request.config.getoption("browser")).lower()
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome("./chromedriver", options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox("./geckodriver", options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
