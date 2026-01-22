class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
    
    def insert(self, x):
        
        node = Node(x)
        
        if self.root is None:
            self.root = node
            return
        
        current = self.root
        while True:
            if current.data > x:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right
            
    def search(self,x):
        if self.root is not None:
            current = self.root
            while current is not None:
                if current.data == x:
                    return True
                elif current.data > x:
                    current = current.left
                else:
                    current = current.right
            return False
        return False
    
    def _inorder_helper(self,node,result):
        if node is None:
            return
        self._inorder_helper(node.left,result)
        result.append(node.data)
        self._inorder_helper(node.right,result)
    
    def inorder(self):
        result = []
        self._inorder_helper(self.root,result)
        return result
    def preorder(self):
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        if node is None:
            return
        result.append(node.data)                    # Root first
        self._preorder_helper(node.left, result)    # Then left
        self._preorder_helper(node.right, result)   # Then right
        
    def postorder(self):
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        if node is None:
            return
        self._postorder_helper(node.left, result)   # Left first
        self._postorder_helper(node.right, result)  # Then right
        result.append(node.data) 
