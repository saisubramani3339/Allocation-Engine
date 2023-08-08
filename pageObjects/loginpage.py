import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



class loginpage:
    User_name = "//input[@id='username']"
    Password =  "//input[@id='password']"
    Login_Button = "//button[@type='submit']"
    profile_icon = "//span[@Id='dropdownMenuButton']"
    logout = "//a[@class='dropdown-item']"
    page_name = "(//h2[@class='heading mb-4'])[1]"
    Errormessage = "//div[contains(text(), 'User name or password invalid')]"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def SetUsername(self, username):
        self.driver.find_element(By.XPATH, self.User_name).clear()
        self.driver.find_element(By.XPATH, self.User_name).send_keys(username)


    def Setpassword(self, password):
        self.driver.find_element(By.XPATH, self.Password).clear()
        self.driver.find_element(By.XPATH, self.Password).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.Login_Button).click()

    def Clickprofile(self):
        self.driver.find_element(By.XPATH, self.profile_icon).click()

    def Clicklogout(self):
        self.driver.find_element(By.XPATH, self.logout).click()

    def Pagename(self):
        self.driver.find_element(By.XPATH, self.page_name).text()

    def getErrormessage(self):
        self.driver.find_element(By.XPATH, self.Errormessage).text()

