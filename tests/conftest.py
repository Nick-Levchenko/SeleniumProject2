import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import ConfigReader

config = ConfigReader()
class Chrome(webdriver.Chrome):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


@pytest.fixture
def driver():
    options = Options()
    options.add_argument(config.read_config('max_window_size'))
    driver = Chrome(options=options)
    driver.get(config.read_config('url'))
    yield driver
    driver.quit()
