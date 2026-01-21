import unittest
import sys
sys.path.append('..')
from data_structures.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.list = DoublyLinkedList()
    
    # Helper to convert to array (forward)
    def to_array_forward(self):
        result = []
        current = self.list.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    # Helper to convert to array (backward)
    def to_array_backward(self):
        if self.list.head is None:
            return []
        current = self.list.head
        while current.next is not None:
            current = current.next
        result = []
        while current is not None:
            result.append(current.data)
            current = current.prev
        return result
    
    # Test insert_beginning
    def test_insert_beginning_empty_list(self):
        self.list.insert_beginning(10)
        self.assertEqual(self.to_array_forward(), [10])
    
    def test_insert_beginning_multiple(self):
        self.list.insert_beginning(30)
        self.list.insert_beginning(20)
        self.list.insert_beginning(10)
        self.assertEqual(self.to_array_forward(), [10, 20, 30])
    
    # Test insert_end
    def test_insert_end_empty_list(self):
        self.list.insert_end(10)
        self.assertEqual(self.to_array_forward(), [10])
    
    def test_insert_end_multiple(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.assertEqual(self.to_array_forward(), [10, 20, 30])
    
    # Test bidirectional links
    def test_forward_and_backward_match(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        forward = self.to_array_forward()
        backward = self.to_array_backward()
        self.assertEqual(forward, list(reversed(backward)))
    
    # Test delete
    def test_delete_head(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.list.delete(10)
        self.assertEqual(self.to_array_forward(), [20, 30])
        self.assertEqual(self.list.head.prev, None)
    
    def test_delete_tail(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.list.delete(30)
        self.assertEqual(self.to_array_forward(), [10, 20])
    
    def test_delete_middle(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.list.delete(20)
        self.assertEqual(self.to_array_forward(), [10, 30])
    
    def test_delete_middle_preserves_links(self):
        self.list.insert_end(10)
        self.list.insert_end(20)
        self.list.insert_end(30)
        self.list.delete(20)
        # Check forward and backward still work
        self.assertEqual(self.to_array_forward(), [10, 30])
        self.assertEqual(self.to_array_backward(), [30, 10])
    
    def test_delete_only_element(self):
        self.list.insert_end(10)
        self.list.delete(10)
        self.assertEqual(self.to_array_forward(), [])
    
    def test_delete_nonexistent_raises_error(self):
        self.list.insert_end(10)
        with self.assertRaises(IndexError):
            self.list.delete(99)


if __name__ == '__main__':
    unittest.main()