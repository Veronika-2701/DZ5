from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Главная страница")
@allure.severity("blocker")
class Basket:
    """Этот класс представляет сущность Главной страницы"""

    @allure.id("инициализация главной страницы")
    def __init__(self, driver):
        """Эта функция инициализирует драйвер"""
        self.driver = driver
        # self.driver.implicitly_wait(15)
        # self.driver.maximize_window()

    @allure.id("элементы главной страницы")
    def remove(self):
        """Эта функция находит элемент backpack."""
        self.backpack = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")

        """Эта функция находит элемент bolt-t-shirt."""
        self.bts = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")

        """Эта функция находит элемент onesie."""
        self.onesie = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")

        """Эта функция находит элемент bike-light."""
        self.bl = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")

        """Эта функция находит элемент fleece-jacket."""
        self.fj = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")

        """Эта функция находит элемент t-shirt-(red)."""
        self.tsr = self.driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-test.allthethings()-t-shirt-(red)']")

    @allure.id("переход в корзину")
    def basket(self):
        """Эта функция находит элемент shopping_cart_link(значок корзины)."""
        self.cart_link = self.driver.find_element(By.CLASS_NAME, ("shopping_cart_link")) 