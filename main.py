from datetime import datetime as dt

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
    
    def open_schedule(self):
        return self.schedule()

    def open_search_schedule(self):
        return self.watch_on_site_schedule()

    def set_group(self):
        return self.set_groups()
    
    def click_to_group(self):
        return self.click_to_groups()

    def get_green_day(self):
        return self.current_day()
    
    def screenshot(self, num_test: str):
        self.screenshots(num_test)


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
        result = self.pg.click_to_group()
        self.assertEqual(result, "221-323")
    
    def test_5(self):
        days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]
        cur_day = dt.today().weekday()
        result = self.pg.get_green_day()
        if cur_day == 6:
            self.assertEqual(result, None)
        else:
            self.assertEqual(result, days[cur_day])


if __name__ == '__main__':
    unittest.main(warnings='ignore')
