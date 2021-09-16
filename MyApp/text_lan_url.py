from web_scraping import url
#from url_test import url


# Task 2--Detecting the language based on the URL--------------------------------
def lang_in_url(url):
    split = url.split(".")

# Checking Language by subDomain;
    if split[0].find("de") == -1:
        print("*********Based on the URL, this page is not in German**************")
    else:
        print("*********Based on the URL, this page is in German*****************")


url_lang = lang_in_url(url)
