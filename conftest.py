import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # after test
    # driver.quit() # Closing Browser
    sleep(3)
