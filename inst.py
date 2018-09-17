import json
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

mi_url = "https://www.instagram.com/espol1/"

uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
'''
browser = webdriver.Firefox()
browser.get(mi_url)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = 0
while match < 5:
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match += 1


body = browser.find_element_by_tag_name('body')
for _ in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

time.sleep(3)
source_data = browser.page_source
page = soup(source_data, "html.parser")
'''
#filename = "alertaInstagram.csv"
#f = open(filename, "w")
#headers = "Tema: \nLink: \n"
#f.write(headers)
#posts = page_soup.findAll("body")


script_tag = page_soup.find('script', text=re.compile('window\._sharedData'))
shared_data = script_tag.string.partition('=')[-1].strip(' ;')
result = json.loads(shared_data)
n = len(result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'])
for i in range(1,n):
    resultado = "Descripcion: " +result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges'][0]['node']['text'] + "\nLink: https://www.instagram.com/p/" + result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['shortcode']+"\n"
    print(resultado)




#f.close()
