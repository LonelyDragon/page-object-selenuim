from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[text()='View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    PASSWORD_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REG_PASS = (By.XPATH, "//input[@name='registration-password1']")
    REG_PASS_CONFIRM = (By.XPATH, "//input[@name='registration-password2']")
    CONFIRM_REG = (By.NAME, "registration_submit")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CARD_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_ADD = (By.CSS_SELECTOR, ".alertinner strong")
    CARD_BUTTON = (By.CSS_SELECTOR, ".product_main form button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    ITEMS_CONTAINER = (By.XPATH, "//div[@id='content_inner']")
    TEXT_OF_EMPTY_LIST = (By.XPATH, "//div[@id='content_inner']/p")
