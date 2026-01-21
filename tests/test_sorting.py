import unittest
import sys
sys.path.append('..')
from algorithms.mergesort import merge_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quicksort import quicksort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort


class TestBubbleSort(unittest.TestCase):
    
    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(bubble_sort([1]), [1])
    
    def test_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_random_order(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([3, -1, 4, -5, 0]), [-5, -1, 0, 3, 4])
    
    def test_two_elements(self):
        self.assertEqual(bubble_sort([2, 1]), [1, 2])


class TestSelectionSort(unittest.TestCase):
    
    def test_empty_array(self):
        self.assertEqual(selection_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(selection_sort([1]), [1])
    
    def test_already_sorted(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_random_order(self):
        self.assertEqual(selection_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        self.assertEqual(selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        self.assertEqual(selection_sort([3, -1, 4, -5, 0]), [-5, -1, 0, 3, 4])


class TestInsertionSort(unittest.TestCase):
    
    def test_empty_array(self):
        self.assertEqual(insertion_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(insertion_sort([1]), [1])
    
    def test_already_sorted(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_random_order(self):
        self.assertEqual(insertion_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        self.assertEqual(insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        self.assertEqual(insertion_sort([3, -1, 4, -5, 0]), [-5, -1, 0, 3, 4])


class TestMergeSort(unittest.TestCase):
    
    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])
    
    def test_already_sorted(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_random_order(self):
        self.assertEqual(merge_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        self.assertEqual(merge_sort([3, -1, 4, -5, 0]), [-5, -1, 0, 3, 4])


class TestQuickSort(unittest.TestCase):
    
    def test_empty_array(self):
        arr = []
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])
    
    def test_single_element(self):
        arr = [1]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])
    
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_random_order(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        arr = [3, -1, 4, -5, 0]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [-5, -1, 0, 3, 4])
    
    def test_two_elements(self):
        arr = [2, 1]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2])


if __name__ == '__main__':
    unittest.main()