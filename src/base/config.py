from typing import Dict

from selenium.webdriver.edge.options import Options as EdgeOptions


class Config:
    BASE_URL: str = "https://market.yandex.ru/"
    IMAGE_LOGS: str = "./logs/images/"
    
    @staticmethod
    def get_option() -> EdgeOptions:
        options = EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        return options
