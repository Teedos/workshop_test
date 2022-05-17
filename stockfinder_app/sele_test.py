
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
import os


#import requests, bs4

def get_history_table(driver,url):
    """"service = Service('/opt/homebrew/bin/geckodriver')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service,options=options)""" 
    driver.get(url)
    table = driver.find_element(By.CLASS_NAME, 'historical_data_table.table')
    return table.get_attribute('innerHTML')
    
def search_name(target, names):
    for name in names:
        if target.lower()== name.text.lower():
            return name.get_attribute('href')
    return 'Company Not found'

def search_stock(url, target):
    """service = Service('/opt/homebrew/bin/geckodriver')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service,options=options) """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url)
    links = driver.find_elements(By.CLASS_NAME, 'ajax-chart a')
    link = search_name(target, links)
    table = get_history_table(driver, link)
    return table

"""def search_name(target, lists):
    return 

def search_history_table(soup):
    table = soup.select_one('.historical_data_table.table')
    return table

def search_bs():
    url = 'https://www.macrotrends.net/stocks/stock-screener'
    res = requests.get(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    target = 'apple'
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    print(soup)
    links = soup.select_one(".ajax-chart")
    print(links)"""
    #table = search_history_table
    #print(table)
#url = 'https://www.macrotrends.net/stocks/stock-screener'
#search_bs()
#print(search_stock(url,'NVIDIA'))