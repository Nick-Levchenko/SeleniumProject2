from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchPage(BasePage):
    PAGE_LOADING_ELEMENT = (By.XPATH, "//*[@data-gpnav='item']")
    SORTING_FILTER = (By.ID, "sort_by_trigger")
    DECREASING_PRICE_FILTER = (By.ID, "Price_DESC")
    FIRST_ITEM = (By.XPATH, "//*[@data-ds-itemkey]")
    FIRST_ITEMS = f"(//*[@data-price-final and @data-bundlediscount])"

    def __str__(self):
        return "Search Page"

    def sort_games_by_descending_price(self):
        first_item = self.wait.until(EC.visibility_of_element_located(self.FIRST_ITEM))
        self.wait.until(EC.element_to_be_clickable(self.SORTING_FILTER)).click()
        self.wait.until(EC.element_to_be_clickable(self.DECREASING_PRICE_FILTER)).click()
        self.wait.until(EC.staleness_of(first_item))

    def take_first_elements(self, number_of_elements):
        quantity_of_elements = f"[position()<{number_of_elements + 1}]"
        first_items = self.FIRST_ITEMS + quantity_of_elements
        get_first_items = (By.XPATH, first_items)
        result_items = self.wait.until(EC.presence_of_all_elements_located(get_first_items))
        return result_items
