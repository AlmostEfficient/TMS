# TMS - TradeMe Scaper
Tiny-ish scripts to scrape items from auction site TradeMe using urlopen and BeautifulSoup. I mainly use this from my terminal when working so I don't have to click stuff. 

__Tip:__ Put these scripts in a folder in your PATH variable and you can run them from __anywhere__ using [PowerToys Run](https://github.com/microsoft/PowerToys/wiki/PowerToys-Run-Overview) in a few keystrokes.

## Requirements
- bs4 -  `pip install bs4`

## Available scripts
* __gpus.py__ - Runs a search for items in the "Video card" category filtered for used only, sorted by latest listings. Prints the first page of results and saves to a csv file in C:/Data. Pass in "new" as the second argument to include new items.

* __cpus.py__ - Runs a search for used AMD CPUS, sorted by latest listings. Prints the first page of results and saves to a csv file in C:/Data. Pass in "new" as the second argument to include new items.

## Disclaimer
Scraping data is against TradeMe's Terms and Conditions. Don't use this. I made this for educational purposes.
> No scraping: You may not use a robot, spider, scraper or other unauthorised automated means to access the Site or information featured on it for any purpose. You also may not manually scrape, harvest or otherwise extract data from our Site without our express permission.

Also, I suck at Python so there's ~~probably~~ bugs.
