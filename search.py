from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime
import os
import sys
#Don't try this at 127.0.0.1
def search(term, *args):
    url = 'https://www.trademe.co.nz/a/marketplace/computers/components/search?search_string='+term+'&condition=used&sort_order=expirydesc'
    #Requesting the page
    uClient = uReq(url)
    #Storing the html of the page
    page_html = uClient.read()
    #Closing the connection
    uClient.close()

    #Parsing the HTML with Beautiful Soup
    page_soup = soup(page_html, 'html.parser')
    #Grabbing each card item on the page (TradeMe items have a class of 'o-card')
    containers = page_soup.findAll('div', {'class': 'o-card'})

    for index, container in enumerate(containers):

        title_container = container.findAll('div', {'id': '-title'})
        title = title_container[0].text.strip()

        try:
            res_container = container.findAll('div', {'id': '-price'})
            res = '$'+res_container[0].text.strip().split('$',1)[1] 
        except: 
            res = "N/A"

        try:
            bn_container = container.findAll('div', {'id': '-buy-now'})
            bn = '$'+bn_container[0].text.strip().split('$',1)[1] 
        except:
            bn = "N/A"
        print(str(index) +": "+title + " || Reserve: " + res + " || Buy now: " + bn)

if __name__ == "__main__":
    try:
        search(sys.argv[1])
    except IndexError:
        search(input('Enter search term: '))

wait = input("Press enter to exit.")
