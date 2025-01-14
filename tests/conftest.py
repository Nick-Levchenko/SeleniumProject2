import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Chrome(webdriver.Chrome):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = Chrome(options=options)
    driver.get('https://store.steampowered.com/')
    yield driver
    driver.quit()
