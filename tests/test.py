from pages.page_form import FormPage


class TestForm:

    def test_one(self, browser):
        form_page = FormPage(browser, 'https://ya.ru')
        form_page.open_site()
        form_page.find_element_on_site()
