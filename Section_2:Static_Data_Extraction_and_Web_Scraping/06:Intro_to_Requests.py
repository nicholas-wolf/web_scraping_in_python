import requests

url = "https://finance.yahoo.com/quote/AAPL/"

prop = "Previous Close"

response = requests.get(url)

print(response)
print(response.status_code==200)
text = response.text

ind = text.index("Previous Close")

reduceText = text[ind:ind+200]
print(reduceText)

reduceTextSplit = text[ind:].split("</td>") [1]
value  = reduceTextSplit.split(">")[-1]
#print(reduceTextSplit[:3])

print(value)