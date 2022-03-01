import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Set language for browser")


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    driver = None
    if browser_lang is None:
        raise pytest.UsageError("need --language")
    else:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
