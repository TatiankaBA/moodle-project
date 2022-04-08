import pytest
from selenium import webdriver
from os import getenv
from selenium.webdriver.chrome.options import Options
import os


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action='store_true', 
                     help="Run driver in headless mode.")


@pytest.fixture()
def chrome_options(request, chrome_options):
    if not request.config.getoption("--headless"):
        
        chrome_options.add_argument("--window-size=2560,1440")
        # any other config values to be ran when not headless
    else:
        chrome_options.add_argument("--headless")
        # any other config values to be ran when headless
    return chrome_options

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome" and not request.config.getoption("--headless"):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(20)

    elif browser_name == "chrome" and request.config.getoption("--headless"):
        print("\nstart browser for test..")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.implicitly_wait(20)
    
    elif browser_name == "firefox" and not request.config.getoption("--headless"):
        print("\nstart browser for test..")
        browser = webdriver.Firefox()
        browser.implicitly_wait(20)


    elif browser_name == "firefox" and request.config.getoption("--headless"):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        browser = webdriver.Firefox(firefox_options=fireFoxOptions)
        browser.implicitly_wait(20)

    
    yield browser
    print("\nquit browser..")
    browser.quit()
