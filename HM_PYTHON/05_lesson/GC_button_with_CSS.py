from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")
button_add = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.btn-test").click()

sleep(2)

driver.quit()