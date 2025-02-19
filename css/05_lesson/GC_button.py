from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
button_add = driver.find_element(By.CSS_SELECTOR, "button")

for x in range(1, 6):
    button_add.click()

button_delete = driver.find_elements(By.CLASS_NAME, "added-manually")

print(f"Количество кнопок Delete: {len(button_delete)}")

sleep(10)

driver.quit()
