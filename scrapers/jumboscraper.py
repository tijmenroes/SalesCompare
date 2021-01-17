from selenium import webdriver

# months = ["jan", "feb", "maa", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]

PATH = "C:\Program Files (x86)\Chromedriver87\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.jumbo.com/aanbiedingen")


def main():
    products = driver.find_elements_by_class_name("jum-promotion-card")
    timeslot = driver.find_element_by_class_name("jum-promotion-datetab__link").text

    day1 = timeslot[11:13]
    month1 = timeslot[14:17]

    day2 = timeslot[22:24]
    month2 = timeslot[25:28]
    
    scrape_data(products)
    
def scrape_data(products):
    scraped_data = []
    try:
        for product in products:
            scraped_data.append({
                "product": product.find_element_by_tag_name("h4").text,
                "action_desc": product.find_element_by_tag_name("h3").text,
                "action": product.find_element_by_class_name("jum-tag-tertiary").text
            })
    finally:
        driver.quit()
        return scraped_data
    