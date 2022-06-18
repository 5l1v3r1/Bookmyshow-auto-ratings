from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/login/?referer=/bengaluru/movies/beast/ET00311733")

input=driver.find_element_by_xpath('//*[@id="wzrk-confirm"]').click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

input=driver.find_element_by_xpath('//*[@id="emailId"]').send_keys("vk123@gmail.com") #replace with your email

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

driver.maximize_window()
time.sleep(15)

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(8)

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()
