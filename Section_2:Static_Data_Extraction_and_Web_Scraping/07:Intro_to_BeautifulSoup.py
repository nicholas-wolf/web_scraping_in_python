import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/"

response = requests.get(url)

responseText = response.text

soup = BeautifulSoup(responseText,features="html.parser")

trs = soup.find_all("tr")
print(trs[0].text)

print(trs[0].td)

print(trs[0].td.text)

print(trs[0].td.span.text)

print(trs[0].span.text)

print(trs[0].contents)

# first element
print(trs[0].contents[0].text)

# second element
print(trs[0].contents[1].text)

tds = soup.find_all("td",class_="C($primaryColor) W(51%)")
print(tds[0])
print(tds[1])

print(trs[0].find("td",attrs={"data-test":"PREV_CLOSE-value"}).text)