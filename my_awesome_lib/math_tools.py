def add(a, b):
    """
    Zwraca sumę dwóch liczb

    Args:
        a (int, float): Pierwsza liczba
        b (int, float): Druga liczba

    Returns:
        int, float: Suma liczb a i b
    """
    return a + b


def silnia(n):
    """
    Oblicza silnię liczby n.

    Args:
        n (int): Liczba całkowita.

    Returns:
        int: Silnia liczby n.

    Raises:
        ValueError: Jeśli n jest ujemne.
    """
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną")
    return n * silnia(n - 1)


def fibonacci(n):
    """
    Zwraca n-tą liczbę Fibonacciego.

    Args:
        n (int): Numer liczby Fibonacciego.

    Returns:
        int: n-ta liczba Fibonacciego

    Raises:
        ValueError: Jeśli n jest ujemne.
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną")
    return fibonacci(n - 1) + fibonacci(n - 2)


def pierwsza(n):
    """
    Sprawdza, czy liczba jest liczbą pierwszą.

    Args:
        n (int): Liczba całkowita.

    Returns:
        bool: True jeśli liczba jest pierwsza, False w przeciwnym wypadku.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
