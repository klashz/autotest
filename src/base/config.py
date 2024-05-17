from typing import Dict

from selenium.webdriver.edge.options import Options as EdgeOptions


class Config:
    BASE_URL: str = "https://lambdatest.github.io/sample-todo-app/"
    DONE: str = "done-true"
    UNDONE: str = "done-false"
    MAPPED: Dict[str, str] = {"done-true": "Marked", "done-false": "Not marked"}

    @staticmethod
    def get_option() -> EdgeOptions:
        options = EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return options
