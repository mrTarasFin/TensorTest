import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    '''Функция инициализирует работу WebDriver основные настройки для тестирования'''
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window() # расширяем окно браузера до максимальных размеров
    yield driver
    driver.quit()
