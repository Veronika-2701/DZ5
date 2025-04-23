import pytest
import allure
from page.calculator import Calculator
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
@allure.title("инициализация драйвера")
@allure.description("Эта функция Инициализирует драйвер, устанавливает неявное ожидание 2 секунды и открывает окно браузера на весь экран. Затем получает URL, создают генератор, которые позволяют итерировать через последовательность данных, и закрывает браузер.")
@allure.feature("инициализация драйвера")
@allure.severity("blocker")
def driver():
    """Эта функция Инициализирует драйвер, устанавливает неявное ожидание 2 секунды и открывает окно браузера на весь экран.
    Затем получает URL, создают генератор, которые позволяют итерировать через последовательность данных, и закрывает браузер."""
    with allure.step("инициализация драйвера"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(2)
        driver.maximize_window()
    with allure.step("получение url и создание генератора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield driver
    with allure.step("закрытие драйвера"):
        driver.quit()

@allure.title("калькулятор")
@allure.description("Эта функция вызывает переменную Калькулятора класса и говорит, что связана с драйвером (функцией выше). Затем вызывает из класса функции delay и button. Потом из вызванной функции button вызывает четыре значения, на которые после вызыва нажмет. Вызовет функцию string_result, которая напечатает текст, и сравнит с результатом '15'.")
@allure.feature("калькулятор")
@allure.severity("blocker")
def test_calc(driver):
    """Эта функция вызывает переменную Калькулятора класса и говорит, что связана с драйвером (функцией выше).
    Затем вызывает из класса функции delay и button. 
    Потом из вызванной функции button вызывает четыре значения, на которые после вызыва нажмет.
    Вызовет функцию string_result, которая напечатает текст, и сравнит с результатом '15'."""
    with allure.step("калькулятор"):
        page = Calculator(driver)
    with allure.step("указание сколько ждать"):
        page.delay(5)
    with allure.step("выбор и нажатие на кнопки"):
        page.button()
        page.seven.click()
        page.plus.click()
        page.eight.click()
        page.eq.click()
    with allure.step("сравнение результата"):
        page.string_result()
        assert page.result == "15"



    