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
    
    def checking_start_text(self):
        text = self.driver.find_element(By.CLASS_NAME, "ng-binding").text
        return text
    
    def status_first_task(self):
        return self.get_status_tasks(self.driver)[0]

    def click_by_tasks(self):
        status_tasks = self.get_status_tasks(self.driver)
        print("Status of task list before click:", self.mapper(status_tasks))

        tasks = self.get_tasks(self.driver)
        for i in range(len(status_tasks)):
            tasks[i].click()
            time.sleep(1)

            temp_status_tasks = self.get_status_tasks(self.driver)
            print("Status of task list after click:", self.mapper(temp_status_tasks))

        return self.get_text_task(self.driver)[-1]

    def create_new_task(self):
        self.create_task(self.driver, "Сделать первую лабу")
        time.sleep(1)
        tasks = self.get_tasks(self.driver)
        status_tasks = self.get_status_tasks(self.driver)
        print("Status of task list with new task before click:", self.mapper(status_tasks))
        tasks[-1].click()
        status_tasks = self.get_status_tasks(self.driver)
        print("Status of task list with new task after click:", self.mapper(status_tasks))
        return self.get_text_task(self.driver)[-1]
    
    def checking_count(self):
        return len(self.get_tasks(self.driver))
    

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pg = TestPage()

    def test_1(self):
        result = self.pg.checking_start_text()
        self.assertEqual(result, "5 of 5 remaining")

    def test_2(self):
        result = self.pg.status_first_task()
        self.assertEqual(result, "done-false")

    def test_3(self):
        result = self.pg.click_by_tasks()
        self.assertEqual(result, "Fifth Item")

    def test_4(self):
        result = self.pg.create_new_task()
        self.assertEqual(result, "Сделать первую лабу")

    def test_5(self):
        result = self.pg.checking_count()
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
