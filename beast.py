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

time.sleep(5)

input=driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/div/div[2]/ul/li[5]/div/span')
input.click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span')
input.click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[3]')
input.click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button/span')
input.click()
