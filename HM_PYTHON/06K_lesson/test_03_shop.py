import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 50) 

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, ("user-name")).send_keys("standard_user")
driver.find_element(By.ID, ("password")).send_keys("secret_sauce")
driver.find_element(By.ID, ("login-button")).click()

driver.get("https://www.saucedemo.com/inventory.html")

driver.find_element(By.ID, ("add-to-cart-sauce-labs-backpack")).click()
driver.find_element(By.ID, ("add-to-cart-sauce-labs-bolt-t-shirt")).click()
driver.find_element(By.ID, ("add-to-cart-sauce-labs-onesie")).click()


driver.find_element(By.CLASS_NAME, ("shopping_cart_link")).click()

driver.get("https://www.saucedemo.com/cart.html")
driver.find_element(By.ID, ("checkout")).click()

driver.get("https://www.saucedemo.com/checkout-step-one.html")
driver.find_element(By.ID, ("first-name")).send_keys("Vera")
driver.find_element(By.ID, ("last-name")).send_keys("Rapid")
driver.find_element(By.ID, ("postal-code")).send_keys("345678")
driver.find_element(By.ID, ("continue")).click()

driver.get("https://www.saucedemo.com/checkout-step-two.html")

@pytest.mark.parametrize("total", [
    (driver.find_element(By.CLASS_NAME, ("summary_total_label")).text)
])
def test_total(total):
    assert total == "Total: $58.29"

driver.quit()
