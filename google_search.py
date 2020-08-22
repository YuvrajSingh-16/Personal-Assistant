import os
import datetime
import smtplib
import webbrowser
import wolframalpha
import random
import pyttsx3
import sys
import wikipedia
import bot
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()
soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

for news in news_list[:15]:
    newsList = news.title.text.split("-")
    print("* According to ", newsList[1], "..", newsList[0], end="\n\n")