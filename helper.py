import random
from datetime import datetime, timedelta
from locators.order_page_locators import OrderPageLocators

class URls:
    base_url = 'https://qa-scooter.praktikum-services.ru/'
    dzen_url = 'https://dzen.ru/?yredirect=true'

class Answers:
    answers = [(0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
               (1,
                "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
               (2,
                "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
               (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
               (4,
                "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
               (5,
                "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
               (6,
                "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
               (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")]

class UserData:
    names = ["Вася", "Анна Мария", "Лю Фен Ом"]
    name = random.choice(names)

    surnames = ["Кто", "Знает", "Доу", "Великолепный"]
    surname = random.choice(surnames)

    streets = ["Пушкина", "Есенина", "Чехова", "Вознесенского"]
    address = f'{random.choice(streets)} д. {random.randint(1, 999)}, кв. {random.randint(1, 999)}'

    phone = f"{random.randint(10000000000, 99999999999)}"

    station_number = random.randint(1,237)

    start_date = datetime(2024, 4, 5)
    end_date = datetime(2024, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    date = random_date.strftime("%d.%m.%Y")

    rent_periods = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']
    rent_time = random.choice(rent_periods)

    colors = OrderPageLocators.GREY_COLOR_SELECTOR, OrderPageLocators.BLACK_COLOR_SELECTOR
    color = random.choice(colors)

    comments = ["", "ляляля", "URGENT ORDER!!!"]
    comment = random.choice(comments)
