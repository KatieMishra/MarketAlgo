import requests
from bs4 import BeautifulSoup
import re
import csv
import time
from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('Users/fbomfim/bin')
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)

name = 'TSLA'
url = "https://finance.yahoo.com/quote/" + name + "/history/" # yahoo website
html = requests.get(url).text # opens url
soup = BeautifulSoup(html, 'html.parser') # parses through html

driver.get(url);
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    # time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# looking at html for test
outFile = open("test.html", 'w')
outFile.write(soup.prettify())

