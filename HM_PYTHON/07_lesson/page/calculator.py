from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def delay(self, query):
        self.d = self.driver.find_element(By.ID, "delay")
        self.d.clear()
        self.d.send_keys(query)

    def button(self):
        self.c = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='top']/span[text()='C']")
        self.seven = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='7']")
        self.eight = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='8']")
        self.nine = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='9']")
        self.plus = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='+']")
        self.four = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='4']")
        self.five = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='5']")
        self.six = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='6']")
        self.minus = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='-']")
        self.one = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='1']")
        self.two = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='2']")
        self.three = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='3']")
        self.division = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='÷']")
        self.zero = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='0']")
        self.point = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='.']")
        self.eq = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='=']")
        self.multiply = self.driver.find_element(By.XPATH, ".//div[@id='calculator']/div[@class='keys']/span[text()='x']")

    def string_result(self):
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element(self.driver.find_element(By.ID, "spinner")))
        self.result = self.driver.find_element(By.CLASS_NAME, "screen").text
