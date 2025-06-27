"""
    For this lessons I want you to iterate over a list
    of numbers (temperatures) and return the highest temperature in the list
    AND the lowest temperature in the list

    Remeber in the last lesson you are able to return multiple values in a 
    function.
"""
def find_max_min(temperatures):
    return None

# test_functions.py
import unittest

class TestListExercises(unittest.TestCase):
    def test_find_max_min(self):
        temps = [72, 68, 75, 70, 74]
        expected_max = 75
        expected_min = 68
        max_temp, min_temp = find_max_min(temps)
        self.assertEqual(max_temp, expected_max)
        self.assertEqual(min_temp, expected_min)

    def test_find_max_min_single_element(self):
        temps = [42]
        self.assertEqual(find_max_min(temps), (42, 42))

    def test_find_max_min_all_equal(self):
        temps = [50, 50, 50]
        self.assertEqual(find_max_min(temps), (50, 50))

    def test_find_max_min_negative_values(self):
        temps = [-10, -20, -5, -30]
        self.assertEqual(find_max_min(temps), (-5, -30))

    def test_find_max_min_mixed_signs(self):
        temps = [-15, 0, 20, -5, 10]
        self.assertEqual(find_max_min(temps), (20, -15))