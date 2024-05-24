from typing import Dict

from selenium.webdriver.edge.options import Options as EdgeOptions


class Config:
    BASE_URL: str = "https://megamarket.ru/"
    QUERY: str = "смарт-часы"
    IMAGE_LOGS: str = "./logs/images/"
    
    @staticmethod
    def get_option() -> EdgeOptions:
        options = EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        options.page_load_strategy = 'none'
        return options
