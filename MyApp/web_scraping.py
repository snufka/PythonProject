#import pandas as pd
import requests
from bs4 import BeautifulSoup
#import re
#import matplotlib.pyplot as plt
# %matplotlib inline

# Task 1-------------------------------------------------------------------------
url = input("Enter wiki url :")
# for easy testing
#url= 'https://de.wikipedia.org/wiki/Pietro_Antonio_Lorenzoni'


def scraping_webpage(url):  # web scraping function

    page = requests.get(url)

# getting the text and parsing it
    soup = BeautifulSoup(page.text, 'html.parser')

# The Wiki page Text
    text = []
    text_body = soup.find_all(class_='mw-body')

    for item in text_body:
        text.append(item.text)

# Clean version of the text
    string = ' '.join([str(item) for item in text])
    return string


my_fun = scraping_webpage(url)
print(my_fun)
