import requests
import json
from datetime import datetime

from bs4 import BeautifulSoup

url = 'https://www.lidl.nl/acties'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

thisyear = "/" + str(datetime.now().year)

def format_date(date):
    return datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')

def get_dates(key, startdate=None, enddate=None):
    if key is not None:
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
    res = []
    for key in data:
        start, end = get_dates(key)
        res.append({"time_start": start, "time_end": end, "sales": data[key]})
    return res

def main():
    products = soup.find_all('article', class_='product--tile')
    scraped_data = {}
    for product in products:
        date_desc = None
        sale_desc = None
        if product.find('li', class_='ribbon__item--primary'):
            date_desc = product.find('li', class_='ribbon__item--primary').get_text(strip=True)
        if product.find('li', class_='ribbon__item--danger'):
            sale_desc = product.find('li', class_='ribbon__item--danger').get_text(strip=True)
        if product.find('span', class_='pricebox__recommended-retail-price'):
            old_price =  product.find('span', class_='pricebox__recommended-retail-price').get_text(strip=True)


        product_data = {
            "title": product.find('h3', class_='product__title').get_text(strip=True),
            "old_price": old_price.replace("cake.pricebox.originalPrice", ''), #weird tag from Lidl site that's hard to exclude
            "new_price": product.find('span', class_='pricebox__price').get_text(strip=True),
            "subtitle": sale_desc,
            "img_path": ""
        }
        if date_desc not in scraped_data:
            scraped_data[date_desc] = [product_data]
        else:
            scraped_data[date_desc].append(product_data)

    return finalise_data(scraped_data)

# main()

