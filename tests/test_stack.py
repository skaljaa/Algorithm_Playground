import unittest
import sys
sys.path.append('..')
from data_structures.stack import Stack


class TestStack(unittest.TestCase):
    
    def setUp(self):
        """Create a fresh stack for each test"""
        self.stack = Stack()
    
    # Test is_empty
    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())
    
    def test_stack_with_items_is_not_empty(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
    
    # Test push
    def test_push_single_item(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
    
    def test_push_multiple_items(self):  # sourcery skip: class-extract-method
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.peek(), 30)
    
    # Test pop
    def test_pop_returns_last_item(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
    
    def test_pop_removes_item(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 10)
    
    def test_pop_empty_stack_raises_error(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
    
    # Test peek
    def test_peek_returns_top_without_removing(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.peek()
        self.assertEqual(self.stack.peek(), 20)
    
    def test_peek_empty_stack_raises_error(self):
        with self.assertRaises(IndexError):
            self.stack.peek()
    
    # Test LIFO behavior
    def test_lifo_order(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)


if __name__ == '__main__':
    unittest.main()