import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import pytest

class TestLesson3():

    def test_add_to_basket_button_presence(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
                
        try:
            button = WebDriverWait(browser, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR , "button.btn-add-to-basket")) )
        except:
            assert False, "'Add to basket' button should be present"
        