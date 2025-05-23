import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import unittest
from entrypoint import book_seat, get_manifest  # Replace with actual filename

class TestFlightBooking(unittest.TestCase):
    def setUp(self):
        self.passengers = []

    def test_valid_seat_booking(self):
        result = book_seat(self.passengers, "Alice", 3)
        self.assertEqual(result, "Seat 3 assigned to Alice")
        self.assertEqual(len(self.passengers), 1)

    def test_duplicate_seat_booking(self):
        book_seat(self.passengers, "Bob", 2)
        result = book_seat(self.passengers, "Charlie", 2)
        self.assertEqual(result, "Seat 2 is already taken.")
        self.assertEqual(len(self.passengers), 1)

    def test_invalid_seat_number_high(self):
        result = book_seat(self.passengers, "Dave", 15)
        self.assertEqual(result, "Seat number must be between 1 and 10.")

    def test_invalid_seat_number_low(self):
        result = book_seat(self.passengers, "Eve", 0)
        self.assertEqual(result, "Seat number must be between 1 and 10.")

    def test_manifest_order(self):
        book_seat(self.passengers, "Frank", 5)
        book_seat(self.passengers, "Grace", 2)
        manifest = get_manifest(self.passengers)
        self.assertEqual(manifest[0]['seat'], 2)
        self.assertEqual(manifest[1]['seat'], 5)

if __name__ == '__main__':
    unittest.main()
