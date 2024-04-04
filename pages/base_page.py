from selenium import webdriver
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_with_wait(self, locator):
        self.find_element_with_wait(locator).click()

    def fill_the_input(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text


    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locator, number):
        method, loc = locator
        loc = loc.format(number)
        return method, loc

    @allure.step('Переход на вторую вкладку')
    def switch_tabs_with_wait(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))

    @allure.step('Получение URL текущей страницы')
    def get_url(self):
        current_url = self.driver.current_url
        return current_url