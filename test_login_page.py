from pages.login_page import LoginPage
from pages.main_page import MainPage


url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_can_find_login_page(browser):
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_url()

def test_login_form_exists(browser):
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_form()

def test_register_form_exists(browser):
    page = LoginPage(browser, url)
    page.open()
    page.should_be_register_form()

def test_login_func_element_exists(browser):
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_page

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()