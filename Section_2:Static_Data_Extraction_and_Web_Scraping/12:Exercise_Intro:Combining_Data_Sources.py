'''
1 Combining two data sources

Now that we have created a webscrap to get a list of company ticker symbols and we also have
a webscrap to get more financial information for them from the Yahoo Finance website, it’s
time to combine these information sources.

Modify the programs weve created in the previous lecture to have a program that scraps
the list of S&P 500 companies for the ticker symbols, and gets the additional information from
the Yahoo Finance website.

Furthermore, put this data into a pandas dataframe (in whatever format you think is
good/appropriate for further analysis) and save it to a csv file.

Challenge:
Make this webscrap run every 15 seconds, and make sure to not overwrite your previous data file.

1. You can use the time module to get the current time and also have your program wait
for a specific amount of time
    (a) You can use time.time() to get the current epoch time
    (b) You can store time.time() in a variable to keep track of the time that an event
    occurred and reference it later (or subtract it from calling time.time() again to get
    the time difference between the event and now)
    (c) You can use time.sleep(seconds) to make your program wait for a specific number of
    seconds
2. You can use the os module to check if a specific file exists
    (a) You can use os.path.isfile(pathToFile) to check if the file at the location referenced
    in pathToFile exists.
    E.g. os.path.isfile(”test/rt.txt”) checks if the file rt.txt exists in the folder test (relative to the folder where the program is saved).
3. Also use the datetime module an create an extra column that keeps track of the time the
information was recorded
    (a) You can use datetime.datetime.now() to get the current date and time
    (b) You can use the .timestamp() on a datetime object to get the epoch timestamp
    (e.g.datetime.datetime.now() gives the current datetime’s epoch time)
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time,os,datetime

def getFinancialInformation(symbol):
    url = "https://finance.yahoo.com/quote/"+symbol+"/"

    response = requests.get(url)
    responseText = response.text
    soup = BeautifulSoup(responseText,features="html.parser")
    trs = soup.find_all("tr")

    finalName = "1y Target Est"  
    names = []
    values = []
    namVal = {}




    for i in range(len(trs)):
        for j in range(len(trs[i].contents)):
            if j == 0:#name
                try:
                    name = trs[i].contents[j].text
                    names.append(name)
                except:
                    continue    
            if j == 1:#value
                try:
                    value = trs[i].contents[j].text
                    values.append(value)  
                except:
                    continue    
        namVal[name]=value 
        if name == finalName:
            break         

    return names,values

def getCompanyList():
    wikiUrl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    response = requests.get(wikiUrl)
    pageText = response.text
    soup = BeautifulSoup(pageText,features="html.parser")

    tickerSymbols = []
    tbody = soup.find_all("tbody")

    for i in range(len(tbody[0].contents)):
        if i<2:
            continue
        if i%2 !=0:
            continue
    
        symbol = tbody[0].contents[i].contents[1].text
        tickerSymbols.append(symbol.strip("\n"))
        if len(tickerSymbols) == 505:
            break

    return tickerSymbols

while True:
    #Check current time
    start = time.time()

    #Extract and Save data
    data = {"symbol":[],
            "metric":[],
            "value":[],
            "time":[]}

    try:
        tickerSymbols = getCompanyList()
    except Exception as e:
        print(str(e))
        break

    for symbol in tickerSymbols:
        try:
            names,values = getFinancialInformation(symbol)
        except Exception as e:
            print(str(e))
            continue    
        collectedTime = str(datetime.datetime.now())

        for i in range(len(names)):
            data["symbol"].append(symbol)
            data["metric"].append(names[i])
            data["value"].append(values[i])
            data["time"].append(collectedTime)


    df = pd.DataFrame(data)
    savePath = "financialData.csv"
    if os.path.isfile(savePath):
        #don't overwrite
        df.to_csv(savePath,mode="a",header=False,columns=["symbol","metric","value","time"])
    else:
        #create
        df.to_csv(savePath,columns=["symbol","metric","value","time"])

    #Wait until 15 seconds have passed from above
    timeDiff = time.time()-start
    if 15-timeDiff>0:
        time.sleep(15-timeDiff)