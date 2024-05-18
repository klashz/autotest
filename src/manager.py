import os
import time
from datetime import datetime as dt
from typing import List, Optional

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
        element = By.XPATH, "//div[@class='kYYKD _3EmFM']"
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(element))
        all_results_search = self.driver.find_element(*element)
        blocks = all_results_search.find_elements(By.XPATH, "//div[@class='_1ENFO']")
        likes = all_results_search.find_elements(By.XPATH, "//button[@class='_2VECW' and @title='Добавить в избранное']")
        texts = all_results_search.find_elements(By.XPATH, "//h3[@role='link']")
        prices = all_results_search.find_elements(By.XPATH, "//span[@class='_1ArMm']")
        total = abs(len(blocks) - len(likes))
        
        c = 1
        for text, price in list(zip(texts, prices))[total:size + total]:
            print(f'Название товара: "{text.text}"  Цена товара: {price.text}')
            c += 1

        return likes, c

    def select_like(self, likes: List[WebElement]) -> str:
        likes[0].click()
        result = likes[0].get_attribute("title")
        time.sleep(2)
        return result

    def select_favorite(self) -> str:
        self.driver.find_element(By.XPATH, "//a[@href='/my/wishlist?track=head']").click()
        time.sleep(1)
        return self.driver.current_url
    
    def delete_favorite(self) -> str:
        self.driver.find_element(By.XPATH, "//button[@title='Удалить из избранного']").click()
        time.sleep(5)
        return self.driver.find_element(By.XPATH, "//button[@title='Добавить в избранное']").get_attribute("title")

    def refresh_page(self) -> str:
        self.driver.refresh()
        element = By.XPATH, "//span[@data-auto='emptyStateHeader']"
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(element))

        results = self.driver.find_element(*element)
        
        return results.text
    
    def screenshots(self, test_name: str, path: Optional[str] = Config.IMAGE_LOGS) -> None:
        current_time = dt.now().strftime('%Y_%m_%d_%H_%M_%S')
        filename = f"num_test_{test_name}_{current_time}.png"
        image = self.driver.save_screenshot(os.path.join(path, filename))
