from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Калькулятор")
@allure.severity("blocker")
class Calculator: 
    """Этот класс представляет сущность Калькулятора."""
    @allure.id("инициализация калькультор")
    def __init__(self, driver):
        """Эта функция инициализирует драйвер"""
        self.driver = driver
        # self.driver.implicitly_wait(15)
        # self.driver.maximize_window()

    @allure.id("элемент delay")
    def delay(self, query: str):
        """Эта функция находит элемент delay и очищает строку.
        Затем подставляет в него значение 'query'."""
        self.d = self.driver.find_element(By.ID, "delay")
        self.d.clear()
        self.d.send_keys(query)

    @allure.id("элементы калькулятора")
    def button(self):
        """Эта функция находит элемент C."""
        self.c = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='top']/span[text()='C']")

        """Эта функция находит элемент 7."""
        self.seven = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='7']")
        
        """Эта функция находит элемент 8."""
        self.eight = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='8']")

        """Эта функция находит элемент 9."""
        self.nine = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='9']")

        """Эта функция находит элемент +."""
        self.plus = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='+']")

        """Эта функция находит элемент 4."""
        self.four = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='4']")

        """Эта функция находит элемент 5."""
        self.five = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='5']")

        """Эта функция находит элемент 6."""
        self.six = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='6']")

        """Эта функция находит элемент -."""
        self.minus = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='-']")

        """Эта функция находит элемент 1."""
        self.one = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='1']")

        """Эта функция находит элемент 2."""
        self.two = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='2']")

        """Эта функция находит элемент 3."""
        self.three = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='3']")

        """Эта функция находит элемент ÷."""
        self.division = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='÷']")

        """Эта функция находит элемент 0."""
        self.zero = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='0']")

        """Эта функция находит элемент . ."""
        self.point = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='.']")

        """Эта функция находит элемент =."""
        self.eq = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='=']")

        """Эта функция находит элемент x."""
        self.multiply = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='x']")

    @allure.id("результат")
    def string_result(self):
        """Эта функция находит элемент spinner и ждет 10 секунд пока элемент не изчезнет.
        Затем находит элемент screen и берет текст у данного элемента."""
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element(self.driver.find_element(By.ID, "spinner")))
        self.result = self.driver.find_element(By.CLASS_NAME, "screen").text
