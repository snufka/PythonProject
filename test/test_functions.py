import pytest
from '../MyApp/text_lan_url.py' import lang_in_url
  
def test_for_url_land():
  assert lang_in_url('https://de.wikipedia.org/wiki/Angela_Merkel')==('*********Based on the URL, this page is in German**************')