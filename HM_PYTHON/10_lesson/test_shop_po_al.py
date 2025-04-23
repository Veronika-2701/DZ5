import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.authoriz import Authorization
from page.basket import Basket
from page.checkout import Checkout

@pytest.fixture()
@allure.title("инициализация драйвера")
@allure.description("Эта функция Инициализирует драйвер, устанавливает неявное ожидание 2 секунды и открывает окно браузера на весь экран. Затем получает URL, создают генератор, которые позволяют итерировать через последовательность данных, и закрывает браузер.")
@allure.feature("инициализация драйвера")
@allure.severity("blocker")
def driver1():
    with allure.step("инициализация драйвера"):
        global driver
        driver = webdriver.Firefox()
        driver.implicitly_wait(2)
        driver.maximize_window()
    with allure.step("получение url и создание генератора"):
        driver.get("https://www.saucedemo.com/")
        yield driver
    with allure.step("закрытие драйвера"):
        driver.quit()

@allure.title("авторизация")
@allure.description("Эта функция вызывает переменную Авторизации класса и говорит, что связана с драйвером (функцией выше). Затем вызывает из класса функции string_un и string_pw, подставляет новые значения юзера и пароля соответственно и нажимает на кнопку из функции button_log.")
@allure.feature("авторизация")
@allure.severity("blocker")
def test_auth(driver1):
    with allure.step("авторизация"):
        page_auth = Authorization(driver1)
        with allure.step("введение логина и пароля"):
            page_auth.string_un("performance_glitch_user")
            page_auth.string_pw("secret_sauce")
        with allure.step("передна главную страницу"):
            page_auth.button_log()

@allure.title("Главная страница")
@allure.description("Дальше функция вызывает переменную Главной страницы класса и говорит, что связана с драйвером (функцией выше). Вызывает функцию remove, нажимает на нужные товары. Вызывает функцию basket и переходит в корзину.")
@allure.feature("Главная страница")
@allure.severity("blocker")
def test_basket(driver1):
    test_auth(driver1)
    with allure.step("Главная страница"):
        page_basket = Basket(driver1)
        with allure.step("клик на товаре"):
            page_basket.remove()
            page_basket.backpack.click()
            page_basket.onesie.click()
            page_basket.bts.click()
        with allure.step("переход в корзину"):
            page_basket.basket()
            page_basket.cart_link.click()

@allure.title("Корзина")
@allure.description("Дальше функция вызывает переменную Корзины класса  говорит, что связана с драйвером (функцией выше). Вызывает функцию check_but и кнопку check, затем нажимает на нее. В четыре пустых поля подставляет значения. Вызывает функцию data_cont и кнопку cont, затем нажимает на нее.")
@allure.feature("Корзина")
@allure.severity("blocker")
def test_check(driver1):
    test_basket(driver1)
    with allure.step("Корзина"):
        page_checkout = Checkout(driver1)
        with allure.step("задать форме значение полей"):
            page_checkout.check_but()
            page_checkout.check.click()
            page_checkout.data_fn("Vera")
            page_checkout.data_ln("Rapid")
            page_checkout.data_pc("345678")
        with allure.step("переход к результату тотал"):
            page_checkout.data_cont()
            page_checkout.cont.click()

@allure.title("сравнить значение тотал")
@allure.description("Вызывает функцию total_f и элемент tot, где будет вытащен текст. Затем сравнит значение текста элемента и Тотал.")
@allure.feature("сравнить значение тотал")
@allure.severity("blocker")
def test_total(driver1):
    test_check(driver1)
    with allure.step("сравнить значение тотал"):
        page_checkout = Checkout(driver1)
        page_checkout.total_f()
        total = page_checkout.tot.text
        assert total == "Total: $58.29"