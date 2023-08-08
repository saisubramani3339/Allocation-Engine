import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture()
def test_setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser.....")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser.....")
    else:
        driver = webdriver.Edge()
        print("Launching Edge Browser.....")
    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")

#################### Pytest HTML Report ###################

# It is a hook for Adding Environment info to HTML Report
def pytest_html_report_title(report):
    report.title = "Automation Testing Test Report"

def pytest_configure(config):
    Project_Name = 'ServiceNow -- Allocation Engine'
    Module_Name = 'Login Page'
    Tester = 'Sai Subramaniam'
    config._metadata = {
        "Project_Name": Project_Name,
        "Module_Name": Module_Name,
        "Tester": Tester,
    }
# It is a hook for delete/modify Environment info to HTML Report




# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

