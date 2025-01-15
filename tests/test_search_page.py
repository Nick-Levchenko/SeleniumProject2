import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage

from conftest import driver
from utils import ListUtils


class TestSearchPage:
    GAMES = {'The Witcher': 10, 'Fallout': 20}

    @pytest.mark.parametrize("game, count", [(x, y) for x, y in GAMES.items()])
    def test_search_page_sort_by_descending_price(self, game, count, driver):
        sorter = ListUtils()
        search_page = SearchPage(driver)
        home_page = HomePage(driver)
        home_page.wait_page_opening()
        home_page.search_game(game)
        search_page.wait_page_opening()
        search_page.sort_games_by_descending_price()
        games_list = search_page.take_first_elements(count)
        assert sorter.sorting_by_descending(games_list), f'sorting for {game} is not descending'
