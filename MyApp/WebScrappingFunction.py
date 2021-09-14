import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
%matplotlib inline

#Task 1-------------------------------------------------------------------------
#url= input ("Enter wiki url :")
#for easy testing
url= 'https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart'

def scraping_webpage(): #web scraping function

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
    return string

my_fun = scraping_webpage()


#TASK 3-------------------------------------------------------------------------
#list of only the letters, including german letters
def letters_frequency():
     x = re.findall("[A-Za-zÀ-ȕ]", my_fun)

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
     return sortedDict

lff=letters_frequency()

#the frequency table
df1=pd.DataFrame(lff.items(),columns=['Letter', 'Frequency Input 1'])
print(df1)

#The chart
df_reset=df1.set_index('Letter')
df_reset.plot.bar(figsize=(20,10),title='Letters Frequency Distribution')

# Task 2-----------------------------------------------------------------------
def is_the_text_in_german():
#count of letters sum
   values_char = lff.values()
   total_char= sum(values_char)
#print("Total number of letters in the text: {}".format(total_char))

#Counting German Letters and counting the percentage of the letter in the text
   germna_letters= ['ä', 'ö', 'ü', 'ß']
   german_char_dict = {k:lff[k] for k in germna_letters if k in lff}

   values_german_char = german_char_dict.values()
   total_german_char= sum(values_german_char)

   print("Total number of German letter in the text: {}".format(total_german_char))

# Calculation of the % of the German latters of the text
   percentage_of_german_char= (total_german_char/total_char)*100

   print("percentage of greman letter in the text: {}".format(percentage_of_german_char))

#Probablity that the text is in German----------
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

text_lang= is_the_text_in_german()

