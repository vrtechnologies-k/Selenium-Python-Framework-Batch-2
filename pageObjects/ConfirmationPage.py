from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.TAG_NAME,'select')
    checkBox = (By.CLASS_NAME,'chkAgree')
    processed = (By.XPATH,"//button[contains(.,'Proceed')]")

    def getCountry(self):
        return self.driver.find_element(*ConfirmationPage.country)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmationPage.checkBox)

    def getProcessed(self):
        return self.driver.find_element(*ConfirmationPage.processed)