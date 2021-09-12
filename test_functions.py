#Testing
import pytest

def test_for_url_land():
  assert lang_in_url('https://de.wikipedia.org/wiki/Angela_Merkel')==('*********Based on the URL, this page is in German**************')
  
