from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import ConfigReader


class BasePage:
    PAGE_LOADING_ELEMENT = None

    def __init__(self, driver):
        self.config = ConfigReader()
        self.driver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, self.config.read_config("timeout"))

    def wait_page_opening(self):
        self.wait.until(EC.visibility_of_element_located(self.PAGE_LOADING_ELEMENT))
