from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.google.com"

browser = webdriver.Chrome(executable_path= "/Users/nicholaswolf/Documents/web_scraping_in_python/Section_3:Scraping_Websites_That_Load_Data_With_Javascript/chromedriver")

browser.get(url)

inputElement = browser.find_element(By.NAME, "q")
inputElement.send_keys("Yahoo Finance")
inputElement.submit()

xPath = '//*[@id="gb"]/div/div[1]/a'
# element = browser.find_element(By.XPATH, xPath)
# element.click()

element = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH, xPath))).click()


# browser.quit()