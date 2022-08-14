from selenium.webdriver.common.by import By

from tests.conftest import driver


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, 'name')
    email = (By.NAME,'email')
    password = (By.ID,'exampleInputPassword1')
    checkbox = (By.ID,'exampleCheck1')
    gender = (By.ID,'exampleFormControlSelect1')
    radio = (By.ID,'inlineRadio2')
    bday = (By.ID,'bday')
    submit = (By.CSS_SELECTOR,"[class*='btn-success']")
    alert = (By.CSS_SELECTOR,"[class*='alert-success']")

    def getName(self):
        self.driver.find_element(*HomePage.name)

    def getEmail(self):
        self.driver.find_element(*HomePage.email)

    def getPassword(self):
        self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        self.driver.find_element(*HomePage.gender)

    def getRadio(self):
        self.driver.find_element(*HomePage.radio)

    def getBday(self):
        self.driver.find_element(*HomePage.bday)

    def getSubmit(self):
        self.driver.find_element(*HomePage.submit)

    def getAlert(self):
        self.driver.find_element(*HomePage.alert)