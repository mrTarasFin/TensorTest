from selenium.webdriver import ActionChains

from pages.BaseApp import BasePage
from locators.locator_form import PageLocators as Locators
from selenium.webdriver.common.keys import Keys
import time


class FormPage(BasePage):

    def is_search_field_present(self):
        time.sleep(1)
        if self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD):
            return True
        else:
            return False

    def find_search_field(self):
        return self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD)

    def click_search_field(self):
        self.find_search_field().click()

    def enter_word(self, word):
        self.find_search_field().send_keys(word)

    def is_suggest_visible(self):
        time.sleep(1)
        if self.find_element(Locators.LOCATOR_YANDEX_SUGGEST, time=2):
            return True and print('Help suggest is visible')
        else:
            return False and print('Help suggest is not visible')

    def start_search_word(self):
        search_field = self.find_search_field()
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_first_link(self):
        self.find_element(Locators.LOCATOR_TENSOR_LINK).click()
        time.sleep(5)

    def is_url_current(self):
        if self.get_current_url() == 'https://tensor.ru/':
            return print('Link is "tensor.ru"')
        else:
            return print('Link is not "tensor.ru"')

    def find_help_suggest(self):
        if self.find_element(Locators.LOCATOR_YANDEX_SUGGEST):
            return True
        else:
            return False

    def click_all_icon(self):
        self.find_element(Locators.LOCATOR_YANDEX_ICONS_ALL).click()

    def find_item_icon(self):
        icon_image = self.find_element(Locators.LOCATOR_IMAGES_INNER)
        icon_image.click()

    def choose_first_image_item(self):
        self.find_element(Locators.LOCATOR_FIRST_IMAGES_ITEMS).click()






