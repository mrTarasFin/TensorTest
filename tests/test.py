import pytest
from pages.page_form import FormPage
from time import sleep


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
    sleep(5)
    image.find_item_icon()
    image.go_to_next_page()
    image.choose_first_image_item()






