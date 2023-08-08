import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class rolespage:
    settings = "(//li[@data-toggle='tooltip'])[10]"
    user_role = "(//div[@role='button'])[2]"
    role_user = "//p[contains(text(), ' Assign Role to user')]"
    search = "//input[@id='myInput']"
    delete = "//*[@id='svg_delete_user']"
    edit = "(//*[@id='svg_edit_user'])[1]"
    add_user = "(//button[@id='btn-add'])[2]"
    user_id = "//*[@id='s2id_autogen3']"
    select_user = "//input[@id='s2id_autogen4_search']"
    delete_user_cancel = "(//button[@class='btn btn-default'])[4]"
    delete_user_delet = "(//button[@class='btn btn-default save_btn'])[3]"
    adduser = "(//button[@id='btn-add'])[2]"
    adduser_drpd = "//span[@class='select2-arrow']"
    adduser_textbox = "//input[@class='select2-input']"
    userclick = "//li[@role='presentation']"
    selectrole = "//select[@id='add_user_role']"
    rolename = "(//option[@id='input_roleid'])[4]"
    addusersave = "(//button[@id='submit_id'])[2]"
    rolestab = "//p[contains(text(), 'Roles')]"
    addrole = "(//button[@id='btn-add'])[1]"
    roletext = "(//input[@role='textbox'])[2]"
    addrolesave = "(//button[@value='Submit'])[1]"
    editussave = "(//button[@id='submit_id'])[1]"
    ampassword = "//input[@id='password']"
    amusername = "//input[@id='username']"
    roleconfig = "(//*[@id='configure'])[7]"
    alloca = "(//li[@data-toggle='tooltip'])[3]"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def SetUsername(self, amusername):
        self.driver.find_element(By.XPATH, self.amusername).clear()
        self.driver.find_element(By.XPATH, self.amusername).send_keys(amusername)

    def Setpassword(self, ampassword):
        self.driver.find_element(By.XPATH, self.ampassword).clear()
        self.driver.find_element(By.XPATH, self.ampassword).send_keys(ampassword)

    def click_settings(self):
        self.driver.find_element(By.XPATH, self.settings).click()

    def User_mang(self):
        self.driver.find_element(By.XPATH, self.user_role).click()

    def getrole_user(self):
        self.driver.find_element(By.XPATH, self.role_user).click()

    def getSearch(self, role):
        self.driver.find_element(By.XPATH, self.search).clear()
        self.driver.find_element(By.XPATH, self.search).send_keys(role)
        self.driver.find_element(By.XPATH, self.search).send_keys(Keys.ENTER)

    def delete_user(self):
        self.driver.find_element(By.XPATH, self.delete).click()

    def del_user_cancel(self):
        self.driver.find_element(By.XPATH, self.delete_user_cancel).click()

    def del_user(self):
        self.driver.find_element(By.XPATH, self.delete_user_delet).click()

    def add_user_btn(self):
        self.driver.find_element(By.XPATH, self.adduser).click()

    def add_user_drp(self):
        self.driver.find_element(By.XPATH, self.adduser_drpd).click()

    def adduser_txt_box(self, usname):
        self.driver.find_element(By.XPATH, self.adduser_textbox).send_keys(usname)

    def click_user(self):
        self.driver.find_element(By.XPATH, self.userclick).click()

    def select_role(self):
        self.driver.find_element(By.XPATH, self.selectrole).click()

    def role_name(self):
        self.driver.find_element(By.XPATH, self.rolename).click()

    def add_usersave(self):
        self.driver.find_element(By.XPATH, self.addusersave).click()

    def tab_roles(self):
        self.driver.find_element(By.XPATH, self.rolestab).click()

    def add_role(self):
        self.driver.find_element(By.XPATH, self.addrole).click()

    def role_txt(self, roletext):
        self.driver.find_element(By.XPATH, self.roletext).send_keys(roletext)

    def add_role_save_btn(self):
        self.driver.find_element(By.XPATH, self.addrolesave).click()

    def uedit(self):
        self.driver.find_element(By.XPATH, self.edit).click()

    def editus_save(self):
        self.driver.find_element(By.XPATH, self.editussave).click()

    def role_config(self):
        self.driver.find_element(By.XPATH, self.roleconfig).click()

    def get_alloca(self):
        self.driver.find_element(By.XPATH, self.alloca).click()
