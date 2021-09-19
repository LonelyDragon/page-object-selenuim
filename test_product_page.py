from _pytest import mark
from pages.product_page import ProductPage
import pytest


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


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
