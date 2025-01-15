import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = None
    driver = webdriver.Chrome()
    yield driver
    driver.quit()