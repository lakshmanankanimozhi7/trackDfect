import xlsxwriter
import logging
import os
from unittest import TestCase
from selenium import webdriver
import src.framework.global_config as config
from selenium.webdriver.chrome.options import Options

# from sauceclient import SauceClient


class BaseTest(TestCase):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")


        self.driver = webdriver.Chrome("/Users/kanimozhi/software/chromedriver")
        config.DRIVER = self.driver


    def tearDown(self):
        self.driver.quit()


    def save_screen_shot(self, name,num):
        dir = os.getcwd() + "/screenshots{}/".format(num)
        if not os.path.exists(dir):
            os.makedirs(dir)
        file_name = name + ".png"
        self.logger.info(file_name)
        self.driver.save_screenshot(filename=file_name)



