import unittest
import sys
sys.path.append('..')
from data_structures.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.list = SinglyLinkedList()
    
    # Helper to convert list to array for easier testing
    def to_array(self):
        result = []
        current = self.list.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    # Test insert_beginning
    def test_insert_beginning_empty_list(self):
        self.list.insert_beginning(10)
        self.assertEqual(self.to_array(), [10])
    
    def test_insert_beginning_multiple(self):
        self.list.insert_beginning(30)
        self.list.insert_beginning(20)
        self.list.insert_beginning(10)
        self.assertEqual(self.to_array(), [10, 20, 30])
    
    # Test insert_end
    def test_insert_end_empty_list(self):
        self.list.insert_end(10)
        self.assertEqual(self.to_array(), [10])
    
    def test_insert_end_multiple(self):  # sourcery skip: class-extract-method
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.assertEqual(self.to_array(), [10, 20, 30])
    
    # Test delete
    def test_delete_head(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.list.delete(10)
        self.assertEqual(self.to_array(), [20, 30])
    
    def test_delete_tail(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.list.delete(30)
        self.assertEqual(self.to_array(), [10, 20])
    
    def test_delete_middle(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.list.delete(20)
        self.assertEqual(self.to_array(), [10, 30])
    
    def test_delete_only_element(self):
        self.list.insert_end(10)
        self.list.delete(10)
        self.assertEqual(self.to_array(), [])
    
    def test_delete_empty_list_raises_error(self):
        with self.assertRaises(IndexError):
            self.list.delete(10)
    
    def test_delete_nonexistent_raises_error(self):
        self.list.insert_end(10)
        with self.assertRaises(IndexError):
            self.list.delete(99)
    
    # Test search
    def test_search_found(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.assertTrue(self.list.search(20))
    
    def test_search_not_found_raises_error(self):
        self.list.insert_end(10)
        with self.assertRaises(IndexError):
            self.list.search(99)
    
    def test_search_empty_list_raises_error(self):
        with self.assertRaises(IndexError):
            self.list.search(10)


if __name__ == '__main__':
    unittest.main()