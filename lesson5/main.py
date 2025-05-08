import unittest

def count_freq(list1):
    """
        Given a generic list
        return a dictionary of the frequencies of each
        unique element.

        Example:
            nums -> [1,1,2,2,2,3]
            output -> {1: 2, 2: 3, 3: 1}
        Example 2:
            chars -> ['a', 'a', 'b']
            output 0> {a: 2, b: 1}
    """


class TestCountFreq(unittest.TestCase):

    def test_basic_strings(self):
        self.assertEqual(count_freq(['a', 'b', 'a', 'c', 'b', 'a']),
                         {'a': 3, 'b': 2, 'c': 1})

    def test_basic_integers(self):
        self.assertEqual(count_freq([1, 2, 1, 3, 2, 1]),
                         {1: 3, 2: 2, 3: 1})

    def test_empty_list(self):
        self.assertEqual(count_freq([]), {})

    def test_single_element(self):
        self.assertEqual(count_freq(['x']), {'x': 1})

    def test_all_unique(self):
        self.assertEqual(count_freq([1, 2, 3, 4]), {1: 1, 2: 1, 3: 1, 4: 1})

    def test_case_sensitivity(self):
        self.assertEqual(count_freq(['A', 'a', 'A']), {'A': 2, 'a': 1})



if __name__ == "__main__":
    unittest.main()