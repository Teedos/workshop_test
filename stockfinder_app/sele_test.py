
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import requests, bs4

"""def get_history_table(driver,url):
    #service = Service('/opt/homebrew/bin/geckodriver')
    #options = Options()
    #options.headless = True
    #driver = webdriver.Firefox(service=service,options=options)
    driver.get(url)
    table = driver.find_element(By.CLASS_NAME, 'historical_data_table.table')
    return table.get_attribute('innerHTML')
    
def search_name(target, names):
    for name in names:
        if target.lower()== name.text.lower():
            return name.get_attribute('href')
    return 'Company Not found'

def search_stock(url, target):
    #service = Service('/opt/homebrew/bin/geckodriver')
    #options = Options()
    #options.headless = True
    #driver = webdriver.Firefox(service=service,options=options) 
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
    return table"""
def get_history_table(driver):
    """"service = Service('/opt/homebrew/bin/geckodriver')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service,options=options)""" 
    #driver.get(url)
    #table = driver.find_element(By.CLASS_NAME, 'historical_data_table.table')
    table = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "historical_data_table.table")))
    return table.get_attribute('innerHTML')
    

def get_description(driver):
    description = driver.find_element(By.XPATH, "//span[contains(text(), 'Historical daily')]")
 
    return description.get_attribute('innerHTML')


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
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys(target)
    suggestion_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "typeahead__result")))
    sugg_links = driver.find_elements(By.CLASS_NAME,"typeahead__list a")
    if sugg_links:
        #sugg_link = driver.find_element(By.CLASS_NAME,"typeahead__list a")
        sugg_links[0].click()
        tabs = driver.find_element(By.CLASS_NAME, 'nav.nav-tabs a')
        #tabs = driver.find_element(By.CSS_SELECTOR, 'li a')
        tabs.click()
        table = get_history_table(driver)
        graphic = get_description(driver)
        #print(table)
        #print(graphic)
        #print(table)
        #driver.switch_to.default_content()
        return table, graphic
    #print('nothing found')
    return False, False

def get_price(driver):
    driver.find_element(By.XPATH,"//span[text() = 'Historical Data']").click()
    for i in range(0,3):
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(1)
    #table = driver.find_element(By.ID,"Col1-1-HistoricalDataTable-Proxy")
    table = driver.find_element(By.CSS_SELECTOR,"table")
    return table.get_attribute('outerHTML')

def get_summary(driver):
    summary = driver.find_element(By.ID,"quote-summary")
    return summary.get_attribute('outerHTML')
    
def search_finance(url, target):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url)
    agree_cookies = driver.find_elements(By.NAME, 'agree')
    if agree_cookies:
        agree_cookies[0].click()
    search_bar =  WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, "yfin-usr-qry")))
    search_bar.send_keys(target)
    button = driver.find_element(By.ID, 'header-desktop-search-button')
    button.click()
    summary = get_summary(driver)
    history = get_price(driver)
    #print(price)
    driver.quit()
    return  summary, history
    
#url = 'https://www.macrotrends.net/stocks/stock-screener'
#search_bs()
#print(search_stock(url,'NVIDIA'))