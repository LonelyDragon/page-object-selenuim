from pages.login_page import LoginPage


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
