import time
from collections import Counter

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import unittest

from src import (
    GetSeleniumEdge, 
    Config, 
    PageManager
)


class TestPage:
    def __init__(self) -> None:
        self.manager = PageManager()
        self.driver = GetSeleniumEdge()
        self.driver.get(Config.BASE_URL)
    
    def open_schedule(self):
        return self.manager.schedule(self.driver)

    def open_search_schedule(self):
        return self.manager.watch_on_site_schedule(self.driver)

    def set_group(self):
        return self.manager.set_groups(self.driver)
    
    def click_to_groups(self):
        return self.manager.click_to_groups(self.driver)
    
    def screenshot(self, num_test: str):
        self.manager.screenshot(self.driver, num_test)


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

    def test_1(self):
        result = self.pg.open_schedule()
        self.assertEqual(result, "https://mospolytech.ru/obuchauschimsya/raspisaniya/")

    def test_2(self):
        result = self.pg.open_search_schedule()
        self.assertEqual(result, "https://rasp.dmami.ru/")

    def test_3(self):
        result = self.pg.set_group()
        self.assertEqual(result, "221-323")

    def test_4(self):
        result = self.pg.click_to_groups()
        self.assertEqual(result, "221-323")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
