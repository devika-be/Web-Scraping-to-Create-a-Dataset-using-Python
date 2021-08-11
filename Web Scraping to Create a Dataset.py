#The datasets that you find on the internet from various data sources are either created by companies and organizations or are collected from websites. You must have scraped data from web pages by using the Python libraries, but may have stuck while preparing the scraped data to create a dataset. 

#How are Datasets Created by Scraping the Web?
#There are so many libraries, frameworks, and tools that are used for the task of web scraping. Some of the most common libraries and modules in Python used for web scraping are:
#1)Scrapy
#2)Selenium
#3)BeautifulSoup
#4)Urlib.request
#All of the above Python libraries and modules are great for scraping data from websites. After scraping the data, the data is prepared so that it can be stored in a CSV file to create a dataset.

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

with open("language.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        writer.writerow(row)
   
  
import pandas as pd
a = pd.read_csv("language.csv")
a.head()