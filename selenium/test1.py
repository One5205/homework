import selenium
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestSelenium:
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium测试')
        self.driver.find_element(By.XPATH, '//*[@id="page"]/a[10]').click()
        # self.driver.get('https://www.baidu.com/')
