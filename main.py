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


# Проверяет, что изначальное количество оставшихся задач указано правильно.
text = driver.find_element(By.CLASS_NAME, "ng-binding").text
assert text == "5 of 5 remaining", ValueError("Задачи не совпадают!")

# Отмечает первую задачу как выполненную и проверяет изменение.
status_tasks = manager.get_status_tasks(driver)
print("Status of task list before click:", status_tasks)

tasks = manager.get_tasks(driver)
tasks[0].click()
time.sleep(1)

status_tasks = manager.get_status_tasks(driver)
print("Status of task list after click:", status_tasks)

# Добавляет новый элемент в список и отмечает его как выполненный.
manager.create_task(driver, "Сделать первую лабу")
time.sleep(1)
tasks = manager.get_tasks(driver)
tasks[-1].click()
status_tasks = manager.get_status_tasks(driver)
print("Check status of task list with new task: ", status_tasks)
time.sleep(1)

