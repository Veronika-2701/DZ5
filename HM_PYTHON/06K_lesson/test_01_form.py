import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys("")
driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
country = driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
e_mail = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
phone = driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
company = driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

driver.find_element(By.CLASS_NAME, "btn.btn-outline-primary.mt-3").click()

@pytest.mark.parametrize("class_red", [
    (driver.find_element(By.ID,'zip-code').get_attribute('class'))
])
def test_zk(class_red):
    assert class_red == "alert py-2 alert-danger"

@pytest.mark.parametrize("class_green", [
    (driver.find_element(By.ID, "first-name").get_attribute("class")), 
    (driver.find_element(By.ID, "last-name").get_attribute("class")),
    (driver.find_element(By.ID, "address").get_attribute("class")),
    (driver.find_element(By.ID, "city").get_attribute("class")),
    (driver.find_element(By.ID, "country").get_attribute("class")),
    (driver.find_element(By.ID, "e-mail").get_attribute("class")),
    (driver.find_element(By.ID, "phone").get_attribute("class")),
    (driver.find_element(By.ID, "job-position").get_attribute("class")),
    (driver.find_element(By.ID, "company").get_attribute("class"))
])
def test_assert(class_green):
    assert class_green == "alert py-2 alert-success"

driver.quit()