import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=f"C://drivers")
    parser.addoption("--url", default=f"https://stage-v4-frontend.e-credit.one")
    # parser.addoption("--url", default=f"https://stage-v4-frontend.e-credit.one/applications/list")
    parser.addoption("--headless", action="store_true")

@pytest.fixture
def base_url(request):
    base_url = request.config.getoption("--url")
    return base_url

@pytest.fixture
def driver(request):
    service = Service(executable_path=ChromeDriverManager().install())
    browser_name = request.config.getoption("--browser")
    driver_path = request.config.getoption("--drivers")
    options = ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options, executable_path=f"{driver_path}/chromedriver")
    browser.maximize_window()
    request.addfinalizer(browser.close)
    return browser


