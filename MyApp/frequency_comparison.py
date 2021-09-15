import pandas as pd
import matplotlib.pyplot as plt
import requests
# %matplotlib inline
from web_scraping import scraping_webpage
from letters_frequency import letters_frequency, df1

# Task 4 Plooting----------------------------------------------------------

url_2 = input("Enter second url: ")
#url_2 = 'https://de.wikipedia.org/wiki/Angela_Merkel'

page_2 = requests.get(url_2)
secondtext = scraping_webpage(url_2)
# print(secondtext)

lff_2 = letters_frequency(secondtext)
# print(lff_2)

df2 = pd.DataFrame(lff_2.items(), columns=['Letter', 'Frequency Input 2'])
# print(df2)


def data_merging_chart():
    merged_table = pd.merge(df1, df2, on='Letter', how='outer')
    print(merged_table)
    df_reset = merged_table.set_index('Letter')
    df_reset.plot.bar(figsize=(20, 10), title='Frequency Comperebale Plot')


merged_chart = data_merging_chart()
print(merged_chart)
