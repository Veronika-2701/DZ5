from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Authorization:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()   

    def string_un(self, query):
        self.username = self.driver.find_element(By.ID, ("user-name"))
        self.username.send_keys(query)

    def string_pw(self, qwerty):
        self.password = self.driver.find_element(By.ID, ("password")) 
        self.password.send_keys(qwerty)

    def button_log(self): 
        self.button = self.driver.find_element(By.ID, ("login-button"))  
        self.button.send_keys(Keys.RETURN)

    