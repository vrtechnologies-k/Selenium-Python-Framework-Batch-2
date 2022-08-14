import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_placeOrder(self):

        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

        self.driver.find_element(By.CLASS_NAME, 'search-keyword').send_keys('ber')

        time.sleep(4)

        vegtables = self.driver.find_elements(By.CSS_SELECTOR, '.products .product')

        print(len(vegtables))

        buttons = self.driver.find_elements(By.XPATH, '//div[@class="product"]/div/button')
        list1 = []
        list2 = []
        for button in buttons:
            vegnames = button.find_element(By.XPATH, 'parent::div/parent::div/h4').text
            assert "ber" in vegnames
            list1.append(vegnames)
            button.click()

        self.driver.find_element(By.CLASS_NAME, 'cart-icon').click()

        self.driver.find_element(By.XPATH, "//button[contains(.,'PROCEED TO CHECKOUT')]").click()

        time.sleep(3)

        productnames = self.driver.find_elements(By.CSS_SELECTOR, '.product-name')

        for product in productnames:
            vegname = product.text
            list2.append(vegname)

        print(list1)
        print(list2)

        assert list1 == list2
        sum = 0
        eachproductprice = self.driver.find_elements(By.XPATH, "//table[@id='productCartTables']/tbody/tr/td[5]")

        for price in eachproductprice:
            productprice = price.text
            sum = sum + int(productprice)  # 48+160+180

        totalprice = self.driver.find_element(By.CSS_SELECTOR, '.totAmt').text

        assert sum == int(totalprice)

        self.driver.find_element(By.CLASS_NAME, 'promoCode').send_keys("rahulshettyacademy")

        self.driver.find_element(By.CLASS_NAME, 'promoBtn').click()

        # time.sleep(10)

        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))

        promoinfo = self.driver.find_element(By.CLASS_NAME, 'promoInfo').text

        assert "Code applied" in promoinfo

        discountAmount = self.driver.find_element(By.CLASS_NAME, 'discountAmt').text

        assert sum > float(discountAmount)

        self.driver.find_element(By.XPATH, "//button[contains(.,'Place Order')]").click()

        Select(self.driver.find_element(By.TAG_NAME, 'select')).select_by_visible_text("India")

        self.driver.find_element(By.CLASS_NAME, 'chkAgree').click()

        self.driver.find_element(By.XPATH, "//button[contains(.,'Proceed')]").click()

        time.sleep(10)
