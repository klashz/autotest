import os
import time
from datetime import datetime as dt
from typing import List, Union, Optional

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base import Config


# base class for Page Object
class PageManager:
    def __init__(self) -> None:
        pass

    def __open_list(self) -> None:
        button = self.driver.find_element(By.XPATH, "//button[@class='hamburger']")
        button.click()
    
    def __open_study(self) -> None:
        button = self.driver.find_element(By.XPATH, "//a[text()='Обучающимся']")
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(lambda _: button.is_displayed())
        webdriver.ActionChains(self.driver).move_to_element(button).perform()
    
    def __open_schedule(self) -> None:
        button = self.driver.find_element(By.XPATH, "//a[text()='Расписания']")
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(lambda _: button.is_displayed())
        button.click()

    def schedule(self) -> None:
        self.__open_list()
        self.__open_study()
        self.__open_schedule()
        return self.driver.current_url

    def watch_on_site_schedule(self) -> str:
        span = self.driver.find_element(By.XPATH, "//span[text()='Смотрите на сайте']")
        webdriver.ActionChains(self.driver).scroll_to_element(span).perform()
        button = span.find_element(By.XPATH, "./..")
        button.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url
    
    def set_groups(self, groups: str = Config.GROUPS) -> None:
        entry = self.driver.find_element(By.XPATH, "//input[@class='groups']")
        entry.send_keys(groups)
        return groups
    
    def click_to_groups(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='221-323']")))
        group = self.driver.find_element(By.XPATH, "//div[text()='221-323']")
        group.click()
        return group.get_attribute("id")

    def current_day(self):
        time.sleep(1)
        if dt.today().weekday() == 6 - 1:
            return None
        title = self.driver.find_element(By.CLASS_NAME, "schedule-day_today") \
                           .find_element(By.CLASS_NAME, "schedule-day__title")

        return title
    
    def screenshots(self, test_name: str, path: Optional[str] = Config.IMAGE_LOGS) -> None:
        current_time = dt.now().strftime('%Y_%m_%d_%H_%M_%S')
        filename = f"num_test_{test_name}_{current_time}.png"
        self.driver.save_screenshot(os.path.join(path, filename))
