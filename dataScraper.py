# scrapes the data for the algorithm

import requests
from bs4 import BeautifulSoup
import re
import csv

def loadCSV(name):
    url = "https://finance.yahoo.com/quote/" + name + "/history/" # yahoo website
    html = requests.get(url).text # opens url
    # print(html)
    soup = BeautifulSoup(html, 'html.parser') # parses through html

    # looking at html for test
    # outFile = open("test.html", 'w')
    # outFile.write(soup.prettify())

    # set up csv
    with open('stocks.csv', mode='a') as stocks:
        stockWrite = csv.writer(stocks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # set up first two rows
        try:
            nameBox = soup.find('h1', attrs={'data-reactid': '7'})
            stockWrite.writerow([nameBox.text.strip()])
        except:
            stockWrite.writerow(["error finding stock name"])
        stockWrite.writerow(['Date', 'Open', 'High', 'Low',	'Close*', 'Adj Close**', 'Volume'])

        index = 51 # html constant
        while(index < 1547): # another html constant 1547
        # use selenium to make constant bigger (more results)
            row = []
            for i in range(index, index + 13, 2):
            # ik, there are a lot of hardcoded constants, but scraping is dirty lol
                try:
                    nameBox = soup.find('span', attrs={'data-reactid': index})
                    row.append(nameBox.text.strip())
                except AttributeError:
                    row.append("error finding object")
                index += 2
            index += 1
            stockWrite.writerow(row)
        stockWrite.writerow([]) # blank row to separate companies

companyNames = ['TSLA', 'GOOGL']

for name in companyNames:
    loadCSV(name)


