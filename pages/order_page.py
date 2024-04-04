import allure

import helper
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from helper import UserData
import random


class OrderPage(BasePage):
    @allure.step("Клик по кнопке Заказать в хэдэре")
    def click_order_from_header(self):
        self.click_with_wait(OrderPageLocators.ORDER_HEADER_LOCATOR)

    @allure.step("Клик по кнопке Заказать на главной")
    def click_order_from_main(self):
        self.click_with_wait(OrderPageLocators.ORDER_MAIN_LOCATOR)

    def fill_name(self):
        self.fill_the_input(OrderPageLocators.NAME_FIELD, helper.UserData.name)

    def fill_surname(self):
        self.fill_the_input(OrderPageLocators.SURNAME_FIELD, helper.UserData.surname)

    def fill_address(self):
        self.fill_the_input(OrderPageLocators.ADDRESS_FIELD, helper.UserData.address)

    def fill_phone(self):
        self.fill_the_input(OrderPageLocators.PHONE_FIELD, helper.UserData.phone)

    @allure.step("Заполнение данных пользователя")
    def fill_user_data(self):
        self.fill_name()
        self.fill_surname()
        self.fill_address()
        self.fill_phone()

    @allure.step("Выбор станции метро")
    def select_metro_station(self, station_number):
        self.click_with_wait(OrderPageLocators.METRO_FIELD)
        station_locator = self.format_locators(OrderPageLocators.METRO_STATION, station_number)
        self.scroll_to_element(station_locator)
        self.click_with_wait(station_locator)

    @allure.step("Клик по кнопке Далее")
    def click_next(self):
        self.click_with_wait(OrderPageLocators.NEXT_CTA)

    @allure.step('Выбор даты')
    def select_date(self, date):
        self.click_with_wait(OrderPageLocators.DATE_DROPDOWN)
        self.fill_the_input(OrderPageLocators.DATE_DROPDOWN, helper.UserData.date)

    @allure.step('Выбор срока аренды')
    def select_rent_time(self, rent_time):
        self.click_with_wait(OrderPageLocators.RENT_TIME_DROPDOWN)
        rent_time = self.format_locators(OrderPageLocators.RENT_TIME_SELECTION, rent_time)
        self.click_with_wait(rent_time)

    @allure.step('Выбор цвета')
    def select_color(self, color):
        self.click_with_wait(color)
    @allure.step('Комментарий')
    def comment(self):
        self.fill_the_input(OrderPageLocators.COMMENT_INPUT, helper.UserData.comment)

    def click_order_from_order(self):
        self.click_with_wait(OrderPageLocators.ORDER_CTA)

    def confirm_order(self):
        self.click_with_wait(OrderPageLocators.CONFIRM_CTA)


    @allure.step('Клик по кнопке Заказать и согласие во всплывающем окне в конце оформления заказа')
    def complete_order(self):
        self.click_order_from_order()
        self.confirm_order()

    def get_confirmation_text(self):
        return self.get_text(OrderPageLocators.CONFIRMATION_LOCATOR)
