from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Test Name", Keys.ENTER)
time.sleep(2)
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Test Last Name", Keys.ENTER)
time.sleep(2)
e_mail = driver.find_element(By.NAME, value="email")
e_mail.send_keys("testemail@mymail.com", Keys.ENTER)
time.sleep(5)

driver.quit()



