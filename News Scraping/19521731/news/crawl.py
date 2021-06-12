from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from datetime import datetime
import pandas as pd
import requests
import time
import json

class crawler(object):

    def __init__(self):
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(".\chromedriver.exe",chrome_options=chrome_options)
        self.delay = 3

    def get_date(self,url):
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')
        date_line = str(soup.body.findAll('p',attrs={'class':'byline'}))
        date = date_line[(date_line.find('Updated')+8):-5]
        return date
    
    def load_page(self):
        browser = self.driver
        j = 1
        while j < 1395:
            browser.get("https://www.thepoke.co.uk/category/news/page/{page}/".format(page=j))
            time.sleep(self.delay)
            all_data = browser.find_elements_by_css_selector('div.boxframe.archive > article.boxgrid > a')
            for i in range(len(all_data)):
                line = {}
                line['article_link'] = all_data[i].get_attribute('href')
                line['headline'] = all_data[i].text.split('\n')[1]
                line['posted_at'] = self.get_date(all_data[i].get_attribute('href'))
                line['is_sarcastic'] = 1
                with open('crawled_data/ThePoke.txt','a') as filedata:
                    json.dump(line,filedata)
                    filedata.write('\n')
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(self.delay)
            j += 1

    def close_browser(self):
        self.driver.close()
        print('Done!')

def convert_to_csv(path):
    with open(path,'rb') as f:
        data = f.readlines()
    data = map(lambda x: x.rstrip(),data)
    data_json_string = b'[' + b','.join(data) + b']'
    data_df = pd.read_json(data_json_string)
    print(data_df.head(10))
    data_df.to_csv(path[:-3]+'csv')

def formating_date(path):
    df = pd.read_csv(path)
    print(df.head(10))
    for i in range(len(df)):
        t = df.values[i][3]
        new_date = datetime.strptime(t,"%b %d, %Y").strftime("%d/%m/%Y")
        df.loc[i,'posted_at'] = new_date
    print(df.head(10))
    df.to_csv(path,index=False)
    
    

if __name__ == "__main__":
    # crawl
    sarcasm_crawler = crawler()
    sarcasm_crawler.load_page()
    sarcasm_crawler.close_browser()

    # convert to csv
    # path = 'crawled_data/ThePoke.txt'
    # convert_to_csv(path)

    # formating date
    # path = 'crawled_data\ThePoke.csv'
    # formating_date(path)