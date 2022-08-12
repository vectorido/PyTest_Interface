import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ...")
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose your destiny. I mean... choose your web browser")


@pytest.fixture(scope="function")
def browser(request):
    browser = None
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if language in ("es", "en", "ru", "fr", "it"):
        if browser_name == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            browser = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be firefox or chrome. The best or nothing")
    else:
        raise pytest.UsageError("--language should be existing and pretty popular")
    yield browser
    print("\nquit browser..")
    time.sleep(30)
    browser.quit()
