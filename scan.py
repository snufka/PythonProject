import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
%matplotlib inline


#url= input ("Enter wiki url :")
url= 'https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart'
page=requests.get(url)

#getting the text and parsing it
soup = BeautifulSoup(page.text, 'html.parser')

#The Wiki page Text
review_text=[]
text_body = soup.find_all(class_='mw-body')

for item in text_body:
    review_text.append(item.text)


#Clean version of the text
string =' '.join([str(item) for item in review_text]) 
#print(string)

#list of only the letters, including german letters
x = re.findall("[A-Za-zÀ-ȕ]", string)

#turn it back to str to count frequency
clean_str= ''.join([str(elem) for elem in x])
#TASK 3
#frequency count
freq = {} 
for item in clean_str.lower(): 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1


#sorting dictinory alphabetically
sortedDict = dict( sorted(freq.items(), key=lambda x: x[0].lower()) )

# Task 2
#count of letters sum
values_char = sortedDict.values()
total_char= sum(values_char)
#print("Total number of letter in the text: {}".format(total_char))

#Counting German Letters and counting the percentage of the letter in the text
germna_letters= ['ä', 'ö', 'ü', 'ß']
german_char_dict = {k:sortedDict[k] for k in germna_letters if k in sortedDict}
values_german_char = german_char_dict.values()
total_german_char= sum(values_german_char)
print("Total number of German letter in the text: {}".format(total_german_char))
# Calculation of the % of the German latters of the text
percentage_of_german_char=  (total_german_char/total_char)*100
print("percentage of greman letter in the text: {}".format(percentage_of_german_char))

#Probablity that the text is in German
if percentage_of_german_char >= 0.465:
    print( "We are 100% sure that this text is in German! The frequency of special German characters is 0.465% or higher!")
elif percentage_of_german_char < 0.465 and percentage_of_german_char >= 0.348:
    print("The chance that this text is in German is very high 100% - 75%! The frequency of special German characters is {}%".format(percentage_of_german_char))
elif percentage_of_german_char < 0.348 and percentage_of_german_char >= 0.2325:
    print("We are 75% - 50% sure that this text is in German! The frequency of special German characters is {}%".format(percentage_of_german_char))
elif percentage_of_german_char < 0.2325 and percentage_of_german_char >= 0.116:
    print("We are 50% - 25% sure that this text is in German! The frequency of special German characters is {}%".format(percentage_of_german_char))
else: 
    print( "Not German! There is less than 25% that this text is in German! The frequency of special German characters is {}%".format(percentage_of_german_char))


#making a ferquency table
df1=pd.DataFrame(sortedDict.items(),columns=['Letter', 'Frequency 1'])
#print(df1)
df_reset=df1.set_index('Letter')

df_reset.plot.bar()

#TASK 4--------------------------------------------------------------------------------------------

#url_2= input("second link: ")
url_2='https://de.wikipedia.org/wiki/Angela_Merkel'
page_2=requests.get(url_2)

#getting the text and parsing it
soup_2= BeautifulSoup(page_2.text, 'html.parser')

#The text
review_text_2=[]
text_body_2 = soup_2.find_all(class_='mw-body')

for item in text_body_2:
    review_text_2.append(item.text)


#pretty string of thr text
string_2 =' '.join([str(item) for item in review_text_2]) 


#list of only the letters including german letters
x_2 = re.findall("[A-Za-zÀ-ȕ]", string_2)

#turn it back to str to count frequency
clean_str_2= ''.join([str(elem) for elem in x_2])
#TASK 3
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

#count of letters sum
values_char_2 = sortedDict_2.values()

total_char_2 = sum(values_char_2)

#print("Total number of letter in 2nd text: {}".format(total_char_2))


#making a ferquency table
df2=pd.DataFrame(sortedDict_2.items(),columns=['Letter', 'Frequency 2'])
#print(df2)

#Merging the table 
merged_table=pd.merge(df1, df2, on='Letter', how='outer')
#print(merged_table)
#changing the index to letters
df_reset=merged_table.set_index('Letter')
df_reset.plot.bar()
