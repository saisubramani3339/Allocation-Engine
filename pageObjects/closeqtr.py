import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



class classqtrpage:
    nav_cls_qtr = "(//li[@data-toggle='tooltip'])[9]"
    cls_qtr_btn = "//button[@id='closequarter']"
    download = "//button[@ng-click='ExportReporttoExcel()']"
    next = "//a[@id='closeqater_next']"
    previous = "//a[@id='closeqater_previous']"
    master_data = "(//li[@data-toggle='tooltip'])[4]"
    Historical_data = "//*[@id='nav-HistoricalData-tab']"
    hissearch = "//input[@id='myInput']"
    Yes = "(//button[@type='button'])[3]"
    No = "(//button[@type='button'])[4]"



    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def nav_close(self):
        self.driver.find_element(By.XPATH, self.nav_cls_qtr).click()

    def download_btn(self):
        self.driver.find_element(By.XPATH, self.download).click()

    def master(self):
        self.driver.find_element(By.XPATH, self.master_data).click()

    def Historical(self):
        self.driver.find_element(By.XPATH, self.Historical_data).click()

    def his_search(self, hissearch):
        self.driver.find_element(By.XPATH, self.hissearch).clear()
        self.driver.find_element(By.XPATH, self.hissearch).send_keys(hissearch)

    def close_quarter(self):
        self.driver.find_element(By.XPATH, self.cls_qtr_btn).click()

    def yes_btn(self):
        self.driver.find_element(By.XPATH, self.Yes).click()

    def No_btn(self):
        self.driver.find_element(By.XPATH, self.No).click()


