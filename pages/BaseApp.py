from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(e_c.presence_of_element_located(locator),
                                                      message=f'Элемент {locator} не найден'
                                                      )

    def find_elements(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(e_c.presence_of_all_elements_located(locator),
                                                      message=f'Элементы {locator} не найдены'
                                                      )

    def open_site(self):
        return self.driver.get(self.url)


