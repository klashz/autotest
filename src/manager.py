from typing import List, Union
from collections import Counter

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from .base import Config


class PageManager:
    def __init__(self) -> None:
        pass

    def get_status_tasks(self, driver: webdriver) -> List[WebElement]:
        task_list = driver.find_element(By.TAG_NAME, "ul")
        status_tasks = task_list.find_elements(By.XPATH, f"//span[@class='{Config.UNDONE}' or @class='{Config.DONE}']")
        return list(map(lambda x: x.get_attribute("class"), status_tasks))

    def get_tasks(self, driver: webdriver) -> List[WebElement]:
        task_list = driver.find_element(By.TAG_NAME, "ul")
        tasks = task_list.find_elements(By.XPATH, "//input[@type='checkbox']")
        return tasks

    def create_task(self, driver: webdriver, text: str) -> Union[bool, ValueError]:
        if not isinstance(text, str):
            raise ValueError("Enter only string type!")
        
        # Set text!
        temp_input = driver.find_element(By.XPATH, "//input[@id='sampletodotext']")
        temp_input.send_keys(text)

        # click!
        button: WebElement = driver.find_element(By.XPATH, "//input[@id='addbutton']")
        button.click()

        return True

    def mapper(self, values: List[Union[Config.DONE, Config.UNDONE]]) -> str:

        for i in range(len(values)):
            values[i] = Config.MAPPED[values[i]]

        results = Counter(values)
        info = f'Marked: {results.get("Marked", 0)}  Not marked: {results.get("Not marked", 0)}'

        return info
