import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def selectOptionByText(self, locator, Text):
        select = Select(locator)
        select.select_by_visible_text(Text)

    def verifyelementPresent(self,className):
        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, className)))
