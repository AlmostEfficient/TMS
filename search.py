from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime
import os
import sys
#Don't try this at 127.0.0.1
def search(term, *args):
    url = 'https://www.trademe.co.nz/a/marketplace/computers/components/search?search_string='+term+'&sort_order=expirydesc'
    #TODO use an argument to let user decide if they want to add &condition=used
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

    links = []
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
        
        links.append(container.find('a').get('href'))

        print(str(index) +": "+title.ljust(80, " ") + " || Reserve: " + res.ljust(7, " ") + " || Buy now: " + bn)
    if links.count == 0:
        print("No links found")
        return
    selection = input("To open a result input the number: ")
    try:
        index = int(selection)
        #TODO Check link to make sure the address matches new format or old TM format. Currently it breaks cause TM either adds /a/ or doesn't 
        address = 'https://www.trademe.co.nz'+links[int(index)]
        cmd = 'start \"\" ' if sys.platform == 'win32' else 'open \"\" '
        os.system(cmd+address)
    except ValueError:
        #TODO fix the issue with search not working if search passed through input
        print("That's not an int!")

if __name__ == "__main__":
    try:
        search(sys.argv[1])
    except IndexError:
        search(input('Enter search term: '))

#TODO Give the user the option to search again if they want - if not None, search again. Currently broken cause search(input) is broken
wait = input("Press enter to exit.")
