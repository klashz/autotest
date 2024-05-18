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

    def __open_list(self, driver: webdriver) -> None:
        button = driver.find_element(By.XPATH, "//button[@class='hamburger']")
        button.click()
    
    def __open_study(self, driver: webdriver) -> None:
        button = driver.find_element(By.XPATH, "//a[text()='Обучающимся']")
        wait = WebDriverWait(driver, timeout=10)
        wait.until(lambda _: button.is_displayed())
        webdriver.ActionChains(driver).move_to_element(button).perform()
    
    def __open_schedule(self, driver: webdriver) -> None:
        button = driver.find_element(By.XPATH, "//a[text()='Расписания']")
        wait = WebDriverWait(driver, timeout=10)
        wait.until(lambda _: button.is_displayed())
        button.click()

    def schedule(self, driver: webdriver) -> None:
        self.__open_list(driver)
        self.__open_study(driver)
        self.__open_schedule(driver)
        return driver.current_url

    def watch_on_site_schedule(self, driver: webdriver) -> str:
        span = driver.find_element(By.XPATH, "//span[text()='Смотрите на сайте']")
        webdriver.ActionChains(driver).scroll_to_element(span).perform()
        button = span.find_element(By.XPATH, "./..")
        button.click()
        driver.switch_to.window(driver.window_handles[1])
        return driver.current_url
    
    def set_groups(self, driver: webdriver, groups: str = Config.GROUPS) -> None:
        entry = driver.find_element(By.XPATH, "//input[@class='groups']")
        entry.send_keys(groups)
        return groups
    
    def click_to_groups(self, driver: webdriver):
        wait = WebDriverWait(driver, timeout=10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='221-323']")))
        group = driver.find_element(By.XPATH, "//div[text()='221-323']")
        group.click()
        return group.get_attribute("id")
    
    def screenshots(self, driver: webdriver, test_name: str, path: Optional[str] = Config.IMAGE_LOGS) -> None:
        current_time = dt.now().strftime('%Y_%m_%d_%H_%M_%S')
        filename = f"num_test_{test_name}_{current_time}.png"
        image = driver.save_screenshot(os.path.join(path, filename))
