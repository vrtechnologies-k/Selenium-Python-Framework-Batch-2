import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.formSubmissionData import formSubmissionData
from pageObjects.HomePage import HomePage
from tests.conftest import driver
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_submitForm(self,getData):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["Name"])
        homePage.getEmail().send_keys(getData["Email"])
        homePage.getPassword().send_keys(getData["Password"])
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(),getData["Gender"])
        homePage.getRadio().click()
        homePage.getBday().send_keys(getData["DOB"])
        homePage.getSubmit().click()
        time.sleep(2)
        sucMessage = homePage.getAlert().text
        print(sucMessage)
        assert "Success!" in sucMessage

    def test_sample(self):
        print("sample test")

    #@pytest.fixture(params=[("venkat","venkat@gmail.com","venkat@123","Male","01-08-1988"),("Sreelatha","Sreelatha@gmail.com","Sreelatha@123","Female","01-01-1994")])
    #def getData(self,request):
        #return request.param

    @pytest.fixture(params=formSubmissionData.test_formSubmissionData)
    def getData(self,request):
        return request.param
