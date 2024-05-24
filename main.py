import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import unittest

from src import (
    GetSeleniumEdge, 
    Config, 
    PageManager
)


class TestPage(PageManager):
    def __init__(self) -> None:
        self.driver = GetSeleniumEdge()
        self.driver.get(Config.BASE_URL)
        self.item = self.open_item
    
    def enter_url(self):
        return self.open_link()
    
    def enter_query(self):
        return self.search()
    
    def enter_item(self):
        return self.item()
    
    def get_price(self):
        return self.price()
    
    def get_reviews(self):
        return self.reviews()
    
    def screenshot(self, name):
        self.screenshots(name)
    

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pg = TestPage()

    def tearDown(self):
        test_name = self._testMethodName
        errors = self._outcome.errors
        for i, (test, exc_info) in enumerate(errors):
            if exc_info is not None:
                print(f"Error in test: {test_name}")
                print(f"Error details: {exc_info[1]}")
                self.pg.screenshot(test_name)

    def test_0(self):
        result = self.pg.enter_url()
        self.assertEqual(result, "https://megamarket.ru/")

    def test_1(self):
        result = self.pg.enter_query()
        self.assertEqual(result.lower(), "смарт-часы")

    def test_2(self):
        outer_name, inner_name = list(self.pg.enter_item())
        self.assertEqual(outer_name, inner_name)
    
    def test_3(self):
        result = self.pg.get_price()
        self.assertTrue(result is not None)

    def test_4(self):
        result = self.pg.get_reviews()
        self.assertTrue(result != 0)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
