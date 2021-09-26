from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def product_list_must_be_empty(self) -> None:
        # проверка на наличие итемов в корзине
        assert self.browser.find_elements(
            *BasketPageLocators.ITEMS_CONTAINER), "basket does not empty"

    def product_list_must_contain_a_message_about_the_empty_basket(self) -> None:
        # проверка на наличие сообщения об отсутствии товаров в корзине. EN
        assert self.browser.find_element(
            *BasketPageLocators.TEXT_OF_EMPTY_LIST).text == "Your basket is empty. Continue shopping",\
            "basket does not contains text"
