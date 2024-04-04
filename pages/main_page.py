import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
class MainPage(BasePage):
    @allure.step("Клик на вопрос и получение соответствующего ответа")
    def click_to_question_and_get_answer_text(self, number):
        locator_question = self.format_locators(MainPageLocators.QUESTION_LOCATOR, number)
        self.scroll_to_element(locator_question)
        self.click_with_wait(locator_question)
        locator_answer = self.format_locators(MainPageLocators.ANSWER_LOCATOR, number)
        return self.get_text(locator_answer)

    @allure.step('Клик по кнопке подтверждения куки "Да все привыкли"')
    def accept_cookie_button(self):
        self.click_with_wait(MainPageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step("Клик по логотипу Яндекса")
    def click_to_yandex_logo(self):
        self.find_element_with_wait(MainPageLocators.YANDEX_LOGO).click()

    @allure.step("Клик по логотипу Самокат")
    def click_to_scooter_logo(self):
        self.find_element_with_wait(MainPageLocators.SCOOTER_LOGO).click()

