import pytest
from selenium.common import TimeoutException

from pages.home_page import HomePage
from pages.search_page import SearchPage


class TestSearchPage:
    GAMES = {'The Witcher': 10, 'Fallout': 20}

    def setup_method(self, driver):
        self.search_page = SearchPage(self.driver)
        self.home_page = HomePage(self.driver)

    @pytest.mark.parametrize('game', GAMES.keys())
    def test_search_page_sort_by_descending_price(self, game):
        self.home_page.open_page()
        try:
            assert self.home_page.checking_the_page_opening()
        except TimeoutException:
            raise AssertionError(f'Loading time exceeded for {self.home_page.PAGE_URL}')
        self.home_page.search_game(game)
        try:
            assert self.search_page.checking_the_page_opening()
        except TimeoutException:
            raise AssertionError(f'Loading time exceeded for {self.search_page.PAGE_URL}')
        items = self.search_page.sort_games_by_descending_price(self.GAMES[game])
        games_list = []
        for item in items:
            games_list.append(int(item.get_attribute('data-price-final')))
        assert all([x >= y for x, y in zip(games_list, games_list[1:])]), f'sorting for {game} is not descending'
