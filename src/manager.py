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

    def open_catalog(self, driver: webdriver) -> str:
        button = driver.find_element(By.XPATH, "//span[text()='Каталог']/..")
        button.click()
        return button.text

    def select_category(self, driver: webdriver) -> str:
        element = By.XPATH, "//span[text()='Все для гейминга']"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(element))
        category = driver.find_element(element[0], element[1] + "/..")
        webdriver.ActionChains(driver).move_to_element(category).perform()
        return driver.current_url

    def select_xbox(self, driver: webdriver) -> str:
        element = By.XPATH, "//a[text()='Xbox']"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(element))
        xbox = driver.find_element(*element)
        return xbox.text
    
    def select_subcategory(self, driver: webdriver) -> str:
        element = By.XPATH, "//a[text()='Xbox']"
        item: WebElement = driver.find_element(element[0], element[1] + "//parent::div//parent::div//parent::div//child::ul//child::a")
        text = item.text
        item.click()
        return text