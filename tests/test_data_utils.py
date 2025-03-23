import unittest
from my_awesome_lib.data_utils import *
import csv
import json
import os


class TestDataUtils(unittest.TestCase):
    def setUp(self):
        # Tworzenie tymczasowego pliku CSV do testów
        self.test_file = "test_data.csv"
        self.test_data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
        with open(self.test_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "age"])
            writer.writeheader()
            writer.writerows(self.test_data)

        self.test_json_file = "test_data.json"
        self.test_json_data = {"name": "Alice", "age": 30}
        with open(self.test_json_file, mode="w") as file:
            json.dump(self.test_json_data, file)

    def tearDown(self):
        # Usuwanie tymczasowych plików
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_json_file):
            os.remove(self.test_json_file)
        if os.path.exists("output.csv"):
            os.remove("output.csv")
        if os.path.exists("output.json"):
            os.remove("output.json")

    def test_load_csv(self):
        data = load_csv(self.test_file)
        self.assertEqual(data, self.test_data)

    def test_load_csv_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_csv("dupa.csv")

    def test_save_csv(self):
        output_file = "output.csv"
        save_csv(self.test_data, output_file)

        # Sprawdzenie czy plik został zapisany
        with open(output_file, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        self.assertEqual(data, self.test_data)

    def test_load_json(self):
        data = load_json(self.test_json_file)
        self.assertEqual(data, self.test_json_data)

    def test_load_json_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_json("dupa.json")

    def test_save_json(self):
        output_file = "output.json"
        save_json(self.test_json_data, output_file)

        # Sprawdzenie czy plik został zapisany
        with open(output_file, "r") as file:
            data = json.load(file)
        self.assertEqual(data, self.test_json_data)


if __name__ == "__main__":
    unittest.main()
