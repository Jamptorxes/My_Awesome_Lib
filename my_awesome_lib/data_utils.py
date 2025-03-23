def load_csv(path):
    """
    Wczytuje dane z pliku CSV i zwraca listę słowników.

    Args:
        path (str): Ścieżka do pliku CSV.

    Returns:
        list: Lista słowników, gdzie każdy słownik reprezentuje wiersz z pliku CSV.

    Raises:
        FileNotFoundError: Jeśli plik nie istnieje.
    """
    import csv

    with open(path, "r") as file:
        return list(csv.DictReader(file))


def save_csv(data, path):
    """
    Zapisuje dane do pliku CSV.

    Args:
        data (list): Lista słowników do zapisania.
        path (str): Ścieżka do pliku CSV.

    Raises:
        ValueError: Jeśli `data` jest pusta lub niepoprawna.
    """
    import csv

    with open(path, mode="w", newline="") as file:
        if not data:
            raise ValueError("Data is empty")

        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def load_json(path):
    """
    Wczytuje dane z pliku JSON i zwraca je jako słownik.

    Args:
        path (str): Ścieżka do pliku JSON.

    Returns:
        dict: Dane z pliku JSON.

    Raises:
        FileNotFoundError: Jeśli plik nie istnieje.
    """
    import json

    with open(path, "r") as file:
        return json.load(file)


def save_json(data, path):
    """
    Zapisuje dane do pliku JSON.

    Args:
        data (dict): Dane do zapisania.
        path (str): Ścieżka do pliku JSON

    Raises:
        ValueError: Jeśli `data` jest puste lub niepoprawne
    """
    import json

    with open(path, mode="w", newline="") as file:
        json.dump(data, file)
