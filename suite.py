import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        arr = []
        self.assertTrue(Solution.check_array_sort(arr))
        self.assertTrue(Solution.check_array_set(arr))

    def test_random_order_true(self):
        arr = [4, 5, 15, 2, 8]
        self.assertTrue(Solution.check_array_sort(arr))
        self.assertTrue(Solution.check_array_set(arr))

    def test_random_order_false(self):
        arr = [10, 5, 15, 2, 8]
        self.assertFalse(Solution.check_array_sort(arr))
        self.assertFalse(Solution.check_array_set(arr))

    def test_reverse_order_true(self):
        arr = [9, 7, 5, 3]
        self.assertTrue(Solution.check_array_sort(arr))
        self.assertTrue(Solution.check_array_set(arr))

    def test_reverse_order_false(self):
        arr = [8, 7, 5, 3]
        self.assertFalse(Solution.check_array_sort(arr))
        self.assertFalse(Solution.check_array_set(arr))

    def test_same(self):
        arr = [3, 3, 3, 3]
        self.assertTrue(Solution.check_array_sort(arr))
        self.assertTrue(Solution.check_array_set(arr))

    def test_negative_true(self):
        arr = [-9, 7, -5, 3]
        self.assertTrue(Solution.check_array_sort(arr))
        self.assertTrue(Solution.check_array_set(arr))

    def test_negative_false(self):
        arr = [-8, 7, -5, -3]
        self.assertFalse(Solution.check_array_sort(arr))
        self.assertFalse(Solution.check_array_set(arr))

    def test_repeated_true(self):
        arr = [7, 3, 1, 3]
        self.assertTrue(Solution.check_array_sort(arr))
        self.assertTrue(Solution.check_array_set(arr))

    def test_repeated_false(self):
        arr = [6, 3, 1, 3]
        self.assertFalse(Solution.check_array_sort(arr))
        self.assertFalse(Solution.check_array_set(arr))


if __name__ == '__main__':
    unittest.main()
