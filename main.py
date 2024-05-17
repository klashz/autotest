import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from src import (
    GetSeleniumEdge, 
    Config, 
    PageManager
)


manager = PageManager()
driver = GetSeleniumEdge()
driver.get(Config.BASE_URL)


text = driver.find_element(By.CLASS_NAME, "ng-binding").text
assert text == "5 of 5 remaining", ValueError("Задачи не совпадают!")

status_tasks = manager.get_status_tasks(driver)
print("Status of task list before click:", status_tasks)

for i in range(len(status_tasks)):
    tasks = manager.get_tasks(driver)
    tasks[i].click()
    time.sleep(1)

    temp_status_tasks = manager.get_status_tasks(driver)
    print("Status of task list after click:", temp_status_tasks)

print("Add new task...")
manager.create_task(driver, "Сделать первую лабу")
time.sleep(1)
tasks = manager.get_tasks(driver)
tasks[-1].click()
print("Status of task list with new task before click:", temp_status_tasks)
status_tasks = manager.get_status_tasks(driver)
print("Status of task list with new task after click: ", status_tasks)
time.sleep(1)
