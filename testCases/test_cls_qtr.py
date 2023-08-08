import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pageObjects.loginpage import loginpage
from pageObjects.rolespage import rolespage
from pageObjects.closeqtr import classqtrpage
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGen
from pytest_html_reporter import attach

download_folder = "C:\\Users\\sai.subramaniam\\Downloads"
chromeOptions = Options()
chromeOptions.add_experimental_option("pref", {
    'download.default_directory': download_folder,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': False,
    })

class Test_01_rol():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    hissearch = ReadConfig.hissearch()

    logger = LogGen.loggen()

    # This case will click the Close Quarter side nav button
    def test_id_001(self, test_setup):
        self.logger.info("*****Test_01_Close Quarter*****")
        self.logger.info("*****Execution Started for test_id_001*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.nav_close()
        page_name = self.driver.find_element(By.XPATH, "//h2[@class='heading mb-1']")
        if page_name.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_001 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_001.png")
            self.driver.close()
            self.logger.error("*****test_id_001 Failed*****")
            assert False

    # This case will check wheather Close Quarter button is enabled or not
    def test_id_002(self, test_setup):
        self.logger.info("*****Execution Started for test_id_002*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.nav_close()
        cls_qtr_btn = self.driver.find_element(By.XPATH, "//button[@id='closequarter']")
        if cls_qtr_btn.is_enabled():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_002 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_002.png")
            self.driver.close()
            self.logger.error("*****test_id_002 Failed*****")
            assert False

    # This case will check wheather Download button is enabled or not
    def test_id_003(self, test_setup):
        self.logger.info("*****Execution Started for test_id_003*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.nav_close()
        download = self.driver.find_element(By.XPATH, "//button[@ng-click='ExportReporttoExcel()']")
        if download.is_enabled():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_003 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_003.png")
            self.driver.close()
            self.logger.error("*****test_id_003 Failed*****")
            assert False

    # This case will download the file
    def test_id_004(self, test_setup):
        self.logger.info("*****Execution Started for test_id_004*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.nav_close()
        self.cq.download_btn()
        time.sleep(10)
        file_name = 'AE Dashboard - Allocation Engine.csv'
        downloaded_file_path = os.path.join(download_folder, file_name)
        file_exists = os.path.exists(downloaded_file_path)
        if file_exists:
            print("file has been downloaded successfully!")
            assert True
            self.driver.close()
            self.logger.info("*****test_id_004 Passed*****")
        else:
            print("File downloaded failed!")
            self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_004.png")
            self.driver.close()
            self.logger.error("*****test_id_004 Failed*****")
            assert False

    # This case will the show entries of the page and it's count
    def test_id_005(self, test_setup):
        self.logger.info("*****Execution Started for test_id_005*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.nav_close()
        scroll = self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        ele = self.driver.find_element(By.XPATH, "//select[@name='closeqater_length']")
        drp = Select(ele)
        drp.select_by_value('10')
        rows = len(self.driver.find_elements(By.XPATH, "//*[@id='closeqater']/tbody/tr"))
        if rows == 10:
            assert True
            ele = self.driver.find_element(By.XPATH, "//select[@name='closeqater_length']")
            drp = Select(ele)
            drp.select_by_value('25')
            rows = len(self.driver.find_elements(By.XPATH, "//*[@id='closeqater']/tbody/tr"))
            if rows <= 25:
                assert True
                ele = self.driver.find_element(By.XPATH, "//select[@name='closeqater_length']")
                drp = Select(ele)
                drp.select_by_value('25')
                rows = len(self.driver.find_elements(By.XPATH, "//*[@id='closeqater']/tbody/tr"))
                if rows <= 50:
                    assert True
                    ele = self.driver.find_element(By.XPATH, "//select[@name='closeqater_length']")
                    drp = Select(ele)
                    drp.select_by_value('25')
                    rows = len(self.driver.find_elements(By.XPATH, "//*[@id='closeqater']/tbody/tr"))
                    if rows <= 100:
                        assert True
                        self.driver.close()
                        self.logger.info("*****test_id_005 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_005.png")
            self.driver.close()
            self.logger.error("*****test_id_005 Failed*****")
            assert False

    # This case will verify the 22-Q4 closed values on Historical Tab
    def test_id_006(self, test_setup):
        self.logger.info("*****Execution Started for test_id_006*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.master()
        self.cq.Historical()
        time.sleep(10)
        # self.cq.his_search(self.hissearch)
        search = self.driver.find_element(By.XPATH, "//input[@id='myInput']")
        search.send_keys('22-Q4')
        salsqtr = self.driver.find_element(By.XPATH, "//*[@id='Historydataget']/tbody/tr[1]/td[12]").text
        if salsqtr == '22-Q4':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_006 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_006.png")
            self.driver.close()
            self.logger.error("*****test_id_006 Failed*****")
            assert False

    # This will verify the status of Previous Quarters (Closed and Current)
    def test_id_007(self, test_setup):
        self.logger.info("*****Execution Started for test_id_007*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.nav_close()
        closed_22q4 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[1]/td[2]").text
        current_22q4 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[1]/td[3]").text
        closed_23q1 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[2]/td[2]").text
        current_23q1 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[2]/td[3]").text
        if closed_22q4 == 'Y' and current_22q4 == 'N':
            assert True
            self.logger.info("*****test_id_007 Passed*****")
            if closed_23q1 == 'Y' and current_23q1 == 'N':
                assert True
                self.driver.close()
                self.logger.info("*****test_id_007 Passed*****")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_007.png")
                self.driver.close()
                self.logger.error("*****test_id_007 Failed*****")
                assert False
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_007.png")
            self.driver.close()
            self.logger.error("*****test_id_007 Failed*****")
            assert False

     # This case will verify the Pagination Flow
    def test_id_008(self, test_setup):
        self.logger.info("*****Execution Started for test_id_008*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.nav_close()
        scroll = self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        ele = self.driver.find_element(By.XPATH, "//select[@name='closeqater_length']")
        drp = Select(ele)
        drp.select_by_value('10')
        rows = len(self.driver.find_elements(By.XPATH, "//*[@id='closeqater']/tbody/tr"))
        if rows == 10:
            assert True
            self.logger.info("*****test_id_008 Passed*****")
            next = self.driver.find_element(By.XPATH, "//a[@id='closeqater_next']")
            next.click()
            if rows <= 10:
                assert True
                self.logger.info("*****test_id_008 Passed*****")
                next = self.driver.find_element(By.XPATH, "//a[@id='closeqater_next']")
                next.click()
                if rows <= 10:
                    assert True
                    self.logger.info("*****test_id_008 Passed*****")
                    next = self.driver.find_element(By.XPATH, "//a[@id='closeqater_next']")
                    next.click()
                    if rows < 10:
                        assert True
                        self.logger.info("*****test_id_008 Passed*****")
                        prev = self.driver.find_element(By.XPATH, "//a[@id='//a[@id='closeqater_previous']']")
                        prev.click()
                    if rows <= 10:
                        assert True
                        self.driver.close()
                        self.logger.info("*****test_id_008 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_008.png")
            self.driver.close()
            self.logger.error("*****test_id_008 Failed*****")
            assert False

    # This case will verify the Functionality of Close Quarter NO
    def test_id_009(self, test_setup):
        self.logger.info("*****Execution Started for test_id_009*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.rp = rolespage(self.driver)
        self.cq = classqtrpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.cq.nav_close()
        self.cq.close_quarter()
        self.cq.No_btn()
        # no_btn = self.driver.find_element(By.XPATH, "(//button[@type='button'])[4]")
        # no_btn.click()
        closed_23q1 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[2]/td[2]").text
        current_23q1 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[2]/td[3]").text
        if closed_23q1 == 'Y' and current_23q1 == 'N':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_009 Passed*****")
        else:
            attach(data=self.driver.get_screenshot_as_png())
            self.driver.close()
            self.logger.error("*****test_id_009 Failed*****")
            assert False

    # # This case will verify the Functionality of Close Quarter Yes
    # def test_id_010(self, test_setup):
    #     self.logger.info("*****Execution Started for test_id_010*****")
    #     self.driver = test_setup
    #     self.driver.get(self.baseURL)
    #     self.lp = loginpage(self.driver)
    #     self.rp = rolespage(self.driver)
    #     self.cq = classqtrpage(self.driver)
    #     self.lp.SetUsername(self.username)
    #     self.lp.Setpassword(self.password)
    #     self.lp.clicklogin()
    #     self.cq.nav_close()
    #     self.cq.close_quarter()
    #     self.cq.yes_btn()
    #     ref = self.driver.refresh()
    #     closed_23q2 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[3]/td[2]").text
    #     current_23q2 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[3]/td[3]").text
    #     closed_23q3 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[4]/td[2]").text
    #     current_23q3 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[4]/td[3]").text
    #     closed_23q4 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[5]/td[2]").text
    #     current_23q4 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[5]/td[3]").text
    #     closed_24q1 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[6]/td[2]").text
    #     current_24q1 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[6]/td[3]").text
    #     closed_24q2 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[7]/td[2]").text
    #     current_24q2 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[7]/td[3]").text
    #     closed_24q3 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[8]/td[2]").text
    #     current_24q3 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[8]/td[3]").text
    #     closed_24q4 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[9]/td[2]").text
    #     current_24q4 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[9]/td[3]").text
    #     closed_25q1 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[10]/td[2]").text
    #     current_25q1 = self.driver.find_element(By.XPATH, "//*[@id='closeqater']/tbody/tr[10]/td[3]").text
    #     if closed_23q2 == 'Y' and current_23q2 == 'N':
    #         assert True
    #         self.cq.master()
    #         self.cq.Historical()
    #         time.sleep(10)
    #         # self.cq.his_search(self.hissearch)
    #         search = self.driver.find_element(By.XPATH, "//input[@id='myInput']")
    #         search.send_keys('23-Q2')
    #         salsqtr = self.driver.find_element(By.XPATH, "//*[@id='Historydataget']/tbody/tr[1]/td[12]").text
    #         if salsqtr == '23-Q2':
    #             assert True
    #             self.driver.close()
    #             self.logger.info("*****test_id_010 Passed*****")
    #         else:
    #             self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_010.png")
    #             self.driver.close()
    #             self.logger.error("*****test_id_010 Failed*****")
    #             assert False
    #     elif closed_23q3 == 'Y' and current_23q3 == 'N':
    #         assert True
    #         self.driver.close()
    #         self.logger.info("*****test_id_010 Passed*****")
    #     elif closed_23q4 == 'Y' and current_23q4 == 'N':
    #         assert True
    #         self.driver.close()
    #         self.logger.info("*****test_id_010 Passed*****")
    #     elif closed_24q1 == 'Y' and current_24q1 == 'N':
    #         assert True
    #         self.driver.close()
    #         self.logger.info("*****test_id_010 Passed*****")
    #     elif closed_24q2 == 'Y' and current_24q2 == 'N':
    #         assert True
    #         self.driver.close()
    #         self.logger.info("*****test_id_010 Passed*****")
    #     elif closed_24q3 == 'Y' and current_24q3 == 'N':
    #         assert True
    #         self.driver.close()
    #         self.logger.info("*****test_id_010 Passed*****")
    #     elif closed_24q4 == 'Y' and current_24q4 == 'N':
    #         assert True
    #         self.driver.close()
    #         self.logger.info("*****test_id_010 Passed*****")
    #     elif closed_25q1 == 'Y' and current_25q1 == 'N':
    #         assert True
    #         self.driver.close()
    #         self.logger.info("*****test_id_010 Passed*****")
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\" + "clo_test_id_010.png")
    #         self.driver.close()
    #         self.logger.error("*****test_id_010 Failed*****")
    #         assert False






