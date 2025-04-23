from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

@allure.epic("Авторизация")
@allure.severity("blocker")
class Authorization:
    """Этот класс представляет сущность Авторизации"""

    @allure.id("инициализация авторизации")
    def __init__(self, driver):
        """Эта функция инициализирует драйвер"""
        self.driver = driver
        # self.driver.implicitly_wait(15)
        # self.driver.maximize_window()   

    @allure.id("логин")
    def string_un(self, query: str):
        """Эта функция находит элемент user-name и подставляет в него значение 'query'."""
        self.username = self.driver.find_element(By.ID, ("user-name"))
        self.username.send_keys(query)

    @allure.id("пароль")
    def string_pw(self, qwerty: str):
        """Эта функция находит элемент password и подставляет в него значение 'qwerty'."""
        self.password = self.driver.find_element(By.ID, ("password"))
        self.password.send_keys(qwerty)

    @allure.id("кнока авторизации")
    def button_log(self):
        """Эта функция находит элемент login-button и нажимает на него (в данном случае нажимает на кнопку RETURN)."""
        self.button = self.driver.find_element(By.ID, ("login-button"))
        self.button.send_keys(Keys.RETURN)

    