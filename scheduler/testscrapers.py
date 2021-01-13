from scheduler import lidlsoupscraper  

def main(supermarket):
    res = None
    print(supermarket)
    if supermarket == "Lidl":
        res = lidlsoupscraper.main()
        # print(res)
    elif supermarket == "Jumbo":
        res = "test"
        print("NO")
    return res

# main("lidl")