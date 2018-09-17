from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

mi_url = "https://www.facebook.com/espol/"

uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

filename = "alertaFacebook.csv"
f = open(filename, "w")
headers = "Tema: \nLink: \n"
f.write(headers)
posts = page_soup.findAll("div", {"class": "_5pbx userContent _3576"})
for post in posts:
    resultado = post.findAll("p")
    tema = resultado[0].text.strip()
    link = post.findAll("a")[0].text
    if tema.find("maestría") != -1 or tema.find("curso") != -1 or tema.find("cursos") != -1 or tema.find("seminario") != -1:
        resultado = "Descripción: " + str(tema) + "\nLink: " + str(link) + "\n"
        print(resultado)
        #f.write(resultado)

f.close()
