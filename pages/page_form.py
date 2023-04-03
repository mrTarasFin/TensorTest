from pages.BaseApp import BasePage
from locators.locator_form import PageLocators as Locators
from selenium.webdriver.common.keys import Keys
import time


class FormPage(BasePage):

    def find_element_on_site(self):
        self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD).send_keys('Тензор', Keys.ENTER)
        self.find_element(Locators.LOCATOR_TENSOR_LINK).click()
        time.sleep(15)

