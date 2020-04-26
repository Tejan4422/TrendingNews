from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

#Hindustan Times
url1 = "https://www.hindustantimes.com/it-s-viral/"
titles = []
driver = webdriver.Chrome("C:/Users/Tejan/Documents/web_scraping/chromedriver")
driver.set_window_size(1120, 1000)
driver.get(url1)
headlines = driver.find_elements_by_xpath('.//div[@class = "media-heading headingfour"]')
headlen = len(headlines)
for i in range(headlen):
    titles.append(headlines[i].text+"*HT")
    
driver = webdriver.Chrome("C:/Users/Tejan/Documents/web_scraping/chromedriver")
for i in range(2,11):
    url2 = "https://www.hindustantimes.com/it-s-viral/?pageno="
    url2 = url2 + str(i)
    print(url2)
    driver.set_window_size(1120, 1000)
    driver.get(url2)    
    headlines = driver.find_elements_by_xpath('.//div[@class = "media-heading headingfour"]')
    headlen = len(headlines)

    for i in range(headlen):       
        titles.append(headlines[i].text+"*HT")


#times of India
url3 = "https://timesofindia.indiatimes.com/mostread.cms?day=7"
titles_times = []
driver = webdriver.Chrome("C:/Users/Tejan/Documents/web_scraping/chromedriver")
driver.set_window_size(1120, 1000)
driver.get(url3)
headlines_times = driver.find_elements_by_tag_name('strong')
headlen = len(headlines_times)
for i in range(headlen):
    titles.append(headlines_times[i].text+"*TOI")

driver = webdriver.Chrome("C:/Users/Tejan/Documents/web_scraping/chromedriver")
for i in range(2,5):
    url_times = "https://timesofindia.indiatimes.com/mostread.cms?day=7&curpg="
    url_times = url_times+ str(i)
    print(url_times)
    driver.set_window_size(1120, 1000)
    driver.get(url_times)
    headlines_times = driver.find_elements_by_tag_name('strong')
    headlen = len(headlines_times)
    
    for i in range(headlen):
        titles.append(headlines_times[i].text+"*TOI")

#India Today
url4 = "https://www.indiatoday.in/trending-news"
driver = webdriver.Chrome("C:/Users/Tejan/Documents/web_scraping/chromedriver")
driver.set_window_size(1120, 1000)
driver.get(url4)
headlines_it = driver.find_elements_by_xpath('.//div[@class = "detail"]')
headlen = len(headlines_it)
for i in range(headlen):
    titles.append(headlines_it[i].text+"*IT")

driver = webdriver.Chrome("C:/Users/Tejan/Documents/web_scraping/chromedriver")
for i in range(1, 11):
    url_it = "https://www.indiatoday.in/trending-news?page="
    url_it = url_it + str(i)
    print(url_it)
    driver.set_window_size(1120, 1000)
    driver.get(url_it)
    headlines_it = driver.find_elements_by_xpath('.//div[@class = "detail"]')
    headlen = len(headlines_it)
    for i in range(headlen):
        titles.append(headlines_it[i].text+"*IT")
        
dict = {'news' : titles}
df = pd.DataFrame(dict)
df.to_csv('scraped_raw_data.csv', index = False)
        
        
        
        
