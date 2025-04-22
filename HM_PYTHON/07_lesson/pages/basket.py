from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basket:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def remove(self):
        self.backpack = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.bts = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt") 
        self.onesie = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        self.bl = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light") 
        self.fj = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
        self.tsr = self.driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-test.allthethings()-t-shirt-(red)']")

    def basket(self):
        self.cart_link = self.driver.find_element(By.CLASS_NAME, ("shopping_cart_link")) 