from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd


def open_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--allow-running-insecure-content")
    # chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=
                              chrome_options)
    driver.maximize_window()
    
    driver.get('https://www.melkeirani.com/')
    
    time.sleep(10)
    from_date = driver.find_element(By.ID, 'tar1')
    to_date = driver.find_element(By.ID, 'tar2')
    
    ##################### DON'T FORGET TO CHANGE DATE ############################
    from_date.send_keys('1402/06/11')  
    to_date.send_keys('1402/06/12')
    time.sleep(3)
    show_button = driver.find_element(By.ID, 'searchbut')
    show_button.click()
    time.sleep(3)
    return driver
    

def get_homes(driver):
    cards = driver.find_elements(By.CSS_SELECTOR, '.col-lg-4.col-xl-3.col-md-12.mb-4')
    
    homes_links = []
    for card in cards:
        link_element = card.find_element(By.TAG_NAME, 'a')
        href = link_element.get_attribute('href')
        homes_links.append(href)
    
    return homes_links

def load_more(driver):
    try:
        load_more_button = driver.find_element(By.CLASS_NAME, 'loadmore') 
        actions = ActionChains(driver)
        actions.move_to_element(load_more_button).perform()
        load_more_button.click()
        time.sleep(8)  # Wait for the new homes to load
    except Exception as e:
        print(f"Error loading more homes: {e}")
    
def how_homes(driver,url):
    driver.get(url)
    homes_df = pd.DataFrame(columns=['movie_id', 'type','date', 'address', 'area','infrastructure', 'floors_sum', 'homes_num','floor_num','rooms', 'property_direction', 'view','flooring', 'wall','cabinet','cooler','water','electricity','gas','age','elevator','parking','desc','price','mortgage','rent','facilities'])
    
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
    
    try:
        floors_sum_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(2) td:nth-child(1)').text
        floors_sum_dr = floors_sum_dr.split('\n')
        floors_sum = int(floors_sum_dr[1])
    except:
        floors_sum = "couldn't crawl"
        
    try:
        homes_num_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(2) td+ td').text
        homes_num_dr = homes_num_dr.split('\n')
        homes_num = int(homes_num_dr[1])
    except:
        homes_num = "couldn't crawl"
        
    try:
        floor_num_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) td:nth-child(1)').text
        floor_num_dr = floor_num_dr.split('\n')
        floor_num = int(floor_num_dr[1])
    except:
        floor_num = "couldn't crawl"
    
    try:
        rooms_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) td+ td').text
        rooms_dr = rooms_dr.split('\n')
        rooms = int(rooms_dr[1])
    except:
        rooms = "couldn't crawl"
        
    try:
        property_direction_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(4) td:nth-child(1)').text
        property_direction_dr = property_direction_dr.split('\n')
        property_direction = property_direction_dr[1]
    except:
        property_direction = "couldn't crawl"
    
    try:
        view_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(4) td+ td').text
        view_dr = view_dr.split('\n')
        view = view_dr[1]
    except:
        view = "couldn't crawl"
        
    try:
        flooring_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(5) td:nth-child(1)').text
        flooring_dr = flooring_dr.split('\n')
        flooring = flooring_dr[1]
    except:
        flooring = "couldn't crawl"
    
    try:
        wall_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(5) td+ td').text
        wall_dr = wall_dr.split('\n')
        wall = wall_dr[1]
    except:
        wall = "couldn't crawl"
        
    try:
        cabinet_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(6) td:nth-child(1)').text
        cabinet_dr = cabinet_dr.split('\n')
        cabinet = cabinet_dr[1]
    except:
        cabinet = "couldn't crawl"
    
    try:
        cooler_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(6) td+ td').text
        cooler_dr = cooler_dr.split('\n')
        cooler = cooler_dr[1]
    except:
        cooler = "couldn't crawl"
        
    try:
        water_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(7) td:nth-child(1)').text
        water_dr = water_dr.split('\n')
        water = water_dr[1]
    except:
        water = "couldn't crawl"
        
    try:
        electricity_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(7) td+ td').text
        electricity_dr = electricity_dr.split('\n')
        electricity = electricity_dr[1]
    except:
        electricity = "couldn't crawl"
    
    try:
        gas_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(8) td:nth-child(1)').text
        gas_dr = gas_dr.split('\n')
        gas = gas_dr[1]
    except:
        gas = "couldn't crawl"
        
    try:
        age_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(8) td+ td').text
        age_dr = age_dr.split('\n')
        age = int(age_dr[1])
    except:
        age = "couldn't crawl"
    
    try:
        elevator_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(9) td:nth-child(1)').text
        elevator_dr = elevator_dr.split('\n')
        elevator = elevator_dr[1]
    except:
        elevator = "couldn't crawl"
        
    try:
        parking_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(9) td+ td').text
        parking_dr = parking_dr.split('\n')
        parking = parking_dr[1]
    except:
        parking = "couldn't crawl"
        
    try:
        desc_dr = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(10) td:nth-child(1)').text
        desc_dr = desc_dr.split('\n')
        desc = desc_dr[1]
    except:
        desc = "couldn't crawl"    
    
    try:
        facilities = []
        facilities_dr = driver.find_elements(By.CSS_SELECTOR, '.sadiv')
        for f in facilities_dr:
            facilities.append(f.text)
    except:
        facilities = "couldn't crawl"
        
    try:
        price_dr = driver.find_element(By.CSS_SELECTOR, '.col-xl-10').text
        price_dr = price_dr.replace('قیمت :', '').replace('تومان', '').replace(',', '').strip()
        price = price_dr
    except:
        price = "couldn't crawl" 
    
    try:
        mortgage_dr = driver.find_element(By.CSS_SELECTOR, '.col-xl-5:nth-child(1)').text
        mortgage_dr = mortgage_dr.replace('رهن :', '').replace('تومان', '').replace(',', '').strip()
        mortgage = mortgage_dr
    except:
        mortgage = "couldn't crawl"
        
    try:
        rent_dr = driver.find_element(By.CSS_SELECTOR, '.price+ .col-xl-5').text
        rent_dr = rent_dr.replace('اجاره :', '').replace('تومان', '').replace(',', '').strip()
        rent = rent_dr  
    except:
        rent = "couldn't crawl"

    try:
        facilities = []
        facilities_dr = driver.find_elements(By.CSS_SELECTOR, '.sadiv')
        for f in facilities_dr:
            facilities.append(f.text)
    except:
        facilities = "couldn't crawl"
    
    return {
        'related_link': link,
        'type': type_home,
        'date' : date,
        'address': address,
        'area': area,
        'infrastructure' : infrastructure,
        'floors_sum' : floors_sum,
        'homes_num' : homes_num,
        'floor_num' : floor_num,
        'rooms' : rooms,
        'property_direction' : property_direction,
        'view' : view,
        'flooring' : flooring,
        'wall' : wall,
        'cabinet' : cooler,
        'cooler' : cooler,
        'water' : water,
        'electricity': electricity,
        'gas' : gas,
        'age' : age,
        'elevator' : elevator,
        'parking' : parking,
        'desc' : desc,
        'price' : price,
        'mortgage' : mortgage,
        'rent' : rent,
        'facilities' : facilities
        
    }

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('homes_data_1.csv', index=False,encoding='utf-8-sig')
    print("Data saved to homes_data.csv")
    
    
def main():
    driver = open_driver()
    homes_data = []
    homes_links = set()
    
    # Continue loading until no new links are found
    while True:
        current_size = len(homes_links)
        
        # Get new homes and add to the set (set automatically avoids duplicates)
        homes_links.update(get_homes(driver))
        
        # If the size of the set does not increase after loading more, break the loop
        if len(homes_links) == current_size:
            print("No new homes found, stopping the load.")
            break
        time.sleep(2)
        # Load more homes
        load_more(driver)
        time.sleep(2)
    
    # Collect details for each home link
    print(f"Total homes found: {len(homes_links)}")
    for link in homes_links:
        home_details = how_homes(driver, link)
        homes_data.append(home_details)
    
    # Save the data to CSV
    save_to_csv(homes_data)

    driver.quit()


    
if __name__ == "__main__":
    main()
    
    
