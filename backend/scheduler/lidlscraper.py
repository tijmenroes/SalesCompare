from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

thisyear = "/" + str(datetime.now().year)

def format_date(date):
    return datetime.strptime(date, '%d/%m/%Y').strftime('%d-%m-%Y')

def get_dates(key, startdate=None, enddate=None):
    if key.find("vanaf") != -1:
        start = key[9:14] + thisyear
        startdate = format_date(start)
    else:
        start = key[3:8] + thisyear
        end = key[14:19] + thisyear
        startdate = format_date(start)
        enddate = format_date(end)
    return (startdate, enddate)

def finalise_data(data):
    # result = {}
    # for entry in data:
    #     product_data = entry["product_data"]
    #     if entry["date"] not in result:
    #         result[entry["date"]] = [product_data]
    #     else:
    #         result[entry["date"]].append(product_data)
    res = []
    for key in data:
        start, end = get_dates(key)
        res.append({"start": start, "end": end, "data": data[key]})

    print(res)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.lidl.nl/acties")
# Wait for cookie button to appear
driver.implicitly_wait(5)
try:
    cookiebtn = driver.find_element_by_class_name(
        "cookie-alert-extended-button")
    cookiebtn.click()
finally:
    print('button clicked')


try:
    driver.execute_script("window.scrollBy(0,1000)")
    driver.implicitly_wait(5)
    
    products = driver.find_elements_by_class_name("product--tile") 
    
finally:
    # products = driver.find_elements_by_class_name("product--tile")
    print(products)
    scraped_data = {}

    for product in products:
        date = product.find_element_by_class_name("ribbon__item--primary").text
        product_data = {
            "title":  product.find_element_by_class_name("product__title").text,
            "action_desc": product.find_element_by_class_name("pricebox__highlight").text,
            "action_price": product.find_element_by_class_name("pricebox__price").text
        }
        if date not in scraped_data:
            scraped_data[date] = [product_data]
        else:
            scraped_data[date].append(product_data)

        finalise_data(scraped_data)
        driver.quit()