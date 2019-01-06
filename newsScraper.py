"""
Scrapes news articles for a certain company
to feed NLP algorithm
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Driver to open a browser
chromedriver = "/Users/fbomfim/bin/chromedriver"
driver = webdriver.Chrome(chromedriver)

"""
Loads all the paragraphs from a given
website into news.txt
args: url (string with the website url)
"""
def loadText(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    # open news document
    news = open("news.txt", 'a')
    # gets paragraphs
    try:
        paragraphs = soup.findAll('p')
        for paragraph in paragraphs:
            news.write(paragraph.text.encode('utf-8').strip() + "\n")
    except AttributeError:
        print("Couldn't load " + url)
    news.close()

"""
Find all news from Google given a query
and writes them into news.txt
args: name (string with the query)
"""
def getNews(name):
    url = "https://www.google.com/search?q=" + name +  "&rlz=1C5CHFA_enUS814US816&tbas=0&tbm=nws&source=lnt&tbs=qdr:d&sa=X&ved=0ahUKEwiIiMrpwc7fAhXElZAKHWrVBywQpwUIIQ&biw=1440&bih=821&dpr=2"
    driver.get(url)
    urlBoxes = driver.find_elements_by_css_selector("a.l.lLrAF") + driver.find_elements_by_css_selector("RNTUJf")
    for box in urlBoxes:
        loadText(box.get_attribute('href'))
    driver.quit()
# loads all the news in news.txt
companies = ['tesla']
for company in companies:
    getNews(company)
               
