from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


def open_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    driver.get('https://www.melkeirani.com/')
    
    
    from_date = driver.find_element(By.ID, 'tar1')
    to_date = driver.find_element(By.ID, 'tar2')
    
    ##################### DON'T FORGET TO CHANGE DATE ############################
    from_date.send_keys('1400/11/09')  
    to_date.send_keys('1400/11/10')
    
    show_button = driver.find_element(By.ID, 'searchbut')
    show_button.click()
    

def get_homes():
    cards = driver.find_elements(By.CSS_SELECTOR, '.col-lg-4.col-xl-3.col-md-12.mb-4')

    for card in cards:

        link_element = card.find_element(By.TAG_NAME, 'a')
        
    
        href = link_element.get_attribute('href')
        
    return href

def load_more():
    load_more_button = driver.find_element(By.CLASS_NAME, 'loadmore') 
    actions = ActionChains(driver)
    actions.move_to_element(load_more_button).perform()
    load_more_button.click()
    
def how_homes(url):
    homes_df = pd.DataFrame(columns=['movie_id', 'type','date', 'address', 'area','infrastructure', 'floors_sum', 'homes_num','floor_num','rooms', 'property_direction', 'view','flooring', 'wall','cabinet','cooler','water','electricity','gas','age','elevator','parking','deed_type','facilities'])
    
    link = url
    try:
        type_home = driver.find_element(By.CSS_SELECTOR, '.kind-title').text
    except:
        type_home = "couldn't crawl"
    
    try:
        date = driver.find_element(By.CSS_SELECTOR, '.price:nth-child(1) .code').text
    except:
        date = "couldn't crawl"
        
    try:
        address_dr = driver.find_element(By.CSS_SELECTOR, '.card-title').text
        address = address_dr.replace('آدرس ملک : ','')
    except:
        address = "couldn't crawl"
        
    try:
        area_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) td:nth-child(1)').text
        area_dr = area_dr.split('\n')[1]
        area = int(area_dr.split()[0])
    except:
        area = "couldn't crawl"
        
    try:
        infrastructure_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(2) td:nth-child(1)').text
        infrastructure_dr = infrastructure_dr.split('\n')
        infrastructure = int(infrastructure_dr[1])
    except:
        infrastructure = "couldn't crawl"
    
        
    
    
    
    
    
def main():
    open_driver()
    homes = set()
    for i in range (5):
        homes.add(get_homes())
        load_more()
        
        if len(homes) == 96:
            how_homes() 
    
    