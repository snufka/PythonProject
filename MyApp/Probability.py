import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
#import web_scraping as ws
from letters_frequency import lff
# Task 5 & 6--------------------------------------------------------------------


def probability_german_text():
    # count of letters sum
    values_char = lff.values()
    total_char = sum(values_char)
#print("Total number of letters in the text: {}".format(total_char))

# Counting German Letters and counting the percentage of the letter in the text
    germna_letters = ['ä', 'ö', 'ü', 'ß']
    german_char_dict = {k: lff[k] for k in germna_letters if k in lff}

    values_german_char = german_char_dict.values()
    total_german_char = sum(values_german_char)
    print(total_char)
    print("Total number of German letter in the text: {}".format(total_german_char))

# Calculation of the % of the German latters of the text
    percentage_of_german_char = (total_german_char*100)/total_char
    round_percentage_of_german_char = round(percentage_of_german_char, 2)

    print("percentage of greman letter in the text: {}".format(
        round_percentage_of_german_char))

    #mean = (0.456/100)*total_char
    #sd= (0.114/100)*total_char
    #z= (total_german_char - mean)/sd
    #probability= 1-z
    #print('z', z, 'mean',mean,'sd',sd ,'prob',probability)

# Probablity that the text is in German----------
    if percentage_of_german_char >= 0.91:
        print("We are 100% sure that this text is in German! The frequency of special German characters is {}%!".format(
            round_percentage_of_german_char))

    elif percentage_of_german_char > 0.79 and percentage_of_german_char < 0.91:
        print("The probability that this text is in German is 99.9%! The frequency of special German characters is {}%".format(
            round_percentage_of_german_char))

    elif percentage_of_german_char > 0.68 and percentage_of_german_char <= 0.79:
        print("The probability that this text is in German is 97.7%- 99.8%! The frequency of special German characters is {}%".format(round_percentage_of_german_char))

    elif percentage_of_german_char > 0.58 and percentage_of_german_char <= 0.68:
        print("The probability that this text is in German is 84.1% - 97.7%! The frequency of special German characters is {}%".format(round_percentage_of_german_char))

    elif percentage_of_german_char >= 0.46 and percentage_of_german_char <= 0.57:
        print("The probability that this text is in German is 84.1% - 50.1%! The frequency of special German characters is {}%".format(round_percentage_of_german_char))

    elif percentage_of_german_char < 0.46 and percentage_of_german_char >= 0.34:
        print("The probability that this text is in German is 15.8% - 50%! The frequency of special German characters is {}%".format(round_percentage_of_german_char))

    elif percentage_of_german_char < 0.34 and percentage_of_german_char >= 0.23:
        print("We are 97.7% - 84.2% sure that this text is not German! The frequency of special German characters is {}%".format(round_percentage_of_german_char))

    elif percentage_of_german_char < 0.23 and percentage_of_german_char >= 0.11:
        print("We are 99.8% - 97.8% sure that this text is not German! The frequency of special German characters is {}%".format(round_percentage_of_german_char))

    else:
        print("Not German! There is less than 0.1% that this text is in German! The frequency of special German characters is {}%".format(
            round_percentage_of_german_char))


probability_german_text()
prob = probability_german_text()
print(prob)
