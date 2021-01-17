from scrapers import lidlscraper, aldiscraper, ahscraper

def main(supermarket):
    res = None
    if supermarket == "Lidl":
        res = lidlscraper.main()
    elif supermarket == "Jumbo":
        res = "test"
    elif supermarket == "Aldi":
        res = aldiscraper.main()
    elif supermarket == "Albert heijn":
        res = ahscraper.main()
    return res