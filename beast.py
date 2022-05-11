from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/login/?referer=/bengaluru/movies/beast/ET00311733")

input=driver.find_element_by_xpath('//*[@id="wzrk-confirm"]')
input.click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div')
input.click()

input=driver.find_element_by_xpath('//*[@id="emailId"]')
input.send_keys('putyrid123@gmail.com')

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button')
input.click()

#if i find dragging button ratings  i will update it plz select rate button and rate the movie


