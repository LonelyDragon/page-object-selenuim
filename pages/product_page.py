from pages.locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_card(self) -> None:
        # проверка на наличие кнопки перехода в корзину
        button = self.browser.find_elements(*ProductPageLocators.CARD_BUTTON)
        assert len(button) > 0, "Button is not exist"
        button[0].click()

    def is_valid_price_for_item(self) -> None:
        # проверка валидность суммы корзины
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text.split("&nbsp")[0]
        card_total_price = self.browser.find_element(
            *ProductPageLocators.CARD_TOTAL).text.split("&nbsp")[0]
        assert product_price == card_total_price, \
            f"The card contains more than one item or price is not valid\nProduct price: {product_price}\nCard total: {card_total_price}"

    def is_valid_item_in_card(self) -> None:
        # проверка, правильный ли товар попал в корзину
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        product_name_add = self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADD).text
        assert product_name == product_name_add, "Wrong item or empty add to card"

    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def element_should_disappear(self) -> None:
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should be disappear but not"
