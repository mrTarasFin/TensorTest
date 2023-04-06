import pytest
from pages.page_form import FormPage
from locators.locator_form import PageLocators as Locators



@pytest.mark.search_site
def test_one_part(browser):
    search_tensor = FormPage(browser)
    search_tensor.open_site()
    search_tensor.is_search_field_present()
    search_tensor.find_search_field()
    search_tensor.enter_word('Тензор')
    search_tensor.is_suggest_visible()
    search_tensor.start_search_word()
    search_tensor.find_first_link()
    search_tensor.go_to_next_page()
    search_tensor.is_url_current()


@pytest.mark.image
def test_two_part(browser):
    image = FormPage(browser)
    image.open_site()
    image.click_search_field()
    image.click_all_icon()
    image.find_item_icon()
    image.go_to_next_page()
    assert image.get_current_url() == 'https://yandex.ru/images/', 'Ссылка не https://yandex.ru/images/'
    image.choose_first_image_item()
    # на данном шаге требовалось сравнить название категории с текстом в поле поиска, к сожалению у меня не получилось
    image.first_image_in_category()
    image1 = image.get_attribute_src(Locators.LOCATOR_LINK_IMAGE)
    image.click_next_image()
    image2 = image.get_attribute_src(Locators.LOCATOR_LINK_IMAGE)
    assert image1 != image2, 'Ссылка не изменилась'
    if image1 != image2:
        print('Картинка поменялась')
    image.click_prev_image()
    image3 = image.get_attribute_src(Locators.LOCATOR_LINK_IMAGE)
    assert image1 == image3, 'Ссылки картинок разные'
    if image1 == image3:
        print('Перешли к первоначальной картинке')
