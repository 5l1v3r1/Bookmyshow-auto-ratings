#presenting the first bms auto rating using python github

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/777-charlie/ET00077150")  #change which movie you want to auto ratings

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_css_selector('#super-container > div.sc-1hbje21-1.kziggM > div > div > div > div.sc-iujRgT.cSkjY > div > div.sc-exAgwC.eJpBoy > div > div:nth-child(2) > div > div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("yashuvirat@gmail.com") #change email to your required or else use temp mail also 

#otp will not enter manually you must enter it 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(15)

driver.maximize_window()
time.sleep(7)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform() #change to your required ratings i putted 90% rating x and y values

time.sleep(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

time.sleep(50)

driver.close()


