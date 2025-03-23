def reverse(text):
    """
    Odwraca podany tekst

    Args:
        text (str): Tekst do odwrócenia

    Returns:
        str : Odwrócony tekst
    """
    return text[::-1]


def palindrome(text):
    """
    Sprawdza, czy podany tekst jest palindromem.

    Args:
        text (str): Tekst do sprawdzenia.

    Returns:
        bool: True, jeśli tekst jest palindromem, False w przeciwnym wypadku.
    """
    text = text.lower().replace(" ", "")
    return text == text[::-1]


def count_words(text):
    """
    Zlicza słowa w podanym tekście.

    Args:
        text': Tekst do analizy.'

    Returns:
        int: Liczba słów w tekście.
    """

    return len(text.split())


def count_chars(text):
    """
    Zlicza znaki w podanym tekście.

    Args:
        text (str): Tekst do analizy.

    Returns:
        int: Liczba znaków w tekście.
    """
    return len(text)
