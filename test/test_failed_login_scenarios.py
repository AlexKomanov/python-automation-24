from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_locked_out_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling form
    login_page.type_username("locked_out_user")
    login_page.type_password('secret_sauce')
    login_page.click_login_button()

    # Validation of Error message
    error_message_text = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    print(f"{error_message_text = }")
    assert error_message_text == """Epic sadface: Sorry, this user has been locked out."""
