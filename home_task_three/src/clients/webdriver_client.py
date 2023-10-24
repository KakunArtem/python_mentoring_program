import logging

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverTypes:
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    SAFARI = 'safari'


class WebDriverClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver_type: DriverTypes, driver_options=None):
        self._driver_type = driver_type
        self._driver_options = driver_options
        self._driver = self._init_driver()

    def _init_driver(self) -> WebDriver:
        if self._driver_type == DriverTypes.CHROME:
            logging.info('Launch Chrome browser')
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                    options=self._driver_options)
        elif self._driver_type == DriverTypes.FIREFOX:
            logging.info('Launch Firefox browser')
            return webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                                     options=self._driver_options)
        elif self._driver_type == DriverTypes.SAFARI:
            logging.info('Launch Safari browser')
            return webdriver.Safari(options=self._driver_options)
        else:
            raise ValueError("Browser type is not supported")

    def get_client(self):
        return self._driver
