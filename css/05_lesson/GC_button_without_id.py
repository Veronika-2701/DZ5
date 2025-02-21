from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")
driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()

sleep(2)

driver.quit()