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
    url = 'https://www.ah.nl/bonus'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    scraped_data = []

    products = soup.find_all('div', class_='grid-item_col__1cD_2')
    sales = []
    for product in products:
        # (start_time, end_time) = calculate_enddate(product_group.get('id'))

        title =  None
        old_price = None
        subtitle = None
        new_price = None

        if product.find('span', class_="line-title_lineclamp__1ssbk"):
            title = product.find('span', class_="title_lineclamp__1ssbk").get_text(strip=True)
        if product.find('p', class_='text_root__85eHh'):
            subtitle = product.find('p', class_='text_root__85eHh').get_text(strip=True)

        if product.find('div', class_='price_was__3HvMY'):
            old_price = product.find('div', class_='price_was__3HvMY').get_text(strip=True)

        if product.find('span', class_='price_highlight__3OxG1'):
            new_price = product.find('span', class_='price_highlight__3OxG1').get_text(strip=True)

        product_data = {
            "title": title,
            "old_price": old_price,
            "new_price": new_price,
            "subtitle": subtitle,
            "img_path": ""
        }
        sales.append(product_data)

        # obj = {"time_start": start_time, "time_end": end_time, "sales": sales}
        # scraped_data.append(obj)
    print(sales)
    # return scraped_data

main()