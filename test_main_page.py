from pages.main_page import MainPage
from pages.basket_page import BasketPage
import pytest

url = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser) -> None:
        page = MainPage(browser, url)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser) -> None:
        page = MainPage(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser) -> None:
        main_page = MainPage(browser, url)
        main_page.open()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.go_to_basket_page()
        basket_page.product_list_must_be_empty()
        basket_page.product_list_must_contain_a_message_about_the_empty_basket()
