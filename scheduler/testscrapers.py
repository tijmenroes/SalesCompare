from scheduler import lidlscraper, aldiscraper  

def main(supermarket):
    res = None
    if supermarket == "Lidl":
        res = lidlscraper.main()
    elif supermarket == "Jumbo":
        res = "test"
    elif supermarket == "Aldi":
        res = aldiscraper.main()
    return res