from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
#article_count = driver.find_element(By.XPATH, value="//*[@id=\"articlecount\"]/a[1]")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
#article_count.click()

#follow_link = driver.find_element(By.LINK_TEXT, value="Content portals")
#follow_link.click()

search_button = driver.find_element(By.CSS_SELECTOR, value="#p-search a")
search_button.click()
time.sleep(1)
search_box = driver.find_element(By.NAME, value="search")
search_box.send_keys("Pyhton", Keys.ENTER)
time.sleep(3)

driver.quit()
