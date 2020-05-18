import selenium
from selenium import webdriver
import pytest


class TestSelenium:
    def setup(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Firefox()

    def teardown(self):
        self.driver.quit()
    def test_selenium(self):
        # self.driver.get('https://www.baidu.com/')
        self.driver.get('https://www.baidu.com/')
