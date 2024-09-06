from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_standard_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling form
    login_page.type_username("standard_user")
    login_page.type_password('secret_sauce')
    login_page.click_login_button()

    # Validation of redirection
    products_page = ProductsPage(browser=browser)
    products_page.validate_products_page_title()
    products_page.validate_products_page_url()
