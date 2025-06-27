"""
    Your task is simple, Given a list of numbers
    I want you to do these three things

    1. Add 0 to the beginning of the list
    2. Replace the second element with 20.
    3. Add the number 5 to the end of the list.

"""
def modifyList(numbers):
    return None

# test_functions.py
import unittest

class TestListExercises(unittest.TestCase):
    
    def test_modify_list(self):
        input_list = [1, 2, 3, 4]
        expected_output = [0, 1, 20, 3, 4, 5]
        result = modifyList(input_list.copy())
        self.assertEqual(result, expected_output)