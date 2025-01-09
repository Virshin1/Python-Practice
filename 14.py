# Complex Python Program #14

```python
import random
import logging
from typing import List, Tuple, Dict, Optional

# Configure logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class Node:
    """
    A node in a binary tree.

    Attributes:
        value: The value stored in the node.
        left: The left child node.
        right: The right child node.
    """

    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    A binary tree data structure.

    Attributes:
        root: The root node of the tree.
    """

    def __init__(self, root: Optional[Node] = None) -> None:
        self.root = root

    def insert(self, value: int) -> None:
        """
        Inserts a new node with the given value into the tree.

        Args:
            value: The value to insert.
        """

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, node: Node) -> None:
        """
        Inserts a new node with the given value into the tree, starting at the given node.

        Args:
            value: The value to insert.
            node: The node to start at.
        """

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def find(self, value: int) -> Optional[Node]:
        """
        Finds the node with the given value in the tree.

        Args:
            value: The value to search for.

        Returns:
            The node with the given value, or None if the value is not found.
        """

        if self.root is None:
            return None

        return self._find(value, self.root)

    def _find(self, value: int, node: Node) -> Optional[Node]:
        """
        Finds the node with the given value in the tree, starting at the given node.

        Args:
            value: The value to search for.
            node: The node to start at.

        Returns:
            The node with the given value, or None if the value is not found.
        """

        if node is None:
            return None

        if value == node.value:
            return node
        elif value < node.value:
            return self._find(value, node.left)
        else:
            return self._find(value, node.right)

    def delete(self, value: int) -> None:
        """
        Deletes the node with the given value from the tree.

        Args:
            value: The value to delete.
        """

        if self.root is None:
            return

        try:
            self._delete(value, self.root)
        except ValueError:
            logging.error(f"Node with value {value} not found")

    def _delete(self, value: int, node: Node) -> None:
        """
        Deletes the node with the given value from the tree, starting at the given node.

        Args:
            value: The value to delete.
            node: The node to start at.
        """

        if node is None:
            raise ValueError

        if value == node.value:
            # Node to delete has no children
            if node.left is None and node.right is None:
                if node == self.root:
                    self.root = None
                elif node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None

            # Node to delete has one child
            elif node.left is None:
                if node == self.root:
                    self.root = node.right
                elif node == node.parent.left:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

            elif node.right is None:
                if node == self.root:
                    self.root = node.left
                elif node == node.parent.left:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

            # Node to delete has two children
            else:
                # Find the smallest node in the right subtree
                successor = self._find_min(node.right)

                # Copy the value of the successor into the node to delete
                node.value = successor.value

                # Delete the successor
                self._delete(successor.value, successor)

        elif value < node.value:
            self._delete(value, node.left)
        else:
            self._delete(value, node.right)

    def _find_min(self, node: Node) -> Node:
        """
        Finds the smallest node in the tree, starting at the given node.

        Args:
            node: The node to start at.

        Returns:
            The smallest node in the tree.
        """

        while node.left is not None:
            node = node.left

        return node

    def print_preorder(self) -> None:
        """
        Prints the tree in preorder traversal order.
        """

        if self.root is not None:
            self._print_preorder(self.root)

    def _print_preorder(self, node: Node) -> None:
        """
        Prints the tree in preorder traversal order, starting at the given node.

        Args:
            node: The node to start at.
        """

        print(node.value)
        if node.left is not None:
            self._print_preorder(node.left)
        if node.right is not None:
            self._print_preorder(node.right)

    def print_inorder(self) -> None:
        """
        Prints the tree in inorder traversal order.
        """

        if self.root is not None:
            self._print_inorder(self.root)

    def _print_inorder(self, node: Node) -> None:
        """
        Prints the tree in inorder traversal order, starting at the given node.

        Args:
            node: The node to start at.
        """

        if node.left is not None:
            self._print_inorder(node.left)
        print(node.value)
        if node.right is not None:
            self._print_inorder(node.right)

    def print_postorder(self) -> None:
        """
        Prints the tree in postorder traversal order.
        """

        if self.root is not None:
            self._print_postorder(self.root)

    def _print_postorder(self, node: Node) -> None:
        """
        Prints the tree in postorder traversal order, starting at the given node.

        Args:
            node: The node to start at.
        """

        if node.left is not None:
            self._print_postorder(node.left)
        if node.right is not None:
            self._print_postorder(node.right)
        print(node.value)

    def is_balanced(self) -> bool:
        """
        Checks if the tree is balanced.

        A tree is balanced if the height of the left and right subtrees of any node differ by at most 1.

        Returns:
            True if the tree is balanced, False otherwise.
        """

        if self.root is None:
            return True

        return self._is_balanced(self.root)

    def _is_balanced(self, node: Node) -> bool:
        """
        Checks if the tree is balanced, starting at the given node.

        Args:
            node: The node to start at.

        Returns:
            True if the tree is balanced, False otherwise.
        """

        if node.left is None and node.right is None:
            return True

        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)

        return abs(left_height - right_height) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right)

    def _get_height(self, node: Optional[Node]) -> int