import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.authoriz import Authorization
from pages.basket import Basket
from pages.checkout import Checkout

@pytest.fixture()
def driver1():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_search(driver1):
    page_auth = Authorization(driver1)
    page_auth.string_un("performance_glitch_user")
    page_auth.string_pw("secret_sauce")
    page_auth.button_log()
    page_basket = Basket(driver1)
    page_basket.remove()
    page_basket.backpack.click()
    page_basket.onesie.click()
    page_basket.bts.click()
    page_basket.basket()
    page_basket.cart_link.click()
    page_checkout = Checkout(driver1)
    page_checkout.check_but()
    page_checkout.check.click()
    page_checkout.data_fn("Vera")
    page_checkout.data_ln("Rapid")
    page_checkout.data_pc("345678")
    page_checkout.data_cont()
    page_checkout.cont.click()
    page_checkout.total_f()
    total = page_checkout.tot.text
    assert total == "Total: $58.29"



