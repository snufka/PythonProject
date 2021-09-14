from web_scraping import url
#from url_test import url


def lang_in_url(url):
    split = url.split(".")

# Checking Language by subDomain;
    if split[0].find("en") == -1:
        print("*********Based on the URL, this page is in German**************")
  # elif (split[0].includes("en"))
   #     print("it's not english nor German, to find out more please visit https://en.wikipedia.org/wiki/List_of_Wikipedias#List")
    else:
        print("*********Based on the URL, this page is in English*****************")


url_lang = lang_in_url(url)
