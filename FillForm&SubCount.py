from selenium import webdriver
import time
import Config as config
import gmail

#--------------------------------------------------------------------------------------------
# Part 1

driver = webdriver.Chrome()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSek4lvyKCkjeKHJwRRSUdsNb4WCIohFNlog7YjeWVzmEr3DQQ/viewform')

time.sleep(2)

last_name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last_name.send_keys('Kattimani')

first_name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first_name.send_keys('Rishab')

RadioButtonPeriod = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
RadioButtonPeriod.click()

Submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()

#-----------------------------------------------------------------------------------------------
# Part 2

driver.get('https://www.youtube.com/channel/UC6OrQk8WsnCOR1OezlUU9zQ')

get_confirmation_div_text = driver.find_element_by_xpath('//*[@id="subscriber-count"]')
print(get_confirmation_div_text.text)


gmail.send_email('YOUR_EMAIL', get_confirmation_div_text.text)
