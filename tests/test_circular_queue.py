import unittest
import sys
sys.path.append('..')
from data_structures.circular_queue import CircularQueue


class TestCircularQueue(unittest.TestCase):
    
    def setUp(self):
        self.queue = CircularQueue(5)
    
    # Test is_empty
    def test_new_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())
    
    def test_queue_with_items_is_not_empty(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
    
    # Test is_full
    def test_new_queue_is_not_full(self):
        self.assertFalse(self.queue.is_full())
    
    def test_full_queue(self):
        for i in range(5):
            self.queue.enqueue(i)
        self.assertTrue(self.queue.is_full())
    
    # Test enqueue
    def test_enqueue_single_item(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 10)
    
    def test_enqueue_full_queue_raises_error(self):
        for i in range(5):
            self.queue.enqueue(i)
        with self.assertRaises(IndexError):
            self.queue.enqueue(99)
    
    # Test dequeue
    def test_dequeue_returns_first_item(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.dequeue(), 10)
    
    def test_dequeue_empty_queue_raises_error(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()
    
    def test_dequeue_single_item_makes_empty(self):
        self.queue.enqueue(10)
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())
    
    # Test peek
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
    
    # Test wrap-around behavior
    def test_wrap_around(self):
        # Fill queue
        for i in range(5):
            self.queue.enqueue(i)
        # Remove some
        self.queue.dequeue()
        self.queue.dequeue()
        # Add more (should wrap)
        self.queue.enqueue(10)
        self.queue.enqueue(11)
        # Check FIFO still works
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 11)
    
    def test_wrap_around_full_detection(self):
        # sourcery skip: extract-duplicate-method
        # Fill, remove some, fill again to capacity
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.enqueue(7)
        self.assertTrue(self.queue.is_full())


if __name__ == '__main__':
    unittest.main()