"""
    This one given a list of grades
    calculate the sum and average and return those values.

    I have already scaffolded it out so you dont need to worry about
    returning just iterate through the list and calculate the sum and average

"""

def sum_and_average(grades):
    total = 0
    avg = 0

    #Your code goes beneath this line

    return total, avg #dont change this


# test_functions.py
import unittest

class TestListExercises(unittest.TestCase):
    

    def test_sum_and_average(self):
        grades = [80, 90, 70, 100]
        expected_sum = 340
        expected_avg = 85.0
        result_sum, result_avg = sum_and_average(grades)
        self.assertEqual(result_sum, expected_sum)
        self.assertAlmostEqual(result_avg, expected_avg)

    def test_sum_and_average_empty_list(self):
        grades = []
        self.assertEqual(sum_and_average(grades), (0, 0))

    def test_sum_and_average_single_element(self):
        grades = [100]
        self.assertEqual(sum_and_average(grades), (100, 100.0))

    def test_sum_and_average_all_zeros(self):
        grades = [0, 0, 0]
        self.assertEqual(sum_and_average(grades), (0, 0.0))

if __name__ == '__main__':
    unittest.main()
