import pytest
from page.calculator import Calculator
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def test_search(driver):
    page = Calculator(driver)
    page.delay(5)
    page.button()
    page.seven.click()
    page.plus.click()
    page.eight.click()
    page.eq.click()
    
    page.string_result()
    assert page.result == "15"



    