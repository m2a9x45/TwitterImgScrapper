import requests
from bs4 import BeautifulSoup

#https://en.wikipedia.org/wiki/List_of_companies_operating_trains_in_the_United_Kingdom

def main():
    urlList = ['https://twitter.com/ScotRail','https://twitter.com/LDNOverground','https://twitter.com/AvantiWestCoast','https://twitter.com/c2c_Rail','https://twitter.com/CalSleeper',
    'https://twitter.com/chilternrailway','https://twitter.com/CrossCountryUK','https://twitter.com/EastMidRailway','https://twitter.com/Eurostar','https://twitter.com/TLRailUK',
    'https://twitter.com/SouthernRailUK','https://twitter.com/GNRailUK','https://twitter.com/GatwickExpress','https://twitter.com/GC_Rail','https://twitter.com/greateranglia',
    'https://twitter.com/GWRHelp','https://twitter.com/HeathrowExpress','https://twitter.com/Hull_Trains','https://twitter.com/LNER','https://twitter.com/merseyrail',
    'https://twitter.com/northernassist','https://twitter.com/Se_Railway','https://twitter.com/sw_help','https://twitter.com/TfLRail','https://twitter.com/TPExpressTrains',
    'https://twitter.com/tfwrail','https://twitter.com/WestMidRailway']

    for url in urlList:
        # logoUrl = getImageUrl(url)
        x = url.split("/")
        name = x[3]
        print(name + ".jpg")
        # getImageFromUrl(logoUrl, name)

def getImageUrl(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find('img', class_="ProfileAvatar-image")
    logoUrl = images['src']
    return logoUrl

def getImageFromUrl(url, name):
    response = requests.get(url)
    if response.status_code == 200:
        with open("imgs/{0}.jpg".format(name), 'wb') as f:
            f.write(response.content)

if __name__ == "__main__":
    main()