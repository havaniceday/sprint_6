from selenium import webdriver

import pytest
import allure
from selenium import webdriver
from helper import URls

@allure.step('Открыть браузер на странице сервиса / закрыть браузер')
@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--width=1280")
    firefox_options.add_argument("--height=720")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(URls.base_url)
    yield driver
    driver.quit()


