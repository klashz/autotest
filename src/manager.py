import os
import time
import re
from datetime import datetime as dt
from typing import Optional

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base import Config


class PageManager:
    def __init__(self) -> None:
        self.driver: webdriver.Edge

    def open_link(self, url: str = Config.BASE_URL) -> str:
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Искать товары"]')))
        return self.driver.current_url
    
    def search(self, query: str = Config.QUERY) -> str:
        time.sleep(1)
        inp = self.driver.find_element(By.XPATH, '//input[@placeholder="Искать товары"]')
        inp.send_keys(query)
        btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        btn.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='breadcrumb-item']")))
        items = self.driver.find_elements(By.XPATH, "//li[@class='breadcrumb-item']")
        return list(map(lambda x: x.text, items))[-1]
    
    def open_item(self):
        item = self.driver.find_element(By.XPATH, "//div[@class='catalog-items-list']//child::div")
        name = item.find_element(By.XPATH, "//a[@title]").text
        yield name
        item.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='pdp-header']//child::h1")))
        title = self.driver.find_element(By.XPATH, "//div[@class='pdp-header']//child::h1").text
        yield title

    def price(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//meta[@itemprop='price']")))
        price = self.driver.find_element(By.XPATH, "//meta[@itemprop='price']")
        return price.get_attribute("content")

    def reviews(self):
        reviews = self.driver.find_element(By.XPATH, "//span[@class='reviews-rating__reviews-count']").text
        num = re.findall("\d+", reviews)[0]
        return num if num else 0

    def screenshots(self, test_name: str, path: Optional[str] = Config.IMAGE_LOGS) -> None:
        current_time = dt.now().strftime('%Y_%m_%d_%H_%M_%S')
        filename = f"num_test_{test_name}_{current_time}.png"
        image = self.driver.save_screenshot(os.path.join(path, filename))
