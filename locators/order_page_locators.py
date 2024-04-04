from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_HEADER_LOCATOR = By.CLASS_NAME, 'Button_Button__ra12g' #кнопка "Заказать" в хэдэре
    ORDER_MAIN_LOCATOR = DOWN_BUTTON = By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button' #кнопка "Заказать" на основной странице
    NAME_FIELD = By.XPATH, './/input[@placeholder="* Имя"]' #поле ввода имени
    SURNAME_FIELD = By.XPATH, './/input[@placeholder="* Фамилия"]' # поле ввода Фамилии
    ADDRESS_FIELD = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]' # поле ввода Адреса
    METRO_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]' # поле ввода Станции метро
    METRO_STATION = By.XPATH, './/li[@class="select-search__row"]/button[@value="{}"]' # станция метро
    PHONE_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]' # поле ввода номера телефона
    NEXT_CTA = By.XPATH, './/button[text()="Далее"]' #кнопка "Далее"
    DATE_DROPDOWN = By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]' #поле ввода даты
    RENT_TIME_DROPDOWN = By.XPATH, './/span[@class="Dropdown-arrow"]' #открытие дропдауна со сроками аренды
    RENT_TIME_SELECTION = By.XPATH, './/div[@class="Dropdown-menu"]/div[text()="{}"]' #выбор срока аренды
    GREY_COLOR_SELECTOR = By.ID, "grey" #выбор безысходности
    BLACK_COLOR_SELECTOR = By.ID, "black" #выбор серого жемчуга
    COMMENT_INPUT = By.XPATH, './/input[@placeholder="Комментарий для курьера"]' #поле ввода комментария
    ORDER_CTA = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()= "Заказать"]'  #кнопка "Заказать" в конце оформления заказа
    CONFIRM_CTA = By.XPATH, './/button[text()="Да"]' #кнопка "ДА" в конфирмейшен поп-апе
    CONFIRMATION_LOCATOR = By.XPATH, './/div[contains(@class,"Order_NextButton")]/button' #локатор, доступный только для подтвержденного заказа