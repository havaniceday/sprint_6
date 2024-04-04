from selenium.webdriver.common.by import By


class MainPageLocators:
        QUESTION_LOCATOR = By.ID, 'accordion__heading-{}' #локатор клика по вопросу
        ANSWER_LOCATOR = By.XPATH, './/div[@id="accordion__panel-{}"]/p' #локатор ответа
        SCOOTER_LOGO = By.XPATH, './/a[contains(@class, "Header_LogoScooter")]' # логотип "Самокат"
        YANDEX_LOGO = By.XPATH, './/a[contains(@class, "Header_LogoYandex")]' # логотип "Яндекс"
        DZEN_LOCATOR = By.XPATH, '//span[text()="Главная"]' #локатор главной страницы Дзена
        ACCEPT_COOKIES_BUTTON = By.ID, 'rcc-confirm-button' # кнопка подтверждения куки "Да все привыкли"
