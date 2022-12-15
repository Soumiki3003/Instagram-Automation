
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest
import time


class Puki:
    def __init__(self) -> None:
        self.s = Service('./geckodriver.exe')
        self.fire_driver = webdriver.Firefox(service=self.s)

    @pytest.fixture
    def test_setup(self):
        self.fire_driver.implicitly_wait(15)
        self.fire_driver.maximize_window()


    def test_account_instagram(self):

        self.fire_driver.get('https://www.instagram.com/')
        self.fire_driver.implicitly_wait(15)
        self.fire_driver.find_element(
            by=By.NAME, value="username").send_keys("hjjkli133")
        self.fire_driver.find_element(
            by=By.NAME, value="password").send_keys("kinoontheisland")
        self.fire_driver.implicitly_wait(15)
        login = self.fire_driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
        login.click()
        self.fire_driver.implicitly_wait(10)
        not_now = self.fire_driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/section/main/div/div/div/div/button")
        not_now.click()
        self.fire_driver.implicitly_wait(10)
        
        not_now2 = self.fire_driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        not_now2.click()
        
        # scrolling with infinite loading
        last_height = self.fire_driver.execute_script("return document.body.scrollHeight")
        while True:
        # Scroll down to bottom
            self.fire_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
            time.sleep(8)
        # Calculate new scroll height and compare with last scroll height
            new_height = self.fire_driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                 break
            last_height = new_height


obj1 = Puki()
obj1.test_account_instagram()
