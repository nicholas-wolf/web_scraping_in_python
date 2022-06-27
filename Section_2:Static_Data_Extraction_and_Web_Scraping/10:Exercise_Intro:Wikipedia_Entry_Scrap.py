# 1 Wikipedia table scrap
# Our next goal is going to be to scrap all the data from the yahoo finance 
# for a list of 505 companies that are part of the S&P 500 index.
# To do this we first need to know what all of these companies are and what their ticker symbol is.

# In this exercise please write a webscraper that gets the ticker symbol (called Symbol in 
# the table) from the Wikipedia entry on the S&P 500 companies.

import requests
from bs4 import BeautifulSoup

wikiUrl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

response = requests.get(wikiUrl)
pageText = response.text
soup = BeautifulSoup(pageText,features="html.parser")

tickerSymbols = []
tbody = soup.find_all("tbody")
endSymbol = "ZTS"
# print(tbody[0].contents[2])

for i in range(len(tbody[0].contents)):
    if i<2:
        continue
    if i%2 != 0:#looking for even numbers
        continue
    # if int(i/2) != i/2: ###alternate way of finding the even numbers###
    #     continue

    #this is where the symbol text is
    symbol = tbody[0].contents[i].contents[1].text
    tickerSymbols.append(symbol)
    if len(tickerSymbols) == 505:
        break

print(tickerSymbols[20])