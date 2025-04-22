from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()

green_element = driver.find_element(By.CSS_SELECTOR, "#content")
text_in_element = green_element.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(text_in_element)

driver.quit()

