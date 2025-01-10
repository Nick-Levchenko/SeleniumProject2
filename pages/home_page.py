from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    PAGE_URL = 'https://store.steampowered.com/'
    PAGE_LOADING_ELEMENT = (By.XPATH, "//*[@id='foryou_tab']")
    SEARCH_FIELD = (By.XPATH, "//*[@id='store_nav_search_term']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='store_search_link']//img")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def search_game(self, game):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD)).send_keys(game)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
