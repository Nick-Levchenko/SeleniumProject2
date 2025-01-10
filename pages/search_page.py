from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchPage(BasePage):
    PAGE_URL = 'https://store.steampowered.com/search/?term='
    PAGE_LOADING_ELEMENT = (By.XPATH, "//*[@data-gpnav='item']")
    SORTING_FILTER = (By.XPATH, "//*[@id='sort_by_trigger']")
    DECREASING_PRICE_FILTER = (By.XPATH, "//*[@id='Price_DESC']")
    FIRST_ITEM = (By.XPATH, "//*[@data-price-final and @data-bundlediscount]")


    def __init__(self, driver):
        super().__init__(driver)

    def sort_games_by_descending_price(self, number):
        first_n_games = (By.XPATH, f"(//*[@data-price-final and @data-bundlediscount])[position()<{number + 1}]")
        first_item = self.wait.until(EC.visibility_of_element_located(self.FIRST_ITEM))
        self.wait.until(EC.element_to_be_clickable(self.SORTING_FILTER)).click()
        self.wait.until(EC.element_to_be_clickable(self.DECREASING_PRICE_FILTER)).click()
        self.wait.until(EC.staleness_of(first_item))
        first_items = self.wait.until(EC.presence_of_all_elements_located(first_n_games))
        return first_items
