import logging

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pageObjects.loginpage import loginpage
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGen

class Test_01_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    invalid_username = ReadConfig.getinvalid_username()
    invalid_password = ReadConfig.getinvalid_password()
    pasword_space = ReadConfig.getUsername_space()
    username_space = ReadConfig.getUsername_space()
    First_name = ReadConfig.getFirst_name()
    last_name = ReadConfig.getlast_name()
    name_s = ReadConfig.getname_s()
    name = ReadConfig.getname()
    special_cars = ReadConfig.getspecial_chars()
    random_num = ReadConfig.getrandom_num()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_id_001(self, test_setup):
        self.logger.info("*****Test_01_Login*****")
        self.logger.info("*****Execution Started for test_id_001*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'AE Login - Allocation Engine':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_001 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_id_001.png")
            self.driver.close()
            self.logger.error("*****test_id_001 Failed*****")
            assert False,f'Title is getting Mismatch'

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_id_002(self, test_setup):
        self.logger.info("*****Execution Started for test_id_002*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(5)
        name = self.driver.find_element(By.XPATH, "(//h2[@class='heading mb-4'])[1]").text
        if name == 'Dashboard':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_002 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_002.png")
            self.driver.close()
            self.logger.error("*****test_id_002 Failed*****")
            assert False, f'Either User not loggedin Sucessfully or landing page should page be wrong'

    @pytest.mark.regression
    def test_id_003(self, test_setup):
        self.logger.info("*****Execution Started for test_id_003*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.invalid_username)
        self.lp.Setpassword(self.invalid_password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_003 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_003.png")
            self.driver.close()
            self.logger.error("*****test_id_003 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_004(self, test_setup):
        self.logger.info("*****Execution Started for test_id_004*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_004 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_004.png")
            self.driver.close()
            self.logger.error("*****test_id_004 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_005(self, test_setup):
        self.logger.info("*****Execution Started for test_id_005*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.Setpassword(self.username)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_005 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_005.png")
            self.driver.close()
            self.logger.error("*****test_id_005 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_006(self, test_setup):
        self.logger.info("*****Execution Started for test_id_006*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_006 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_006.png")
            self.driver.close()
            self.logger.error("*****test_id_006 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_007(self, test_setup):
        self.logger.info("*****Execution Started for test_id_007*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username_space)
        self.lp.Setpassword(self.pasword_space)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_007 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_007.png")
            self.driver.close()
            self.logger.error("*****test_id_007 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_008(self, test_setup):
        self.logger.info("*****Execution Started for test_id_008*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username_space)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_008 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_008.png")
            self.driver.close()
            self.logger.error("*****test_id_008 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_009(self, test_setup):
        self.logger.info("*****Execution Started for test_id_009*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.pasword_space)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_009 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_009.png")
            self.driver.close()
            self.logger.error("*****test_id_009 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_010(self, test_setup):
        self.logger.info("*****Execution Started for test_id_010*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.First_name)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_010 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_010.png")
            self.driver.close()
            self.logger.error("*****test_id_010 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_011(self, test_setup):
        self.logger.info("*****Execution Started for test_id_011*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.last_name)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_011 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_011.png")
            self.driver.close()
            self.logger.error("*****test_id_011 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_012(self, test_setup):
        self.logger.info("*****Execution Started for test_id_012*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.name)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_012 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_012.png")
            self.driver.close()
            self.logger.error("*****test_id_012 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_013(self, test_setup):
        self.logger.info("*****Execution Started for test_id_013*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.name_s)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_013 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_013.png")
            self.driver.close()
            self.logger.error("*****test_id_013 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_014(self, test_setup):
        self.logger.info("*****Execution Started for test_id_014*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.random_num)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_014 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_014.png")
            self.driver.close()
            self.logger.error("*****test_id_014 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_015(self, test_setup):
        self.logger.info("*****Execution Started for test_id_015*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.random_num)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_015 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_015.png")
            self.driver.close()
            self.logger.error("*****test_id_015 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    def test_id_016(self, test_setup):
        self.logger.info("*****Execution Started for test_id_016*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.random_num)
        self.lp.Setpassword(self.random_num)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_016 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_016.png")
            self.driver.close()
            self.logger.error("*****test_id_016 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_017(self, test_setup):
        self.logger.info("*****Execution Started for test_id_017*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.special_cars)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_017 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_017.png")
            self.driver.close()
            self.logger.error("*****test_id_017 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_018(self, test_setup):
        self.logger.info("*****Execution Started for test_id_018*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.special_cars)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_018 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_018.png")
            self.driver.close()
            self.logger.error("*****test_id_018 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'

    @pytest.mark.regression
    def test_id_019(self, test_setup):
        self.logger.info("*****Execution Started for test_id_019*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.special_cars)
        self.lp.Setpassword(self.special_cars)
        self.lp.clicklogin()
        Error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'User name or password invalid')]")
        if Error_message.is_displayed():
            assert True
            self.driver.close()
            self.logger.info("*****test_id_019 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_019.png")
            self.driver.close()
            self.logger.error("*****test_id_019 Failed*****")
            assert False, f'Either User loggedin on Invalid credentials or Error message is not displayed to the user on Invalid credentials'
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.skip
    def test_id_020(self, test_setup):
        self.logger.info("*****Execution Started for test_id_020*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(4)
        self.lp.Clickprofile()
        self.lp.Clicklogout()
        if self.driver.title == 'AE Login - Allocation Engine':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_020 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_020.png")
            self.driver.close()
            self.logger.error("*****test_id_020 Failed*****")
            assert False, f'User should not  logged out Properly'

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_id_021(self, test_setup):
        self.logger.info("*****Execution Started for test_id_021*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.lp.Clickprofile()
        self.lp.Clicklogout()
        time.sleep(4)
        refresh = self.driver.refresh()
        if self.driver.title == 'AE Login - Allocation Engine':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_021 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_021.png")
            self.driver.close()
            self.logger.error("*****test_id_021 Failed*****")
            assert False, f'User should not logged out Properly or On Refresh activity might session is logged in'

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_id_022(self, test_setup):
        self.logger.info("*****Execution Started for test_id_022*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.Setpassword(self.password)
        self.lp.clicklogin()
        self.lp.Clickprofile()
        self.lp.Clicklogout()
        back = self.driver.back()
        forward = self.driver.forward()
        if self.driver.title == 'AE Login - Allocation Engine':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_022 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_022.png")
            self.driver.close()
            self.logger.error("*****test_id_022 Failed*****")
            assert False, f'User should not logged out Properly or On Browser back and forward activity might session is logged in'

    @pytest.mark.regression
    def test_id_023(self, test_setup):
        self.logger.info("*****Execution Started for test_id_023*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        User_name = self.driver.find_element(By.XPATH, "//input[@id='username']")
        Password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        Login_Button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        if User_name.is_enabled():
            assert True
            if Password.is_enabled():
                assert True
                if Login_Button:
                    assert True
                    self.driver.close()
                    self.logger.info("*****test_id_023 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_0023")
            self.driver.close()
            self.logger.error("*****test_id_023 Failed*****")
            assert False, f'Buttons are not in Enabled '

    def test_id_024(self, test_setup):
        self.logger.info("*****Execution Started for test_id_024*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        Password_link = self.driver.find_element(By.LINK_TEXT, "Forgot Password ?")
        Password_link.click()
        page_name = self.driver.title
        if page_name == 'Password Reset - Identify':
            assert True
            self.driver.close()
            self.logger.info("*****test_id_024 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_024")
            self.driver.close()
            self.logger.error("*****test_id_024 Failed*****")
            assert False, f'Page not redirected to the Password Reset'

    def test_id_025(self, test_setup):
        self.logger.info("*****Execution Started for test_id_025*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        Remember_me = self.driver.find_element(By.XPATH, "//input[@type='checkbox']")
        if Remember_me.is_enabled():
            assert True
            if Remember_me.is_enabled():
                assert True
                self.driver.close()
                self.logger.info("*****test_id_025 Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_id_025")
            self.driver.close()
            self.logger.error("*****test_id_025 Failed*****")
            assert False, f'Remember me checkbox are not enable'

    @pytest.mark.skip
    def test_id_026(self, test_setup):
        self.logger.info("*****Execution Started for test_id_026*****")
        self.driver = test_setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        Password_link = self.driver.find_element(By.LINK_TEXT, "Forgot Password ?")
        Password_link.click()
        username = self.driver.find_element(By.XPATH, "//input[@id='sysparm_user_id_0']")
        username.send_keys('sai.subramaniam')
        captcha = self.driver.find_element(By.XPATH, "//img[@id='captcha_image']")
        captcha_image_url = captcha.get_attribute('pwd_jcaptcha.do')
        captcha_text = captcha.text
        captcha_field = self.driver.find_element(By.XPATH, "//input[@id='sysparm_captcha']")
        captcha_field.send_keys(captcha_text)
        next = self.driver.find_element(By.XPATH, "//button[@id='sysverb_pwd_reset']")
        next.click()









