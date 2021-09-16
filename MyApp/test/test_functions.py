import pytest
from text_lan_url import is_lang_german


# def test_for_url_land():

#   assert url_lang('https://de.wikipedia.org/wiki/Angela_Merkel') == (
#       "*********Based on the URL, this page is in German**************")

# ///////////////////////////////////////////
def test_for_germany():
    assert is_lang_german(
        'https://de.wikipedia.org/wiki/Angela_Merkel') == True


def test_for_other_countries():
    assert is_lang_german(
        'https://it.wikipedia.org/wiki/Angela_Merkel') == False
