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
    
    def open_cat(self):
        result_catalog = self.open_catalog()
        time.sleep(3)
        return result_catalog

    def sel_cat(self):
        result_category = self.select_category()
        return result_category
    
    def sel_xbox(self):
        result_xbox = self.select_xbox()
        return result_xbox
    
    def sel_subcat(self):
        result_subcategory = self.select_subcategory()
        return result_subcategory
    
    def sel_list_and_like(self):
        likes_list, count_blocks = self.select_list()
        result_add = self.select_like(likes_list)
        return result_add

    def sel_favorite(self):
        result_add_favorite = self.select_favorite()
        return result_add_favorite
    
    def displayed_windows(self):
        return self.check_notifications()
    
    def del_favorite(self):
        result_del_favorite = self.delete_favorite()
        return result_del_favorite
    
    def ref_page(self):
        result_refresh_page = self.refresh_page()
        return result_refresh_page
    
    def screenshot(self, name):
        self.screenshots(name)
    
#TODO: add test for check display windows
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
        result = self.pg.open_cat()
        self.assertEqual(result, "Каталог")

    def test_1(self):
        result = self.pg.sel_cat()
        self.assertEqual(result, "https://market.yandex.ru/")

    def test_2(self):
        result = self.pg.sel_xbox()
        self.assertEqual(result, "Xbox")

    def test_3(self):
        result = self.pg.sel_subcat()
        self.assertEqual(result, "Игровые приставки")

    def test_4(self):
        result = self.pg.sel_list_and_like()
        self.assertEqual(result, "Удалить из избранного")
    
    def test_5(self):
        result = self.pg.sel_favorite()
        self.assertEqual(result, "https://market.yandex.ru/my/wishlist?track=head")
    
    def test_6(self):
        result = self.pg.displayed_windows() 
        self.assertEqual(result, True)

    def test_7(self):
        result = self.pg.del_favorite()
        self.assertEqual(result, "Добавить в избранное")
    
    def test_8(self):
        result = self.pg.displayed_windows() 
        self.assertEqual(result, True)
    
    def test_9(self):
        result = self.pg.ref_page()
        self.assertEqual(result, "Войдите в аккаунт")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
