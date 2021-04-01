import emoji
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import sys
# Replace below path with the absolute path of the \
#chromedriver in your computer
for i in range(100):
	driver = webdriver.Chrome('/home/srijithreddy/Desktop//srijith reddy/chromedriver')
	driver.get("https://www.youtube.com/watch?v=PX3xzLJsdkI")
	#driver.set_window_size(4, 4) # to set window size
	element = driver.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
	element.click()		
	element2 = driver.find_element_by_xpath("//button[@class='ytp-mute-button ytp-button']")# to mute
	element2.click()		
	time.sleep(10)
# time.sleep()
	driver.close()
