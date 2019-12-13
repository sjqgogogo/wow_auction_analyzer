import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import lxml
from selenium.webdriver.support import expected_conditions as EC
from AHitem import AHitem


def get_info(item_id, df):
    # get soup
    base_url = 'https://theunderminejournal.com/#us/illidan/item/'
    url = base_url+str(item_id)
    ah_item = AHitem(item_id, df)
    i = 0
    # get all attributes of ah_item
    while True:
        soup = get_soup(url)
        if not ah_item.current_price:
            ah_item.current_price = get_num(soup, '#item-page > div.item-stats > table > tr.current-price > td > span')
        if not ah_item.median_price:
            ah_item.median_price = get_num(soup, '#item-page > div.item-stats > table > tr:nth-child(4) > td > span')
        if not ah_item.mean_price:
            ah_item.mean_price = get_num(soup, '#item-page > div.item-stats > table > tr:nth-child(5) > td > span')
        if not ah_item.quantity:
            ah_item.quantity = get_num(soup, '#item-page > div.item-stats > table > tr:nth-child(1) > td > span')
        if ah_item.current_price != [] and ah_item.mean_price != [] and ah_item.median_price!=[] and ah_item.quantity!=[]:
            break
        if i > 10:
            break
        i += 1
    return ah_item


def get_soup(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    browser.close()
    return soup


def get_num(soup, sel):
    temp = soup.select(sel)
    if type(temp)==type([]) and len(temp)>0:
        tag = temp[0]
        try:
            num = float(tag.string)
        except:
            num = tag.string
    else:
        num = temp
    return num


if __name__=='__main__':
    df = pd.read_csv('target.csv')
    for id in df['id']:
        info = get_info(id, df)
        # info.showall()
        info.show(df)