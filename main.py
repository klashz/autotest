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


class TestPage(PageManager):
    def __init__(self) -> None:
        self.driver = GetSeleniumEdge()
        self.driver.get(Config.BASE_URL)
    
    def __call__(self):
        # time.sleep(10)
        result_catalog = self.open_catalog()
        print(result_catalog)
        time.sleep(3)

        result_category = self.select_category()
        print(result_category)
        result_xbox = self.select_xbox()
        print(result_xbox)
        result_subcategory = self.select_subcategory()
        print(result_subcategory)
        result_list = self.select_list()
        print(result_list)   
    
    # def open_schedule(self):
    #     return self.self.schedule(self.driver)

    # def open_search_schedule(self):
    #     return self.self.watch_on_site_schedule(self.driver)

    # def set_group(self):
    #     return self.self.set_groups(self.driver)
    
    # def click_to_groups(self):
    #     return self.self.click_to_groups(self.driver)
    
    # def screenshot(self, num_test: str):
    #     self.self.screenshot(self.driver, num_test)

pg = TestPage()
pg()

# class TestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.pg = TestPage()

#     def tearDown(self):
#         test_name = self._testMethodName
#         errors = self._outcome.errors
#         for i, (test, exc_info) in enumerate(errors):
#             if exc_info is not None:
#                 print(f"Error in test: {test_name}")
#                 print(f"Error details: {exc_info[1]}")
#                 self.pg.screenshot(test_name)

    # def test_1(self):
    #     result = self.pg.open_schedule()
    #     self.assertEqual(result, "https://mospolytech.ru/obuchauschimsya/raspisaniya/")

    # def test_2(self):
    #     result = self.pg.open_search_schedule()
    #     self.assertEqual(result, "https://rasp.dmami.ru/")

    # def test_3(self):
    #     result = self.pg.set_group()
    #     self.assertEqual(result, "221-323")

    # def test_4(self):
    #     result = self.pg.click_to_groups()
    #     self.assertEqual(result, "221-323")


# if __name__ == '__main__':
    # unittest.main(warnings='ignore')
