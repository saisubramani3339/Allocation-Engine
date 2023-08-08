import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pageObjects.loginpage import loginpage
from pageObjects.rolespage import rolespage
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGen

class Test_01_rol():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    role = ReadConfig.getrole_name()
    usname = ReadConfig.get_adduser_name()
    roletext = ReadConfig.role_text()
    amusername = ReadConfig.amusername()
    ampassword = ReadConfig.ampassword()



    logger = LogGen.loggen()

    def test_id_001(self, test_setup):
        self.logger.info("*****Test_01_Settings*****")
        self.logger.info("*****Execution Started for test_id_001*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        page_name = self.driver.find_element(By.XPATH, "//h2[@class='heading mb-1']").text
        if page_name == 'Configuration':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_001 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_001.png")
            self.driver.close()
            self.logger.error("*****test_id_001 Failed*****")
            assert False

    def test_id_002(self, test_setup):
        self.logger.info("*****Execution Started for test_id_002*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        page_name = self.driver.find_element(By.XPATH, "//p[contains(text(),'Roles')]")
        if page_name.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_002 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_002.png")
            self.driver.close()
            self.logger.error("*****test_id_002 Failed*****")
            assert False

    def test_id_003(self, test_setup):
        self.logger.info("*****Execution Started for test_id_003*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.getrole_user()
        time.sleep(5)
        page_name = self.driver.find_element(By.XPATH, "//p[contains(text(), ' Assign Role to user')]")
        if page_name.is_enabled():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_003 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_003.png")
            self.driver.close()
            self.logger.error("*****test_id_003 Failed*****")
            assert False

    def test_id_004(self, test_setup):
        self.logger.info("*****Execution Started for test_id_004*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.getrole_user()
        search = self.driver.find_element(By.XPATH, "//input[@id='myInput']")
        if search.is_enabled():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_004 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_004.png")
            self.driver.close()
            self.logger.error("*****test_id_004 Failed*****")
            assert False

    def test_id_005(self, test_setup):
        self.logger.info("*****Execution Started for test_id_005*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.getrole_user()
        self.rp.getSearch(self.role)
        search_result = self.driver.find_element(By.XPATH, "//*[@id='user_table']/tbody/tr[1]")
        if search_result.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_005 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_005.png")
            self.driver.close()
            self.logger.error("*****test_id_005 Failed*****")
            assert False

    def test_id_006(self, test_setup):
        self.logger.info("*****Execution Started for test_id_006*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.getrole_user()
        self.rp.getSearch(self.role)
        time.sleep(2)
        self.rp.delete_user()
        close_icon = self.driver.find_element(By.XPATH, "(//button[@data-dismiss='modal'])[7]")
        if close_icon.is_enabled():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_006 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_006.png")
            self.driver.close()
            self.logger.error("*****test_id_006 Failed*****")
            assert False

    def test_id_007(self, test_setup):
        self.logger.info("*****Execution Started for test_id_006*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.getrole_user()
        self.rp.getSearch(self.role)
        self.rp.delete_user()
        self.rp.del_user_cancel()
        search_result = self.driver.find_element(By.XPATH, "//*[@id='user_table']/tbody/tr[1]")
        if search_result.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_007 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_007.png")
            self.driver.close()
            self.logger.error("*****test_id_007 Failed*****")
            assert False

    def test_id_008(self, test_setup):
        self.logger.info("*****Execution Started for test_id_008*****")
        self.driver = test_setup
        self.driver.implicitly_wait(55)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.getrole_user()
        self.rp.getSearch(self.role)
        self.rp.delete_user()
        self.rp.del_user()
        time.sleep(15)
        search = self.driver.find_element(By.XPATH, "//input[@id='myInput']").clear()
        search_txt = self.driver.find_element(By.XPATH, "//input[@id='myInput']").send_keys('amit.tuk')
        search_result = self.driver.find_element(By.XPATH, "(//td[@class='dataTables_empty'])[2]")
        if search_result.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_008 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_008.png")
            self.driver.close()
            self.logger.error("*****test_id_008 Failed*****")
            assert False

    def test_id_009(self, test_setup):
        self.logger.info("*****Execution Started for test_id_009*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.getrole_user()
        self.rp.add_user_btn()
        self.rp.add_user_drp()
        adduser_textbox = self.driver.find_element(By.XPATH, "//input[@class='select2-input']").send_keys("amit tukaram")
        self.driver.find_element(By.XPATH, "//input[@class='select2-input']").send_keys(Keys.ENTER)
        ele = self.driver.find_element(By.XPATH, "//select[@id='add_user_role']")
        drp = Select(ele)
        drp.select_by_visible_text('AE Super Admin')
        self.rp.add_usersave()
        search_result = self.driver.find_element(By.XPATH, "//*[@id='user_table']/tbody/tr[1]")
        if search_result.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_009 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_009.png")
            self.driver.close()
            self.logger.error("*****test_id_009 Failed*****")
            assert False

    def test_id_010(self, test_setup):
        self.logger.info("*****Execution Started for test_id_010*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.add_role()
        pop_up_close = self.driver.find_element(By.XPATH, "(//button[@type='button'])[3]")
        if pop_up_close.is_enabled():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_010 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_010.png")
            self.driver.close()
            self.logger.error("*****test_id_010 Failed*****")
            assert False

    def test_id_011(self, test_setup):
        self.logger.info("*****Execution Started for test_id_011*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.add_role()
        self.rp.role_txt(self.roletext)
        status_drp = self.driver.find_element(By.XPATH, "//select[@ng-model='c.isactive']")
        drp = Select(status_drp)
        drp.select_by_visible_text('Yes')
        self.rp.add_role_save_btn()
        time.sleep(7)
        new_role = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Auto Testing')]")
        if new_role.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_011 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_011.png")
            self.driver.close()
            self.logger.error("*****test_id_011 Failed*****")
            assert False

    def test_id_012(self, test_setup):
        self.logger.info("*****Execution Started for test_id_012*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.getrole_user()
        self.rp.getSearch(self.role)
        self.rp.uedit()
        time.sleep(7)
        ele = self.driver.find_element(By.XPATH, "//select[@ng-model='c.usersroleName']")
        drp = Select(ele)
        drp.select_by_visible_text('Auto Testing')
        self.rp.editus_save()
        time.sleep(15)
        search = self.driver.find_element(By.XPATH, "//input[@id='myInput']").clear()
        search_txt = self.driver.find_element(By.XPATH, "//input[@id='myInput']").send_keys('amit.tukaram')
        # self.rp.getSearch(self.role)
        rl = self.driver.find_element(By.XPATH, "(//td[contains(text(), 'Auto Testing')])[2]")
        if rl.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_012 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_012.png")
            self.driver.close()
            self.logger.error("*****test_id_012 Failed*****")
            assert False

    def test_id_013(self, test_setup):
        self.logger.info("*****Execution Started for test_id_013*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        text = self.driver.find_element(By.XPATH, "(//p[@class='text-center access-content'])[1]")
        reqbtn = self.driver.find_element(By.XPATH, "//button[@id='btn_request']")
        if text.is_displayed():
            assert True
            if reqbtn.is_enabled():
                assert True
                self.driver.close()
                self.logger.info("*****test_id_013 Passed*****")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_id_013.png")
                self.driver.close()
                self.logger.error("*****test_id_013 Failed*****")
                assert False

    def test_id_014(self, test_setup):
        self.logger.info("*****Execution Started for test_id_014*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[1]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'ReadOnly')])[1]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//*[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "All Allocation Data is changed to ReadOnly"
        if actl_msg == exp_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_014 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_014.png")
            self.driver.close()
            self.logger.error("*****test_id_014 Failed*****")
            assert False

    def test_id_015(self, test_setup):
        self.logger.info("*****Execution Started for test_id_015*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        alloca = self.driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[3]")
        if alloca.is_enabled():
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_015.png")
            self.driver.close()
            self.logger.error("*****test_id_015 Failed*****")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_015 Passed*****")

    def test_id_016(self, test_setup):
        self.logger.info("*****Execution Started for test_id_016*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        # self.rp.get_alloca()
        fil_alloc = self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]")
        if fil_alloc.is_enabled():
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_016.png")
            self.logger.info("*****test_id_016 Failed*****")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_016 Passed*****")
        self.driver.implicitly_wait(10)
        down_alloc = self.driver.find_element(By.XPATH, "(//button[@type='button'])[2]")
        if down_alloc.is_enabled():
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_016.png")
            self.driver.close()
            self.logger.error("*****test_id_016 Failed*****")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_016 Passed*****")

    # This will case will give a access to the user as Writable
    def test_id_0017(self, test_setup):
        self.logger.info("*****Execution Started for test_id_017*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[1]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'Writable')])[1]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//*[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "All Allocation Data is changed to Writable"
        if actl_msg == exp_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_017 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_017.png")
            self.driver.close()
            self.logger.error("*****test_id_017 Failed*****")
            assert False

    #This case will verify the writable access is working or not
    def test_id_0018(self, test_setup):
        self.logger.info("*****Execution Started for test_id_018*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        down_alloc = self.driver.find_element(By.XPATH, "(//button[@type='button'])[2]")
        if down_alloc.is_enabled():
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_018.png")
            self.driver.close()
            self.logger.error("*****test_id_018 Failed*****")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_018 Passed*****")

    #This case will verify the user can able to give the readonly access for Allocation Breakdown
    def test_id_019(self, test_setup):
        self.logger.info("*****Execution Started for test_id_019*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[1]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'No Access')])[1]").click()
        time.sleep(10)
        down_val1 = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[2]").click()
        option_1 = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'ReadOnly')])[2]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//*[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "Allocation Breakdown is changed to ReadOnly"
        if exp_msg == actl_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_019 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_019.png")
            self.driver.close()
            self.logger.error("*****test_id_019 Failed*****")
            assert False


    # This will check provided access is working fine or not
    def test_id_020(self, test_setup):
        self.logger.info("*****Execution Started for test_id_020*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        text = self.driver.find_element(By.XPATH, "(//p[@class='text-center access-content'])[1]")
        reqbtn = self.driver.find_element(By.XPATH, "//button[@id='btn_request']")
        if text.is_displayed():
            assert True
            if reqbtn.is_enabled():
                assert True
                self.driver.close()
                self.logger.info("*****test_id_020 Passed*****")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_id_020.png")
                self.driver.close()
                self.logger.error("*****test_id_020 Failed*****")
                assert False

     #This case will provode the Writable access to the user
    def test_id_021(self, test_setup):
        self.logger.info("*****Execution Started for test_id_021*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[2]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'Writable')])[2]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//div[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "Allocation Breakdown is changed to Writable"
        if exp_msg == actl_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_021 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_021.png")
            self.driver.close()
            self.logger.error("*****test_id_019 Failed*****")
            assert False

    # This case will verify provided writable access is working or not
    def test_id_022(self, test_setup):
        self.logger.info("*****Execution Started for test_id_022*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        text = self.driver.find_element(By.XPATH, "(//p[@class='text-center access-content'])[1]")
        reqbtn = self.driver.find_element(By.XPATH, "//button[@id='btn_request']")
        if text.is_displayed():
            assert True
            if reqbtn.is_enabled():
                assert True
                self.driver.close()
                self.logger.info("*****test_id_022 Passed*****")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_id_022.png")
                self.driver.close()
                self.logger.error("*****test_id_022 Failed*****")
                assert False

     # This case will change the access to the user from Allocation break down to close Quarter
    def test_id_023(self, test_setup):
        self.logger.info("*****Execution Started for test_id_023*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        down_val1 = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[2]").click()
        option1 = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'No Access')])[2]").click()
        time.sleep(10)
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[3]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'ReadOnly')])[3]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//*[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "Close Quarter is changed to ReadOnly"
        if exp_msg == actl_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_023 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_023.png")
            self.driver.close()
            self.logger.error("*****test_id_023 Failed*****")
            assert False

    #This case will provide the readonly access for Close Quarter and No Access for Allocation Breakdown
    def test_id_024(self, test_setup):
        self.logger.info("*****Execution Started for test_id_024*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        time.sleep(7)
        cls_qtr = self.driver.find_element(By.XPATH, "//button[@id='closequarter']")
        downnload_btn = self.driver.find_element(By.XPATH, "//button[@ng-click='ExportReporttoExcel()']")
        if cls_qtr.is_enabled() and downnload_btn.is_enabled():
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_023.png")
            self.driver.close()
            self.logger.error("*****test_id_024 Failed*****")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_024 Passed*****")

     # This case will verify to provide the writable access
    def test_id_025(self, test_setup):
        self.logger.info("*****Execution Started for test_id_025*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        self.driver.implicitly_wait(15)
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[3]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'Writable')])[3]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//div[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "Close Quarter is changed to Writable"
        if actl_msg == exp_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_025 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_025.png")
            self.driver.close()
            self.logger.error("*****test_id_025 Failed*****")
            assert False

    # This case will verify the Writable access for Close Quarter
    def test_id_026(self, test_setup):
        self.logger.info("*****Execution Started for test_id_026*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        page_name = self.driver.find_element(By.XPATH, "//h2[@class='heading mb-1']").text
        cls_qtr_btn = self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]")
        download = self.driver.find_element(By.XPATH, "(//button[@type='button'])[2]")
        if page_name == 'Close Quarter':
            assert True
            self.logger.info("*****test_id_026 Passed*****")
            if cls_qtr_btn.is_enabled():
                assert True
                self.logger.info("*****test_id_026 Passed*****")
            if download.is_enabled():
                assert True
                self.driver.close()
                self.logger.info("*****test_id_026 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_026.png")
            self.driver.close()
            self.logger.error("*****test_id_026 Failed*****")
            assert False

    #This case will verify the No Access for Close Quarter and ReadOnly for CustomSKU
    def test_id_027(self, test_setup):
        self.logger.info("*****Execution Started for test_id_027*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        down_val1 = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[3]").click()
        option1 = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'No Access')])[3]").click()
        time.sleep(10)
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[4]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'ReadOnly')])[4]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//*[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "Custom SKU is changed to ReadOnly"
        if exp_msg == actl_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_027 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_027.png")
            self.driver.close()
            self.logger.error("*****test_id_027 Failed*****")
            assert False

    # This case will check the Readonly access for the user
    def test_id_028(self, test_setup):
        self.logger.info("*****Execution Started for test_id_028*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        mega_custom_nav = self.driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[7]")
        Action_required = self.driver.find_element(By.XPATH, "//*[@id='nav-PendingAllocations-tab']")
        completed_tab = self.driver.find_element(By.XPATH, "//*[@id='nav-Allocations-tab']")
        colm_sel = self.driver.find_element(By.XPATH, "//*[@id='filtercler']")
        colm_pref = self.driver.find_element(By.XPATH, "//*[@id='btnPreference']")
        temp_down = self.driver.find_element(By.XPATH, "//*[@id='TemplateDownload']")
        download = self.driver.find_element(By.XPATH, "//*[@id='download']")
        upload = self.driver.find_element(By.XPATH, "(//*[@id='DataUpload'])[1]")
        if mega_custom_nav.is_enabled() and Action_required.is_enabled() and completed_tab.is_enabled():
            assert True
            self.logger.info("*****test_id_028 Passed*****")
            if colm_pref.is_enabled() and colm_sel.is_enabled() and temp_down.is_enabled() and download.is_enabled() and upload.is_enabled():
                self.driver.save_screenshot(".\\Screenshots\\" + "test_id_028.png")
                self.driver.close()
                self.logger.error("*****test_id_028 Failed*****")
                assert False
            else:
                assert True
                self.logger.info("*****test_id_028 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_028.png")
            self.driver.close()
            self.logger.error("*****test_id_028 Failed*****")
            assert False

    # This case will verify the readonly access for a Completed tab
    def test_id_029(self, test_setup):
        self.logger.info("*****Execution Started for test_id_029*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        time.sleep(8)
        mega_custom_nav = self.driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[7]")
        Action_required = self.driver.find_element(By.XPATH, "//*[@id='nav-PendingAllocations-tab']")
        completed_tab = self.driver.find_element(By.XPATH, "//*[@id='nav-Allocations-tab']")
        colm_sel = self.driver.find_element(By.XPATH, "//*[@id='filtercler']")
        colm_pref = self.driver.find_element(By.XPATH, "//*[@id='btnPreference']")
        temp_down = self.driver.find_element(By.XPATH, "//*[@id='TemplateDownload']")
        download = self.driver.find_element(By.XPATH, "//*[@id='download']")
        upload = self.driver.find_element(By.XPATH, "(//*[@id='DataUpload'])[1]")
        completed_tab.click()
        if mega_custom_nav.is_enabled() and Action_required.is_enabled() and completed_tab.is_enabled():
            assert True
            self.logger.info("*****test_id_028 Passed*****")
            if colm_pref.is_enabled() and colm_sel.is_enabled() and temp_down.is_enabled() and download.is_enabled() and upload.is_enabled():
                self.driver.save_screenshot(".\\Screenshots\\" + "test_id_029.png")
                self.driver.close()
                self.logger.error("*****test_id_029 Failed*****")
                assert False
            else:
                assert True
                self.logger.info("*****test_id_029 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_029.png")
            self.driver.close()
            self.logger.error("*****test_id_029 Failed*****")
            assert False

    # This case will provides the Writable access to the user
    def test_id_030(self, test_setup):
        self.logger.info("*****Execution Started for test_id_030*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        self.driver.implicitly_wait(15)
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[4]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'Writable')])[4]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//div[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "Custom SKU is changed to Writable"
        if actl_msg == exp_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_030 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_030.png")
            self.driver.close()
            self.logger.error("*****test_id_030 Failed*****")
            assert False

    # This case will verify the Writable access
    def test_id_031(self, test_setup):
        self.logger.info("*****Execution Started for test_id_031*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        mega_custom_nav = self.driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[7]")
        Action_required = self.driver.find_element(By.XPATH, "//*[@id='nav-PendingAllocations-tab']")
        completed_tab = self.driver.find_element(By.XPATH, "//*[@id='nav-Allocations-tab']")
        colm_sel = self.driver.find_element(By.XPATH, "//*[@id='filtercler']")
        colm_pref = self.driver.find_element(By.XPATH, "//*[@id='btnPreference']")
        temp_down = self.driver.find_element(By.XPATH, "//*[@id='TemplateDownload']")
        download = self.driver.find_element(By.XPATH, "//*[@id='download']")
        upload = self.driver.find_element(By.XPATH, "(//*[@id='DataUpload'])[1]")
        if mega_custom_nav.is_enabled() and Action_required.is_enabled() and completed_tab.is_enabled():
            assert True
            self.logger.info("*****test_id_031 Passed*****")
            if colm_pref.is_enabled() and colm_sel.is_enabled() and temp_down.is_enabled() and download.is_enabled() and upload.is_enabled():
                assert True
                self.driver.close()
                self.logger.info("*****test_id_031 Passed*****")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_id_031.png")
                self.driver.close()
                self.logger.error("*****test_id_031 Failed*****")
                assert False
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_031.png")
            self.driver.close()
            self.logger.error("*****test_id_031 Failed*****")
            assert False

    #This case will verify the Custom SKU Writable access
    def test_id_032(self, test_setup):
        self.logger.info("*****Execution Started for test_id_032*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        time.sleep(8)
        mega_custom_nav = self.driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[7]")
        Action_required = self.driver.find_element(By.XPATH, "//*[@id='nav-PendingAllocations-tab']")
        completed_tab = self.driver.find_element(By.XPATH, "//*[@id='nav-Allocations-tab']")
        colm_sel = self.driver.find_element(By.XPATH, "//*[@id='filtercler']")
        colm_pref = self.driver.find_element(By.XPATH, "//*[@id='btnPreference']")
        temp_down = self.driver.find_element(By.XPATH, "//*[@id='TemplateDownload']")
        download = self.driver.find_element(By.XPATH, "//*[@id='download']")
        upload = self.driver.find_element(By.XPATH, "(//*[@id='DataUpload'])[1]")
        completed_tab.click()
        if colm_pref.is_enabled() and colm_sel.is_enabled() and temp_down.is_enabled() and download.is_enabled() and upload.is_enabled():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_032 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_029.png")
            self.driver.close()
            self.logger.error("*****test_id_032 Failed*****")
            assert False

    #This case will provide the readonly access for dashboard and No Access for Custom SKU
    def test_id_033(self, test_setup):
        self.logger.info("*****Execution Started for test_id_033*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        down_val1 = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[4]").click()
        option1 = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'No Access')])[4]").click()
        time.sleep(16)
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[5]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'ReadOnly')])[5]").click()
        wait = WebDriverWait(self.driver, 15)
        toast = (By.XPATH, "//*[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "Dashboard is changed to ReadOnly"
        if exp_msg == actl_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_033 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_034.png")
            self.driver.close()
            self.logger.error("*****test_id_033 Failed*****")
            assert False

    # This case will verify the readonly access on Dashboard page
    def test_id_034(self, test_setup):
        self.logger.info("*****Execution Started for test_id_034*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        time.sleep(8)
        dashboard = self.driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[2]")
        current_list = self.driver.find_element(By.XPATH, "//*[@id='nav-current-tab']")
        pipeline_list = self.driver.find_element(By.XPATH, "//*[@id='nav-pipeline-tab']")
        History_list = self.driver.find_element(By.XPATH, "//*[@id='nav-history-tab']")
        crnt_down = self.driver.find_element(By.XPATH, "//*[@id='nav-current']/div[2]/div[1]/div[1]/button[2]")
        curr_view = self.driver.find_element(By.XPATH, "(//*[@id='view'])[1]")
        scroll = self.driver.execute_script("arguments[0].scrollIntoView();", current_list)
        time.sleep(4)
        if dashboard.is_displayed() and current_list.is_enabled() and pipeline_list.is_enabled():
            assert True
            self.logger.info("*****test_id_034 Passed*****")
            if crnt_down.is_enabled() and curr_view.is_enabled():
                self.driver.save_screenshot(".\\Screenshots\\" + "test_id_035.png")
                self.logger.error("*****test_id_034 Failed*****")
                assert False
            else:
                assert True
                self.logger.info("*****test_id_034 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_034.png")
            self.driver.close()
            self.logger.error("*****test_id_034 Failed*****")
            assert False
        pipeline_list.click()
        time.sleep(5)
        pip_down = self.driver.find_element(By.XPATH, "//*[@id='nav-pipeline']/div[2]/div[1]/div[1]/button[2]")
        pip_view = self.driver.find_element(By.XPATH, "(//*[@id='view'])[151]")
        if pip_view.is_enabled() and pip_down.is_enabled():
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_034.png")
            self.logger.error("*****test_id_034 Failed*****")
            assert False
        else:
            assert True
            self.logger.info("*****test_id_034 Passed*****")
        History_list.click()
        time.sleep(5)
        his_down = self.driver.find_element(By.XPATH, "//*[@id='nav-history']/div[2]/div[1]/div[1]/button[2]")
        if his_down.is_enabled():
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_034.png")
            self.driver.close()
            self.logger.error("*****test_id_034 Failed*****")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_034 Passed*****")

    #This case will provides the writable access for Dashboard
    def test_id_035(self, test_setup):
        self.logger.info("*****Execution Started for test_id_035*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.rp.click_settings()
        self.rp.User_mang()
        self.rp.role_config()
        self.driver.implicitly_wait(15)
        down_val = self.driver.find_element(By.XPATH, "(//select[@class='ctrl-status'])[5]").click()
        option = self.driver.find_element(By.XPATH, "(//option[contains(text(), 'Writable')])[5]").click()
        wait = WebDriverWait(self.driver, 10)
        toast = (By.XPATH, "//div[@id='snackbarrr']")
        toast_element = wait.until(EC.visibility_of_element_located(toast))
        actl_msg = toast_element.text
        exp_msg = "Dashboard SKU is changed to Writable"
        if actl_msg == exp_msg:
            assert True
            self.driver.close()
            self.logger.info("*****test_id_035 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_035.png")
            self.driver.close()
            self.logger.error("*****test_id_035 Failed*****")
            assert False

    #This case will verify the Writable access on Dashboard page
    def test_id_036(self, test_setup):
        self.logger.info("*****Execution Started for test_id_036*****")
        self.driver = test_setup
        self.driver.implicitly_wait(50)
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.lp.SetUsername(self.amusername)
        self.lp.Setpassword(self.ampassword)
        self.lp.clicklogin()
        time.sleep(8)
        dashboard = self.driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[2]")
        current_list = self.driver.find_element(By.XPATH, "//*[@id='nav-current-tab']")
        pipeline_list = self.driver.find_element(By.XPATH, "//*[@id='nav-pipeline-tab']")
        History_list = self.driver.find_element(By.XPATH, "//*[@id='nav-history-tab']")
        crnt_down = self.driver.find_element(By.XPATH, "//*[@id='nav-current']/div[2]/div[1]/div[1]/button[2]")
        curr_view = self.driver.find_element(By.XPATH, "(//*[@id='view'])[1]")
        scroll = self.driver.execute_script("arguments[0].scrollIntoView();", current_list)
        if dashboard.is_displayed() and current_list.is_enabled() and pipeline_list.is_enabled():
            assert True
            self.logger.info("*****Dash, curr, pip, test_id_036 Passed*****")
            if crnt_down.is_enabled() and curr_view.is_enabled():
                assert True
                self.logger.info("*****Dash, curr, pip, test_id_036 Passed*****")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_id_036.png")
                self.logger.error("*****Dash, curr, pip, test_id_036 Failed*****")
                assert False
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_036.png")
            self.logger.error("*****Dash, curr, pip,test_id_036 Failed*****")
            assert False
        time.sleep(5)
        pipeline_list.click()
        pip_down = self.driver.find_element(By.XPATH, "//*[@id='nav-pipeline']/div[2]/div[1]/div[1]/button[2]")
        pip_view = self.driver.find_element(By.XPATH, "(//*[@id='view'])[151]")
        if pip_view.is_enabled() and pip_down.is_enabled():
            assert True
            self.logger.info("*****Pipe line, test_id_036 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_036.png")
            self.logger.error("*****Pipe line, test_id_036 Failed*****")
            assert False
        History_list.click()
        time.sleep(5)
        his_down = self.driver.find_element(By.XPATH, "//*[@id='nav-history']/div[2]/div[1]/div[1]/button[2]")
        if his_down.is_enabled():
            assert True
            self.driver.close()
            self.logger.info("*****History test_id_036 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_036.png")
            self.driver.close()
            self.logger.error("*****History test_id_036 Failed*****")
            assert False


























