from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 20) 

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-footer>p"))).click()

driver.quit()
