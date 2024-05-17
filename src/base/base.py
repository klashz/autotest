from typing import Optional

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

from . import Config


class SeleniumEdgeConfig:
    def __init__(self, options: Optional[EdgeOptions] = None) -> None:
        self.options = options
        if self.options is None:
            self.options = Config.get_option()
    
    def get_option(self) -> EdgeOptions:
        return self.options
        

class GetSeleniumEdge:
    def __new__(cls, options: Optional[EdgeOptions] = None):
        edge_config = SeleniumEdgeConfig(options)
        
        return webdriver.Edge(options=edge_config.get_option())
