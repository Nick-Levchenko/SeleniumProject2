from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    PAGE_LOADING_ELEMENT = (By.ID, "foryou_tab")
    SEARCH_FIELD = (By.ID, "store_nav_search_term")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='store_search_link']//img")

    def __str__(self):
        return "Home Page"

    def search_game(self, game):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD)).send_keys(game)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
