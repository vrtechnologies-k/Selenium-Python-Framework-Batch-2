import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def selectOptionByText(self, locator, Text):
        select = Select(locator)
        select.select_by_visible_text(Text)