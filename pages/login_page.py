from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password) -> None:
        # регистация нового юзера
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_REG).click()

    def should_be_login_page(self) -> None:
        # проверка что, юзер стоит на странице логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "this is a not login url"

    def should_be_login_form(self) -> None:
        # проверка, что есть форма логина
        assert len(self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)) > 0, "can't find login form from page"

    def should_be_register_form(self) -> None:
        # проверка, что есть форма регистрации на странице
        assert len(self.browser.find_elements(*LoginPageLocators.PASSWORD_FORM)) > 0, "can't find password form from page"