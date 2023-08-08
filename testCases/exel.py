from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get("https://allocationenginedev.service-now.com/ae")
username = driver.find_element(By.XPATH, "//input[@id='username']")
username.send_keys("sai.subramaniam")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("Iopex@2023")
login = driver.find_element(By.XPATH, "//button[@type='submit']")
login.click()
driver.implicitly_wait(20)
mega = driver.find_element(By.XPATH, "(//li[@data-toggle='tooltip'])[7]")
mega.click()
upload = driver.find_element(By.XPATH, "(//button[@id='DataUpload'])[1]").click()
upload_file = driver.find_element(By.XPATH, "//input[@id='triggerFile']")
# ACV = driver.find_element(By.XPATH, "//*[@id='mega_action_required']/tbody/tr[1]/td[7]").text
# result = ACV
# result_wo_sym = result.replace("$", "").replace(",", "")
# result_value = float(result_wo_sym)/2
# file = "C://Users//sai.subramaniam//PycharmProjects//AllocationEngine//testCases//mg2.xlsx"
# upload = driver.find_element(By.XPATH, "(//button[@id='DataUpload'])[1]").click()
# upload_file = driver.find_element(By.XPATH, "//input[@id='triggerFile']").send_keys(file)
# wb = openpyxl.Workbook()
# sheet = wb.active
# data_to_write = [["Product Code", "Product Name", "Business Unit", "Meter", "Quantity", "List Price", "Discount", "Sales Price", "ACV"],
#                  ["PROD17257", "IT Service Management Professional - Unrestricted User v3", "ITSM", "Unrestricted User", 62330, "$20", "71.75%", "$5.65", result_value],
#                  ["PROD14995", "ITOM Operator Professional - Subscription Unit v2", "ITOM", "Subscription Unit", 55000, "$24", "91.375%", "$2.07", result_value]]
# for row_index, row_data in enumerate(data_to_write, start=1):
#     for col_index, cell_data in enumerate(row_data, start=1):
#         sheet.cell(row=row_index, column=col_index, value=cell_data)
#         wb.save("mg3.xlsx")
# file = "./testCases/mg3.xlsx"
# upload = driver.find_element(By.XPATH, "(//button[@id='DataUpload'])[1]").click()
# upload_file = driver.find_element(By.XPATH, "//input[@id='triggerFile']").send_keys(file)
