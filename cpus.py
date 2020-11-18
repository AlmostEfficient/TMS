from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime
import os
import sys

# AMD CPUs - Used, latest listings
url = 'https://www.trademe.co.nz/a/marketplace/computers/components/cpus/amd/search?sort_order=expirydesc&condition=used'

# AMD CPUs - New & used, latest listings
try:
    if sys.argv[1] == 'new': #If the user passed in new as the second argument when launching the script, change the url 
        url = 'https://www.trademe.co.nz/a/marketplace/computers/components/cpus/amd/search?sort_order=expirydesc'
except IndexError:
    pass

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

#Parsing date & time for the name of the CSV file
file_name = datetime.now().strftime("%Y%m%d_%H%M") +' CPUS.csv'
#Deciding where to save the file, I'm using an absolute path
save_path = 'C:\Data'
#Combining the path and the name of the file
file_path = os.path.join(save_path, file_name)
if not os.path.exists(save_path): #In case the folder doesn't exist
    os.makedirs(save_path)
f = open(file_path, 'w')
headers = "Title, Reserve, Buy now\n"
f.write(headers)

for container in containers:

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

    print(title + " || Reserve: " + res + " || Buy now: " + bn)

    f.write(title.replace(",", "|") + "," + res + "," + bn + "\n")

wait = input("Press Enter to continue.")