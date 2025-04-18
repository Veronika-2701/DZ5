from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("http://uitestingplayground.com/textinput")

input = driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")

button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

text_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(text_button)

driver.quit()