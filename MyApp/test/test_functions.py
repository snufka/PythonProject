import pytest
#from ..text_lan_url import url_lang
url = ''


def lang_in_url(url):
    split = url.split(".")

# Checking Language by subDomain;
    if split[0].find("en") == -1:
        print("*********Based on the URL, this page is in German**************")
  # elif (split[0].includes("en"))
   #     print("it's not english nor German, to find out more please visit https://en.wikipedia.org/wiki/List_of_Wikipedias#List")
    else:
        print("*********Based on the URL, this page is in English*****************")


def test_for_url_land():
    assert lang_in_url('https://de.wikipedia.org/wiki/Angela_Merkel') == (
        "*********Based on the URL, this page is in German**************")
