from selenium.webdriver.common.by import By


class PageLocators:
    """В данном классе определены основные локаторы для поиска объектов на странице согласно задания"""

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text") # локатор поля поиска на странице Яндекс
    LOCATOR_FIRST_LINK = (By.XPATH, '//*[@id="search-result"]/li[@data-cid="0"]') # относительный путь к первой ссылке результатов поиска
    LOCATOR_TENSOR_LINK = (By.LINK_TEXT, 'tensor.ru') # ссылка на страницу Тензор
    LOCATOR_YANDEX_SUGGEST = (By.XPATH, '//ul[contains(@class,"mini-suggest__popup-content")]') # путь к всплывающим подсказкам при поиске
    LOCATOR_YANDEX_SERVICE_SUGGEST = (By.CSS_SELECTOR, 'css=.services-suggest__icons-more')
    LOCATOR_YANDEX_ICONS_ALL = (By.CLASS_NAME, 'services-suggest__icons-more')
    LOCATOR_IMAGES_INNER = (
        By.CSS_SELECTOR,
        '.services-more-popup__section-content:nth-child(1) > .services-more-popup__item:nth-child(9) .services-more-popup__item-icon') # ссылка на "Картинки"
    LOCATOR_FIRST_IMAGES_ITEMS = (
        By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0 .PopularRequestList-Shadow') # наименование селектора первого элемента картинок
    LOCATOR_FIRST_IMAGE = (
        By.XPATH, '(//div[contains(@class,"serp-controller")]/descendant::div[contains(@class,"serp-item")])[1]') # первая картинка категории
    LOCATOR_NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next > .CircleButton-Icon') # кнопка слеующей картинки
    LOCATOR_PREV_BUTTON = (By.XPATH, '//div[contains(@class,"CircleButton CircleButton_type_prev")]/'
                                     'descendant::i[contains(@class,"CircleButton-Icon")]') # кнопка предыдущей картинки
    LOCATOR_LINK_IMAGE = (By.XPATH, '//img[contains(@class,"MMImage-Origin")]') # основной класс с ссылкой на картинку

