import unittest
import sys
sys.path.append('..')
from data_structures.queue import Queue


class TestQueue(unittest.TestCase):
    
    def setUp(self):
        self.queue = Queue()
    
    # Test is_empty
    def test_new_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())
    
    def test_queue_with_items_is_not_empty(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
    
    # Test enqueue
    def test_enqueue_single_item(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 10)
    
    def test_enqueue_multiple_items(self):  # sourcery skip: class-extract-method
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.peek(), 10)
    
    # Test dequeue
    def test_dequeue_returns_first_item(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.dequeue(), 10)
    
    def test_dequeue_removes_item(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 20)
    
    def test_dequeue_empty_queue_raises_error(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()
    
    # Test peek
    def test_peek_returns_front_without_removing(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.peek()
        self.assertEqual(self.queue.peek(), 10)
    
    def test_peek_empty_queue_raises_error(self):
        with self.assertRaises(IndexError):
            self.queue.peek()
    
    # Test FIFO behavior
    def test_fifo_order(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)


if __name__ == '__main__':
    unittest.main()