import unittest
import sys
sys.path.append('..')
from data_structures.binary_search_tree import BST


class TestBSTInsertAndSearch(unittest.TestCase):
    
    def setUp(self):
        self.bst = BST()
    
    # Test empty tree
    def test_search_empty_tree(self):
        self.assertFalse(self.bst.search(10))
    
    # Test insert and search single element
    def test_insert_and_search_single(self):
        self.bst.insert(10)
        self.assertTrue(self.bst.search(10))
    
    def test_search_not_found(self):
        self.bst.insert(10)
        self.assertFalse(self.bst.search(99))
    
    # Test multiple inserts
    def test_insert_multiple(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertTrue(self.bst.search(10))
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(15))
    
    # Test BST property (left < root < right)
    def test_bst_property(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.root.data, 10)
        self.assertEqual(self.bst.root.left.data, 5)
        self.assertEqual(self.bst.root.right.data, 15)
    
    def test_deep_tree(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(20)
        self.assertTrue(self.bst.search(3))
        self.assertTrue(self.bst.search(7))
        self.assertTrue(self.bst.search(20))
        self.assertFalse(self.bst.search(100))


class TestBSTTraversals(unittest.TestCase):
    
    def setUp(self):
        self.bst = BST()
        #       10
        #      /  \
        #     5    15
        #    / \
        #   3   7
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(3)
        self.bst.insert(7)
    
    # Test inorder (should be sorted)
    def test_inorder(self):
        self.assertEqual(self.bst.inorder(), [3, 5, 7, 10, 15])
    
    # Test preorder (root first)
    def test_preorder(self):
        self.assertEqual(self.bst.preorder(), [10, 5, 3, 7, 15])
    
    # Test postorder (root last)
    def test_postorder(self):
        self.assertEqual(self.bst.postorder(), [3, 7, 5, 15, 10])
    
    # Test empty tree traversals
    def test_inorder_empty(self):
        empty_bst = BST()
        self.assertEqual(empty_bst.inorder(), [])
    
    def test_preorder_empty(self):
        empty_bst = BST()
        self.assertEqual(empty_bst.preorder(), [])
    
    def test_postorder_empty(self):
        empty_bst = BST()
        self.assertEqual(empty_bst.postorder(), [])
    
    # Test single node traversals
    def test_inorder_single(self):
        single_bst = BST()
        single_bst.insert(42)
        self.assertEqual(single_bst.inorder(), [42])
    
    def test_preorder_single(self):
        single_bst = BST()
        single_bst.insert(42)
        self.assertEqual(single_bst.preorder(), [42])
    
    def test_postorder_single(self):
        single_bst = BST()
        single_bst.insert(42)
        self.assertEqual(single_bst.postorder(), [42])


class TestBSTInorderSorted(unittest.TestCase):
    
    def test_inorder_always_sorted(self):
        bst = BST()
        # Insert in random order
        for val in [50, 30, 70, 20, 40, 60, 80]:
            bst.insert(val)
        # Inorder should be sorted
        self.assertEqual(bst.inorder(), [20, 30, 40, 50, 60, 70, 80])
    
    def test_inorder_with_duplicates(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(10)  # Duplicate goes right
        result = bst.inorder()
        self.assertEqual(result, [5, 10, 10])


if __name__ == '__main__':
    unittest.main()