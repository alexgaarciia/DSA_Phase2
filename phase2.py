# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and then remove
        this node (using super()._remove). After this, the function has to balance the node returned by the function
        super()._remove """
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def balance(self, node):
        """This is a function that, given an element, returns the heigth balance factor of its node"""
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)

    def left_rotation(self, node):
        # Nodes are reorganized.
        a = node.right
        b = a.left
        a.left = node
        node.right = b

        # New heigths need to be computed, since the tree has changed.
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        a.height = 1 + max(self._height(a.left), self._height(a.right))
        return a

    def right_rotation(self, node):
        # Nodes are reorganized
        a = node.left
        b = a.right
        a.right = node
        node.left = b

        # New heights need to be computed, since the tree has changed.
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        a.height = 1 + max(self._height(a.left), self._height(a.right))
        return a

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        # Step 1: Get the balance of the node to check if it is in the range -1, 0, 1 or out of that range.
        balance = self.balance(node)

        # Step 2: Evaluate the balance.
        # IF THE NODE IS UNBALANCED, DEPENDING ON THE CASE, 4 DIFFERENT ACTIONS CAN BE PERFORMED: LEFT ROTATION,
        # RIGHT ROTATION, LEFT-RIGHT ROTATION AND RIGHT-LEFT ROTATION.

        # Case 1 - Left rotation.
        if balance < -1 and self.balance(node.right) <= 0:
            return self.left_rotation(node)

        # Case 2: Right rotation.
        if balance > 1 and self.balance(node.left) >= 0:
            return self.right_rotation(node)

        # Case 3 - Left-Right rotation.
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)

        # Case 4 - Right-left rotation.
        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)

        return node

        # Note: it can be observed that, in some cases, for example, there is balance < -1 or balance > 1, and the main
        # reason of this is because in the balance function from above, there is no absolute value.
