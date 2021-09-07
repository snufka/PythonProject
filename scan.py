import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
%matplotlib inline


url= input ("Enter wiki url :")
#url= 'https://de.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart'
page=requests.get(url)

#getting the text and parsing it
soup = BeautifulSoup(page.text, 'html.parser')

#!!!! NEED TO ADD THE NAME!!!
clean_header = [] 
header= soup.find_all(class_='firstHeading')

for item in header:
    clean_header.append(item.text)

review_text=[]
review_text_elem = soup.find_all(class_='mw-body-content mw-content-ltr')

for item in review_text_elem:
    review_text.append(item.text)


#pretty string of thr text
string =' '.join([str(item) for item in review_text]) 

#also needs to be lower case and alphabet only
print(clean_header)

#list of only the letters including german letters
x = re.findall("[A-Za-zÀ-ȕ]", string)

#turn it back to str to count frequency
clean_str= ''.join([str(elem) for elem in x])

#frequency count
freq = {} 
for item in clean_str.lower(): 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1


#sorting dictinory alphabetically
sortedDict = dict( sorted(freq.items(), key=lambda x: x[0].lower()) )

#for k,v in sortedDict.items():
   # print('{}:{}'.format(k,v))
#making a ferquency table
df1=pd.DataFrame(sortedDict.items(),columns=['Letter', 'Frequency 1'])
print(df1)

#TASK 4
print("-----------------------------------task 4-----------------------------------")
url_2= input("second link: ")
page_2=requests.get(url_2)

#getting the text and parsing it
soup_2= BeautifulSoup(page_2.text, 'html.parser')

#!!!! NEED TO ADD THE NAME!!!
clean_header_2 = [] 
header_2= soup_2.find_all(class_='firstHeading')

for item in header_2:
    clean_header_2.append(item.text)

review_text_2=[]
review_text_elem_2 = soup_2.find_all(class_='mw-body-content mw-content-ltr')

for item in review_text_elem_2:
    review_text_2.append(item.text)


#pretty string of thr text
string_2 =' '.join([str(item) for item in review_text_2]) 

#also needs to be lower case and alphabet only
print(clean_header_2)

#list of only the letters including german letters
x_2 = re.findall("[A-Za-zÀ-ȕ]", string_2)

#turn it back to str to count frequency
clean_str_2= ''.join([str(elem) for elem in x_2])

#frequency count
freq_2 = {} 
for item in clean_str_2.lower(): 
    if (item in freq_2): 
        freq_2[item] += 1
    else: 
        freq_2[item] = 1
#print("This is the letters fequency")

#sorting dictinory alphabetically
sortedDict_2 = dict( sorted(freq_2.items(), key=lambda x_2: x_2[0].lower()) )

#for k,v in sortedDict_2.items():
    #print('{}:{}'.format(k,v))
#making a ferquency table
df2=pd.DataFrame(sortedDict_2.items(),columns=['Letter', 'Frequency 2'])
print(df2)

#Merging the table 
merged_table=pd.merge(df1, df2, on='Letter', how='outer')
print(merged_table)
#changing the index to letters
df_reset=merged_table.set_index('Letter')
df_reset.plot()


