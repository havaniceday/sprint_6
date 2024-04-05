import allure
import pytest

import helper
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helper import URls

class TestHeader:
    @allure.title('Проверка перехода на главную по клику на логотип Самокат')
    @allure.description("Переход на гравную страницу Самоката по кллику на его лого со страницы заказа")
    def test_redirect_to_scooter_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_page.click_order_from_header()
        main_page.click_to_scooter_logo()
        result_url = main_page.get_url()
        assert result_url == helper.URls.base_url

    @allure.title('Проверка перехода на Дзен по клику на логотип Яндекс')
    @allure.description("Открытие новой вкладки Яндекс Дзен по клику на лого")
    def test_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_yandex_logo()
        main_page.switch_tabs_with_wait()
        result_url = main_page.get_url()
        assert result_url == helper.URls.dzen_url
