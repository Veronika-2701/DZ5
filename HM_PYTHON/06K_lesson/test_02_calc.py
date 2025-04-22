import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 50) 

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

driver.find_element(By.CSS_SELECTOR, "[type='text']").clear()
delay = driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)

seven = driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='7']").click()
plus = driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='+']").click()
eight = driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='8']").click()
eq = driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='=']").click()

wait.until(EC.invisibility_of_element(driver.find_element(By.ID, "spinner")))

@pytest.mark.parametrize("input", [
(driver.find_element(By.CLASS_NAME, "screen").text)
])
def test_res(input):
    assert input == "15"

driver.quit()