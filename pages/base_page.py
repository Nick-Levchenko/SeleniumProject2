from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    def checking_the_page_opening(self):
        return self.wait.until(EC.visibility_of_element_located(self.PAGE_LOADING_ELEMENT))
