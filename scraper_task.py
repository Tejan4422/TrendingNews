from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome("C:/Users/Tejan/Documents/web_scraping/chromedriver")
url = "https://www.youtube.com/feed/trending"
driver.set_window_size(1120, 1000)
driver.get(url)
tags = driver.find_elements_by_xpath('.//h3[@class = "title-and-badge style-scope ytd-video-renderer"]')
taglen = len(tags)
tag1 = []
for i in range(taglen):
    tag1.append(tags[i].text)