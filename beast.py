from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/login/?referer=/bengaluru/movies/beast/ET00311733")

input=driver.find_element_by_xpath('//*[@id="wzrk-confirm"]')
input.click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div')
input.click()

input=driver.find_element_by_xpath('//*[@id="emailId"]')
input.send_keys('putyrid123@gmail.com') #Replace With Your Mail OTP Will Not Be Auto Fill You Must Enter It👍

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button')
input.click()

#It Ask Rate Now Click On That & Rate The Movie And Click Submit (If I Find Drag Automatically I Will Update It👍)




