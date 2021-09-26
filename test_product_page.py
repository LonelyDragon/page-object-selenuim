from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import pytest
import random


@pytest.mark.parametrize('promo', [
    "0", "1", "2",
    "3", "4", "5",
    pytest.param("7", marks=pytest.mark.xfail(run=False)),
    "6", "8", "9",
])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo) -> None:
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, f"{url}{promo}")
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.is_valid_price_for_item()
    page.is_valid_item_in_card()


@pytest.mark.xfail(run=False)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser) -> None:
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_card()
    page.should_not_be_success_message()


@pytest.mark.xfail(run=False)
def test_guest_cant_see_success_message(browser) -> None:
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(run=False)
def test_message_disappeared_after_adding_product_to_basket(browser) -> None:
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_card()
    page.element_should_disappear()


@pytest.mark.xfail(run=False)
def test_guest_should_see_login_url_on_product_page(browser) -> None:
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser) -> None:
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser) -> None:
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.product_list_must_be_empty()
    basket_page.product_list_must_contain_a_message_about_the_empty_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser) -> None:
        url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, url)
        self.page.open()
        self.page.register_new_user(
            f'{random.randint(1,100)}@fakemail.ru', 'qwerty1234!')
        self.page.should_be_authorized_user

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser) -> None:
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_card()
        page.is_valid_price_for_item()
        page.is_valid_item_in_card()

    def test_user_cant_see_success_message(self, browser) -> None:
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()
