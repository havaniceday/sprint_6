import allure
import pytest
import helper
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Оформление заказа по клику на кнопку в хэдэре')
    @allure.description("При вводе валидных данных появляется сообщение об успешном оформлении заказа")
    def test_order_from_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie_button()
        order_page.click_order_from_header()
        order_page.fill_user_data()
        order_page.select_metro_station(helper.UserData.station_number)
        order_page.click_next()
        order_page.select_date(helper.UserData.date)
        order_page.select_rent_time(helper.UserData.rent_time)
        order_page.select_color(helper.UserData.color)
        order_page.comment()
        order_page.complete_order()
        text = order_page.get_confirmation_text()
        assert text == "Посмотреть статус"
    @allure.title('Оформление заказа по клику на кнопку в середине страницы')
    @allure.description("При вводе валидных данных появляется сообщение об успешном оформлении заказа")
    def test_order_from_main(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie_button()
        order_page.click_order_from_main()
        order_page.fill_user_data()
        order_page.select_metro_station(helper.UserData.station_number)
        order_page.click_next()
        order_page.select_date(helper.UserData.date)
        order_page.select_rent_time(helper.UserData.rent_time)
        order_page.select_color(helper.UserData.color)
        order_page.comment()
        order_page.complete_order()
        text = order_page.get_confirmation_text()
        assert text == "Посмотреть статус"
