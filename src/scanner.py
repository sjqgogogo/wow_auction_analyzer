import datetime
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from AHitem import AHitem


def get_info(item_id, df):
    # get source code of web page
    url = 'https://www.wowuction.com/us/illidan/Items/Stats/'+str(item_id)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    wait = WebDriverWait(browser,2)
    soup = BeautifulSoup(browser.page_source,'lxml')
    browser.close()

    # get all attributes for item
    ah_item = AHitem(item_id, df)
    ah_item.min_price = get_price(soup, '#AHMinBuyout > span.cur_g', '#AHMinBuyout > span.cur_s')
    ah_item.market_price = get_price(soup, '#AHMarketPrice > span.cur_g', '#AHMarketPrice > span.cur_s')
    # ah_item.average_median_price = get_price(soup,
    #                                          '#tabs_1 > div > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1)',
    #                                          '#tabs_1 > div > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2) > span:nth-child(2)')
    ah_item.current_num = get_num(soup, '#AHCount')
    ah_item.sold_per_day = get_num(soup, '#tabs_1 > div > table:nth-child(3) > tbody > tr:nth-child(6) > td:nth-child(2)')

    return ah_item




def get_num(soup, sel):
    temp = soup.select(sel)
    if type(temp)==type([]) and len(temp)>0:
        tag = temp[0]
        try:
            num = float(tag.string)
        except:
            num = tag.string
    else:
        num = 'NaN'
    return num


def get_price(soup, g_sel, s_sel):
    g = get_num(soup, g_sel)
    s = get_num(soup, s_sel)
    try:
        price = g+s/100
    except:
        price = g
    return price


if __name__=='__main__':
    df = pd.read_csv('target.csv')
    for id in df['id']:
        info = get_info(id, df)
        # info.showall()
        info.show(df)





