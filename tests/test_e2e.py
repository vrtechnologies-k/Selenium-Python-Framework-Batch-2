import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmationPage import ConfirmationPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_placeOrder(self):

        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

        checkoutPage = CheckoutPage(self.driver)

        checkoutPage.getKeyword().send_keys('ber')

        time.sleep(4)
        veg_tables = checkoutPage.getvegTables()
        print(len(veg_tables))

        buttons = checkoutPage.getButtons()
        list1 = []
        list2 = []
        for button in buttons:
            vegnames = button.find_element(By.XPATH, 'parent::div/parent::div/h4').text
            assert "ber" in vegnames
            list1.append(vegnames)
            button.click()

        checkoutPage.getcartIcon().click()
        time.sleep(3)
        checkoutPage.getcheckOut().click()

        time.sleep(3)

        productnames = checkoutPage.getproductName()
        print(len(productnames))
        for product in productnames:
            vegname = product.text
            list2.append(vegname)

        print(list1)
        print(list2)

        assert list1 == list2
        sum = 0

        eachproductprice = checkoutPage.getproductPrices()

        for price in eachproductprice:
            productprice = price.text
            sum = sum + int(productprice)  # 48+160+180

        totalprice = checkoutPage.gettotalAmount().text

        assert sum == int(totalprice)
        checkoutPage.getpromoCode().send_keys("rahulshettyacademy")
        checkoutPage.getpromoButton().click()

        self.verifyelementPresent('promoInfo')

        promoinfo = checkoutPage.getpromoInfo().text

        assert "Code applied" in promoinfo

        discountAmount = checkoutPage.getdiscountAmount().text

        assert sum > float(discountAmount)
        checkoutPage.getplaceOrder().click()

        confirmPage = ConfirmationPage(self.driver)

        Select(confirmPage.getCountry()).select_by_visible_text("India")

        confirmPage.getCheckBox().click()

        confirmPage.getProcessed().click()

        time.sleep(10)
