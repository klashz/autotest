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


class PageManager:
    def __init__(self) -> None:
        pass

    def open_catalog(self) -> str:
        button = self.driver.find_element(By.XPATH, "//span[text()='Каталог']/..")
        button.click()
        return button.text

    def select_category(self) -> str:
        element = By.XPATH, "//span[text()='Все для гейминга']"
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(element))
        category = self.driver.find_element(element[0], element[1] + "/..")
        webdriver.ActionChains(self.driver).move_to_element(category).perform()
        return self.driver.current_url

    def select_xbox(self) -> str:
        element = By.XPATH, "//a[text()='Xbox']"
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(element))
        xbox = self.driver.find_element(*element)
        return xbox.text
    
    def select_subcategory(self) -> str:
        element = By.XPATH, "//a[text()='Xbox']"
        item: WebElement = self.driver.find_element(element[0], element[1] + "//parent::div//parent::div//parent::div//child::ul//child::a")
        text = item.text
        item.click()
        return text

    def select_list(self, size: int = 5):
        element = By.XPATH, "//div[@data-auto='SerpList']"
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(element))
        all_results_search = self.driver.find_element(*element)
        items = all_results_search.find_elements(By.XPATH, "//child::div[@data-apiary-widget-name='@marketfront/SerpEntity']")
        for item in items:
            print(item.find_element(By.XPATH, "//child::h3[@data-auto='snippet-title']").text,
                    item.find_element(By.XPATH, "//child::span[@class='_1ArMm']").text)
        time.sleep(30)
        # /content/page/fancyPage/cms/4/SearchSerp-SearchSerp/serpSearch/content/lazyGenerator/initialContent/serpLayoutItem