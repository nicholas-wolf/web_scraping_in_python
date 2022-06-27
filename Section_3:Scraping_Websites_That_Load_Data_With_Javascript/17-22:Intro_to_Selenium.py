import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = "https://finance.yahoo.com/chart/AAPL#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjgsImZsaXBwZWQiOmZhbHNlLCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJzdHVkaWVzIjp7IuKAjHZvbCB1bmRy4oCMIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6IuKAjHZvbCB1bmRy4oCMIiwiZGlzcGxheSI6IuKAjHZvbCB1bmRy4oCMIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI2ZmMzMzYSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQifX19LCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkFBUEwiLCJjaGFydE5hbWUiOiJjaGFydCIsImluZGV4IjowLCJ5QXhpcyI6eyJuYW1lIjoiY2hhcnQiLCJwb3NpdGlvbiI6bnVsbH0sInlheGlzTEhTIjpbXSwieWF4aXNSSFMiOlsiY2hhcnQiLCLigIx2b2wgdW5kcuKAjCJdfX0sInNldFNwYW4iOnt9LCJsaW5lV2lkdGgiOjIsInN0cmlwZWRCYWNrZ3JvdW5kIjp0cnVlLCJldmVudHMiOnRydWUsImNvbG9yIjoiIzAwODFmMiIsInN0cmlwZWRCYWNrZ3JvdWQiOnRydWUsImV2ZW50TWFwIjp7ImNvcnBvcmF0ZSI6eyJkaXZzIjp0cnVlLCJzcGxpdHMiOnRydWV9LCJzaWdEZXYiOnt9fSwic3ltYm9scyI6W3sic3ltYm9sIjoiQUFQTCIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJBQVBMIiwicXVvdGVUeXBlIjoiRVFVSVRZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnt9fV19"

r = requests.get(url)
t = r.text

value = "BTC-USD"
if value in t:
    print("Yes")
else:
    print("No")

# to make driver not pop up
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options,executable_path="/Users/nicholaswolf/Documents/web_scraping_in_python/Section_3:Scraping_Websites_That_Load_Data_With_Javascript/chromedriver")
driver.get(url)
ps = driver.page_source

if value in ps:
    print("Yes")
else:
    print("No")


# if the whole page is needed, and data is slow. This will give 10 seconds
# driver.implicitly_wait(10)

# this is a explicit wait for slow load times
loadtime = 10
wait = WebDriverWait(driver,loadtime)
loadXPath = '//*[@id="data-util-col"]/section[2]/table/tbody/tr[1]/td[2]/p'
xPath = '//*[@id="data-util-col"]/section[2]/table/tbody/tr[1]'

try:
    wait.until(ec.visibility_of_element_located((By.XPATH,loadXPath)))
    elem = driver.find_elements(By.XPATH,xPath)
    print(elem[0].text.split("\n"))
except Exception as e:
    print(str(e))
    print("Element not visible")

# for i in range(1,6):
#     # this is how to find element by xpath 
#     elem = driver.find_elements(By.XPATH, '//*[@id="data-util-col"]/section[2]/table/tbody/tr['+str(i)+']')
#     print(elem[0].text.split("\n"))
    
# # to get hyperlink
# hrefAttribute = driver.find_elements(By.XPATH, '//*[@id="data-util-col"]/section[2]/table/tbody/tr[1]/td/a')
# print(hrefAttribute[0].get_attribute("href"))


# IMPORTANT to close driver or else you will have a bunch of chrome ext running
driver.quit()