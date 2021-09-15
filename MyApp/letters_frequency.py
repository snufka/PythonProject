import pandas as pd
import re
import matplotlib.pyplot as plt
# %matplotlib inline
from web_scraping import my_fun

# TASK 3-------------------------------------------------------------------------
# list of only the letters, including german letters


def letters_frequency(my_fun):
    x = re.findall("[A-Za-zÀ-ȕ]", my_fun)

# turn it back to str to count frequency
    clean_str = ''.join([str(elem) for elem in x])

# frequency count
    freq = {}
    for item in clean_str.lower():
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

# sorting dictinory alphabetically
    sortedDict = dict(sorted(freq.items(), key=lambda x: x[0].lower()))
    return sortedDict


lff = letters_frequency(my_fun)

# the frequency table
df1 = pd.DataFrame(lff.items(), columns=['Letter', 'Frequency Input 1'])
print(df1)

# The chart
df_reset = df1.set_index('Letter')
df_reset.plot.bar(figsize=(20, 10), title='Letters Frequency Distribution')
