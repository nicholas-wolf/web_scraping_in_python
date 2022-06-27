from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.google.com"

browser = webdriver.Chrome(executable_path= "/Users/nicholaswolf/Documents/web_scraping_in_python/Section_3:Scraping_Websites_That_Load_Data_With_Javascript/chromedriver")

browser.get(url)

inputElement = browser.find_element(By.NAME, "q")
inputElement.send_keys("Yahoo Finance")
inputElement.submit()

browser.quit()