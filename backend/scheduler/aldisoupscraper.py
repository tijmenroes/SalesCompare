import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

def calculate_enddate(start):
    # Calculate difference between date now, and end of the week 
    day_number = datetime.strptime(start, '%Y-%m-%d').strftime('%w')
    days_from = 7 - int(day_number)

    start_time =  datetime.strptime(start, '%Y-%m-%d')
    end_time = start_time + timedelta(days=days_from)
    return (start_time, end_time)        

def main():
    url = 'https://www.aldi.nl/onze-aanbiedingen.html'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    scraped_data = []

    product_groups = soup.find_all('div', class_='mod-offers__day')
    for product_group in product_groups:
        (start_time, end_time) = calculate_enddate(product_group.get('id'))

        products = product_group.find_all('div', class_='mod-article-tile__content')
        sales = []
        for product in products:
            old_price = None
            subtitle = None

            if product.find('s', class_='price__previous'):
                old_price = product.find('s', class_='price__previous').get_text(strip=True)
            if product.find('span', class_='price__unit'):
                subtitle =  product.find('span', class_='price__unit').get_text(strip=True)

            product_data = {
                "title": product.find('h4', class_='mod-article-tile__title').get_text(strip=True),
                "old_price": old_price,
                "new_price": product.find('span', class_='price__main').get_text(strip=True),
                "subtitle": subtitle,
                "img_path": ""
            }
            sales.append(product_data)

        obj = {"time_start": start_time, "time_end": end_time, "sales": sales}
        scraped_data.append(obj)

    return scraped_data

# main()