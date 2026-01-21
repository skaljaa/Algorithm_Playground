import unittest
import sys
sys.path.append('..')
from algorithms import linear_search, binary_search


class TestLinearSearch(unittest.TestCase):
    
    def test_element_at_beginning(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 1), 0)
    
    def test_element_at_end(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 5), 4)
    
    def test_element_in_middle(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
    
    def test_element_not_found(self):
        with self.assertRaises(IndexError):
            linear_search([1, 2, 3, 4, 5], 99)
    
    def test_empty_array(self):
        with self.assertRaises(IndexError):
            linear_search([], 1)
    
    def test_single_element_found(self):
        self.assertEqual(linear_search([42], 42), 0)
    
    def test_single_element_not_found(self):
        with self.assertRaises(IndexError):
            linear_search([42], 99)
    
    def test_duplicate_returns_first(self):
        self.assertEqual(linear_search([1, 2, 2, 2, 3], 2), 1)
    
    def test_negative_numbers(self):
        self.assertEqual(linear_search([-5, -3, 0, 2, 4], -3), 1)


class TestBinarySearch(unittest.TestCase):
    
    def test_element_at_beginning(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
    
    def test_element_at_end(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)
    
    def test_element_in_middle(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
    
    def test_element_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 99), -1)
    
    def test_element_not_found_too_small(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], -5), -1)
    
    def test_empty_array(self):
        self.assertEqual(binary_search([], 1), -1)
    
    def test_single_element_found(self):
        self.assertEqual(binary_search([42], 42), 0)
    
    def test_single_element_not_found(self):
        self.assertEqual(binary_search([42], 99), -1)
    
    def test_two_elements_find_first(self):
        self.assertEqual(binary_search([1, 2], 1), 0)
    
    def test_two_elements_find_second(self):
        self.assertEqual(binary_search([1, 2], 2), 1)
    
    def test_negative_numbers(self):
        self.assertEqual(binary_search([-5, -3, 0, 2, 4], -3), 1)
    
    def test_large_array(self):
        arr = list(range(0, 1000, 2))  # [0, 2, 4, ..., 998]
        self.assertEqual(binary_search(arr, 500), 250)
        self.assertEqual(binary_search(arr, 501), -1)


if __name__ == '__main__':
    unittest.main()