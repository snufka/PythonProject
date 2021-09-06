import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

#url
url= 'https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart'
page=requests.get(url)

#getting the text and parsing it
soup = BeautifulSoup(page.text, 'html.parser')

#!!!! NEED TO ADD THE NAME!!!
review_text=[]
review_text_elem = soup.find_all(class_='mw-body-content mw-content-ltr')

for item in review_text_elem:
    review_text.append(item.text)


#pretty string of thr text
string =' '.join([str(item) for item in review_text]) 

#also needs to be lower case and alphabet only
print(string)
#list of only the letters
x = re.findall("[a-zA-Z]", string)

#turn it back to str to count frequency
clean_str= ''.join([str(elem) for elem in x])

#frequency count
freq = {} 
for item in clean_str.lower(): 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1
print("This is the letters fequency")

#sorting dictinory alphabetically
sortedDict = dict( sorted(freq.items(), key=lambda x: x[0].lower()) )

for k,v in sortedDict.items():
    print('{}:{}'.format(k,v))