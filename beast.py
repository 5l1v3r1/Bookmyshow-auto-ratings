from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/777-charlie/ET00077150")  #change which moview you want to auto ratings

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_css_selector('#super-container > div.sc-1hbje21-1.kziggM > div > div > div > div.sc-iujRgT.cSkjY > div > div.sc-exAgwC.eJpBoy > div > div:nth-child(2) > div > div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("yashuvirat@gmail.com") #change email to your required or else use temp mail also 

time.sleep(3)

#otp must enter you only its can't be automated

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(10)

driver.maximize_window()
time.sleep(10)

#driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(7)

#currently working on auto drag and rating so plz rate in that section i will coming soon

#driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div > div.rating-slider.desktop-rating-slider > div.range-thumb').click()

#time.sleep(8)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

time.sleep(50)

driver.close()



