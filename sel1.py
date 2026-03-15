from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/chadanie/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demoqa.com/")
sleep(5)
driver.maximize_window()
#username= driver.find_element(By.CSS_SELECTOR, "username").send_keys("admin1")
#driver.execute_script("arguments[0].username();", username)

#driver.find_element(By.CSS_SELECTOR, "hbr-input[name='password']").send_keys("P@ssword9")
#driver.find_element(By.CLASS_NAME, "ciscoHarborAuth--auth-src-ui-login-vm-LocalLoginMagnetic_module_css--magneticMainContainer").click()
actual_title=driver.title
print(actual_title)
sleep(5)
if actual_title == "demosite":
    print("Test Passed")
else:
    print("Test Failed")
driver.close()

