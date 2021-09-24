from pages.product_page import ProductPage
import pytest


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"

@pytest.mark.xfail(run=False)
@pytest.mark.parametrize('promo', [
    "0", "1", "2",
    "3", "4", "5",
    pytest.param("7", marks = pytest.mark.fail), 
    "6", "8", "9",
])
def test_guest_can_add_product_to_basket(browser, promo):
    page = ProductPage(browser, f"{url}{promo}")
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.is_valid_price_for_item()
    page.is_valid_item_in_card()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    '''
    Открываем страницу товара 
    Добавляем товар в корзину 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    '''
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_card()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    '''
    Открываем страницу товара 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    '''
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    '''
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    '''
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_card()
    page.element_should_disappear()

def test_guest_should_see_login_url_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()