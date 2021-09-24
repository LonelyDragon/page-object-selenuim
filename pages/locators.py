from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    PASSWORD_FORM = (By.ID, "register_form")

class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CARD_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_ADD = (By.CSS_SELECTOR, ".alertinner strong")
    CARD_BUTTON = (By.CSS_SELECTOR, ".product_main form button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")