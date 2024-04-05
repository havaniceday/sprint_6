import allure
import pytest
from helper import Answers
from pages.main_page import MainPage

class TestMainPage:

    @allure.title('Проверка соответствия ответов вопросам в разделе "Вопросы о важном", вопрос {number}')
    @allure.description("По клику на вопрос появляется соответствующий текст ответа")
    @pytest.mark.parametrize(
        'number, expected_text',
        Answers.answers)
    def test_question_text_is_returned(self, driver, number, expected_text):
        main_page = MainPage(driver)
        text_answer = main_page.click_to_question_and_get_answer_text(number)
        assert text_answer == expected_text
