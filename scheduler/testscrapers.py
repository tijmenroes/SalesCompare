from scheduler import lidlsoupscraper, aldisoupscraper  

def main(supermarket):
    res = None
    print(supermarket)
    if supermarket == "Lidl":
        res = lidlsoupscraper.main()
        # print(res)
    elif supermarket == "Jumbo":
        res = "test"
        print("NO")
    elif supermarket == "Aldi":
        res = aldisoupscraper.main()
    return res

# main("lidl")