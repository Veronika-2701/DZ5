from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

div = driver.find_element(By.ID, "image-container")
award = div.find_element(By.ID, "award")

print(award.get_attribute("src"))

driver.quit()