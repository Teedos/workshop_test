
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


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
    service = Service('/opt/homebrew/bin/geckodriver')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service,options=options) 
    driver.get(url)
    links = driver.find_elements(By.CLASS_NAME, 'ajax-chart a')
    link = search_name(target, links)
    table = get_history_table(driver, link)
    return table

#url = 'https://www.macrotrends.net/stocks/stock-screener'

#print(search_stock(url,'NVIDIA'))