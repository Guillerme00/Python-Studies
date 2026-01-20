import unittest
from bubble_sort import bubble

class bubble_test(unittest.TestCase):
    def test_bubble(self):

        # For bubble sort studies, I hard coded a unsorted list and a sorted list,
        # I did it to test the algorithm
        unsorted_list = [1,5,4,12,123,23,5123,523,44]
        sorted_list = [1,4,5,12,23,44,123,523,5123]

        unsorted_list = bubble(unsorted_list)
        self.assertEqual(unsorted_list, sorted_list)


if __name__ == "__main__":
    unittest.main()