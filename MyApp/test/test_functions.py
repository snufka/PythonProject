from text_lan_url import is_lang_german


def test_for_germany():
    assert is_lang_german(
        'https://de.wikipedia.org/wiki/Angela_Merkel') == True


def test_for_other_countries():
    assert is_lang_german(
        'https://it.wikipedia.org/wiki/Angela_Merkel') == False


if __name__ == "__main__":
    test_for_germany()
    test_for_other_countries()
    print("Tests passed")
