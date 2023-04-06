from pages.BaseApp import BasePage
from locators.locator_form import PageLocators as Locators
from selenium.webdriver.common.keys import Keys
import time


class FormPage(BasePage):

    def is_search_field_present(self):
        '''Функция определяет наличие поля поиска на странице'''
        time.sleep(1)
        if self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD):
            return True
        else:
            return False

    def find_search_field(self):
        '''Функция определяет поле поиска на странице'''
        return self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD)

    def click_search_field(self):
        '''Функция моделирует нажатие кнопкой мыши на поле поиска'''
        self.find_search_field().click()

    def enter_word(self, word):
        '''Функция вводит слово в поле поиска'''
        self.find_search_field().send_keys(word)

    def is_suggest_visible(self):
        '''Функция проверяет наличие дополнительного поиска'''
        time.sleep(1)
        if self.find_element(Locators.LOCATOR_YANDEX_SUGGEST, time=2).is_enabled:
            return True and print('Help suggest is visible')
        else:
            return False and print('Help suggest is not visible')

    def start_search_word(self):
        '''Функция активирует поиск слова в поле поиска'''
        search_field = self.find_search_field()
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_first_link(self):
        '''Функция переходит по первой ссылке в результате поиска'''
        self.find_element(Locators.LOCATOR_TENSOR_LINK).click()
        time.sleep(5)

    def is_url_current(self):
        '''Функция проверяет корректность перехода на страницу сайта Тензор'''
        if self.get_current_url() == 'https://tensor.ru/':
            return print('Link is "tensor.ru"')
        else:
            return print('Link is not "tensor.ru"')

    def find_help_suggest(self):
        '''Функция проверяет наличие suggest вариантов поиска по слову'''
        if self.find_element(Locators.LOCATOR_YANDEX_SUGGEST):
            return True
        else:
            return False

    def click_all_icon(self):
        '''Функция открывает popup с елементами иконок категорий'''
        self.find_element(Locators.LOCATOR_YANDEX_ICONS_ALL).click()

    def find_item_icon(self):
        '''Функция ищет иконку Картинки и активирует ссылку'''
        icon_image = self.find_element(Locators.LOCATOR_IMAGES_INNER)
        icon_image.click()

    def choose_first_image_item(self):
        '''Функция ищет первый елемент из категории картинки'''
        self.find_element(Locators.LOCATOR_FIRST_IMAGES_ITEMS).click()
        time.sleep(5)

    def first_image_in_category(self):
        time.sleep(5)
        self.find_element(Locators.LOCATOR_FIRST_IMAGE).click()
        time.sleep(5)

    def click_next_image(self):
        self.find_element(Locators.LOCATOR_NEXT_BUTTON).click()
        time.sleep(5)

    def click_prev_image(self):
        self.find_element(Locators.LOCATOR_PREV_BUTTON).click()
        time.sleep(5)

    def get_url_site(self):
        self.get_current_url()
