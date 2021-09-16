import pytest
from ..text_lan_url import url_lang

url = ''


def lang_in_url(url):
    split = url.split(".")

# Checking Language by subDomain;
    if split[0].find("de") == -1:
        print("*********Based on the URL, this page is not in German**************")
    else:
        print("*********Based on the URL, this page is in German*****************")


def test_for_url_land():
    assert url_lang('https://de.wikipedia.org/wiki/Angela_Merkel') == (
        "*********Based on the URL, this page is in German**************")
