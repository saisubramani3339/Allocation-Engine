import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import openpyxl


# @pytest.fixture()
# def test_setup():
#     global driver
#     chrome_options = ChromeOptions()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     browser_url = driver.get('https://allocationenginedev.service-now.com/ae')
#     yield
#     driver.quit()
#
# def test_01(test_setup):
#     User_name = driver.find_element(By.XPATH, "//input[@id='username']")
#     User_name.send_keys("sai.subramaniam")
#     Password = driver.find_element(By.XPATH, "//input[@id='password']")
#     Password.send_keys("Iopex@2023")
#     Login_Button = driver.find_element(By.XPATH, "//button[@type='submit']")
#     Login_Button.click()
#     settings = driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[10]").click()
#     role = driver.find_element(By.XPATH, "(//div[@role='button'])[2]").click()
#     role_user = driver.find_element(By.XPATH, "//p[contains(text(), ' Assign Role to user')]").click()
#     adduser = driver.find_element(By.XPATH, "(//button[@id='btn-add'])[2]").click()
#     adduser_drpd = driver.find_element(By.XPATH, "//span[@class='select2-arrow']").click()
#     adduser_textbox = driver.find_element(By.XPATH, "//input[@class='select2-input']").send_keys("amit tukaram")
#     driver.find_element(By.XPATH, "//input[@class='select2-input']").send_keys(Keys.ENTER)
#     ele = driver.find_element(By.XPATH, "//select[@id='add_user_role']")
#     drp = Select(ele)
#     drp.select_by_visible_text('AE Super Admin')
#     time.sleep(7)


