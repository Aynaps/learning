import unittest

def peaksAndValleys(nums: list[int]):
    """
        I want you to write a function given a list
        of integers nums, return a list of indexes where
        index i is a 'peak'. A peak is denoted where at 
        a given index i, its neighbors are smaller

        Example:
            nums -> [1,3,2]
            output -> [3]
    """
    #code goes beneath this line
    

#dont worry about this
class TestPeaksAndValleys(unittest.TestCase):

    def test_single_peak(self):
        self.assertEqual(peaksAndValleys([1, 3, 2]), [3])

    def test_multiple_peaks(self):
        self.assertEqual(peaksAndValleys([1, 3, 2, 5, 4, 6, 3]), [3, 5, 6])

    def test_no_peaks(self):
        self.assertEqual(peaksAndValleys([1, 2, 3, 4, 5]), [])

    def test_decreasing_list(self):
        self.assertEqual(peaksAndValleys([5, 4, 3, 2, 1]), [])

    def test_flat_list(self):
        self.assertEqual(peaksAndValleys([2, 2, 2, 2, 2]), [])

    def test_tiny_list(self):
        self.assertEqual(peaksAndValleys([1]), [])
        self.assertEqual(peaksAndValleys([1, 2]), [])

    def test_peak_with_negative_numbers(self):
        self.assertEqual(peaksAndValleys([-3, -1, -4]), [-1])

    def test_peak_at_end_or_start_ignored(self):
        self.assertEqual(peaksAndValleys([9, 7, 8]), [])  # 7 < 9 but no right neighbor for 9
        self.assertEqual(peaksAndValleys([8, 9, 7]), [9])  # 9 is a valid peak

if __name__ == "__main__":
    unittest.main()