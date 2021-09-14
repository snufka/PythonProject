import pytest
from ..text_lan_url import url_lang


def test_for_url_land():
    assert url_lang('https://de.wikipedia.org/wiki/Angela_Merkel') == (
        '*********Based on the URL, this page is in German**************')
