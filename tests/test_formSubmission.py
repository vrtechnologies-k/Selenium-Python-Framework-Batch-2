import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from tests.conftest import driver
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_submitForm(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")

        homePage = HomePage(self.driver)
        homePage.getName().send_keys("venkat")
        homePage.getEmail().send_keys("venkat@gmail.com")
        homePage.getPassword().send_keys("venkat@123")
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(),"Male")
        homePage.getRadio().click()
        homePage.getBday().send_keys("01-08-1988")
        homePage.getSubmit().click()
        time.sleep(2)
        sucMessage = homePage.getAlert().text
        print(sucMessage)
        assert "Success!" in sucMessage

    def test_sample(self):
        print("sample test")
