# wow_auction_analyzer

## Overview
This project aims to help World of Warcraft players to collect auction data and do some analysis. Right now this analyzer can get latest price of all items in your "wish list", compare it with your ideal price and tell whether it's a good price or not. With the help of this analyzer, players can save gold on daily flask and potion, earn more gold on their trade oriented skills and save time on their long-term investiment. This analyzer are tested in Windows10 only and may not work for other environments.

## Requirements
1, install packages including pandas, bs4, selenium and lxml. 
2, install Google Chrome. 
3, download chromedriver from https://chromedriver.chromium.org/downloads and extract it to get a chromedriver.exe and move it to your Scripts folder for your python interpreter.
For example, for a python interpreter on "C:/python/python.exe", the chromedriver.exe should be on "C:/python/Scripts/chromedriver.exe".

## How to run
1, build your own "wish list". Open target.csv file in src folder and add or modify items with item id( the unique identification you can find in WoW), name( as long as you know what it is), wtb( the price at which you want to buy) and wts( the price at which you want to sell). 
You can use https://theunderminejournal.com to determine wtb and wts.
DO NOT modify the first row of the csv file.
2, set your own base url for the scanner. Go to https://theunderminejournal.com and choose your region and realm to get the url and modify the base_url. 
For example, mine is "https://theunderminejournal.com/#us/illidan" so I need to change the base_url on line 12 of scanner.py into "https://theunderminejournal.com/#us/illidan/item/".
3, just ensure you have a good network environment and get analysis results easily by running scanner.py!

## How to customize
In scanner.py, you can collect more data you want from the website with soup variable in get_info function.
In AHitem.py, you can change the boring word like "very expensive" into interesting ones like "sell now or go die!", change how the analyzer judge the price, and add any rules you want using other collected data like mean price or quantity.

## Future
I'm planning to add database support to get a better and more stable data structure for coming various data science tools. 
After that I will try to build a price_dectector which can generate wtb and wts for an item id automatically so that the "wish list" can be created much more easily with only an item id as input, no searching on theunderminejournal any more!
