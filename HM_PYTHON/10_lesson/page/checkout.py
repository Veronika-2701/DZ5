from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Корзина")
@allure.severity("blocker")
class Checkout:
    """Этот класс представляет сущность Корзины"""

    @allure.id("инициализация корзины")
    def __init__(self, driver):
        """Эта функция инициализирует драйвер"""
        self.driver = driver
        # self.driver.implicitly_wait(15)
        # self.driver.maximize_window()

    @allure.id("переход к форме")
    def check_but(self):
        """Эта функция находит элемент checkout."""
        self.check = self.driver.find_element(By.CSS_SELECTOR, "[id='checkout']")

    @allure.id("поле имя")
    def data_fn(self, uiop: str):
        """Эта функция находит элемент first-name и подставляет в него значение 'uiop'."""
        self.fn = self.driver.find_element(By.ID, ("first-name"))
        self.fn.send_keys(uiop)

    @allure.id("поле фамилия")
    def data_ln(self, asdfg: str):
        """Эта функция находит элемент last-name и подставляет в него значение 'asdfg'."""
        self.ln = self.driver.find_element(By.ID, ("last-name"))
        self.ln.send_keys(asdfg)

    @allure.id("поле код")
    def data_pc(self, hjkl: str):
        """Эта функция находит элемент postal-code и подставляет в него значение 'hjkl'."""
        self.pc = self.driver.find_element(By.ID, ("postal-code"))
        self.pc.send_keys(hjkl)

    @allure.id("переход к результату")
    def data_cont(self):
        """Эта функция находит элемент continue."""
        self.cont = self.driver.find_element(By.ID, ("continue")) 

    @allure.id("результат")
    def total_f(self):
        """Эта функция находит элемент summary_total_label и берет у этого элемента текст.
        Звтем печатает текст с этого элемента."""
        self.tot = self.driver.find_element(By.CLASS_NAME, ("summary_total_label"))
        self.tt = self.tot.text
        print(self.tt)
