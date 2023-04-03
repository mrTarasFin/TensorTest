from selenium.webdriver.common.by import By


class PageLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_FIRST_LINK = (By.XPATH, '//*[@id="search-result"]/li[@data-cid="0"]')
    LOCATOR_TENSOR_LINK = (By.LINK_TEXT, 'tensor.ru')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".services-suggest")

