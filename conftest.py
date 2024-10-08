import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # after test
    # driver.quit() # Closing Browser
    sleep(3)
