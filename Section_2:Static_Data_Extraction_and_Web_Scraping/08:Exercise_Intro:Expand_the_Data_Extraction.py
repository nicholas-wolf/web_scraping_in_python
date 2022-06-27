# 1 Extracting all data in the table
#  Now that you’ve seen how we went about extracting the first value, 
#  see if you can extract all of the values contained within that table,  
#  starting at Previous Close and ending at 1y Target Est.

import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/"

response = requests.get(url)

responseText = response.text

soup = BeautifulSoup(responseText,features="html.parser")

finalName = "1y Target Est"
trs = soup.find_all("tr")

# print(trs[0].contents[0].text)
# print(trs[0].contents[1].text)

names = []
values = []

namVal = {}
#dict2 = {"names":names, "values":values}

# print(trs[0])

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

# print(names)
# print(values)
print(namVal)