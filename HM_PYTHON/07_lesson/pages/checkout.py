from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def check_but(self):
        self.check = self.driver.find_element(By.CSS_SELECTOR, "[id='checkout']")

    def data_fn(self, uiop):
        self.fn = self.driver.find_element(By.ID, ("first-name")) 
        self.fn.send_keys(uiop)

    def data_ln(self, asdfg):
        self.ln = self.driver.find_element(By.ID, ("last-name")) 
        self.ln.send_keys(asdfg)

    def data_pc(self, hjkl):
        self.pc = self.driver.find_element(By.ID, ("postal-code")) 
        self.pc.send_keys(hjkl)

    def data_cont(self):
        self.cont = self.driver.find_element(By.ID, ("continue")) 

    def total_f(self):
        self.tot = self.driver.find_element(By.CLASS_NAME, ("summary_total_label"))
        self.tt = self.tot.text
        print(self.tt)
