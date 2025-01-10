# Complex Python Program #15

```python
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass, field
import random
import logging

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Node:
    """
    A node in a randomized binary tree.

    Args:
        value (int): The value stored in the node.
        left: Left child node.
        right: Right child node.
    """
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

@dataclass
class RandomizedBinaryTree:
    """
    A randomized binary tree that supports efficient search, insertion, and deletion.

    Args:
        root: Root node of the tree.
    """
    root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """
        Inserts a value into the tree.

        Args:
            value (int): The value to insert.
        """
        logging.debug(f"Inserting {value} into the tree.")

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_helper(self.root, value)

    def _insert_helper(self, node: Node, value: int) -> None:
        """
        Recursive helper method for insertion.

        Args:
            node (Node): The current node.
            value (int): The value to insert.
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_helper(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_helper(node.right, value)

    def search(self, value: int) -> Optional[Node]:
        """
        Searches for a value in the tree.

        Args:
            value (int): The value to search for.

        Returns:
            Node or None: The node containing the value, or None if the value is not found.
        """
        logging.debug(f"Searching for {value} in the tree.")

        if self.root is None:
            return None
        else:
            return self._search_helper(self.root, value)

    def _search_helper(self, node: Node, value: int) -> Optional[Node]:
        """
        Recursive helper method for search.

        Args:
            node (Node): The current node.
            value (int): The value to search for.

        Returns:
            Node or None: The node containing the value, or None if the value is not found.
        """
        if node is None:
            return None
        elif node.value == value:
            return node
        elif value < node.value:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)

    def delete(self, value: int) -> None:
        """
        Deletes a value from the tree.

        Args:
            value (int): The value to delete.
        """
        logging.debug(f"Deleting {value} from the tree.")

        if self.root is None:
            return

        # Find the node to delete
        node_to_delete = self._search_helper(self.root, value)
        if node_to_delete is None:
            return

        # Case 1: Node to delete has no children
        if node_to_delete.left is None and node_to_delete.right is None:
            self._delete_helper(node_to_delete)

        # Case 2: Node to delete has one child
        elif node_to_delete.left is None:
            self._delete_helper(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            self._delete_helper(node_to_delete, node_to_delete.left)

        # Case 3: Node to delete has two children
        else:
            # Find the successor of the node to delete
            successor = self._find_successor(node_to_delete)

            # Copy the successor's value to the node to delete
            node_to_delete.value = successor.value

            # Delete the successor
            self._delete_helper(successor)

    def _delete_helper(self, node: Node, child: Optional[Node] = None) -> None:
        """
        Recursive helper method for deletion.

        Args:
            node (Node): The node to delete.
            child (Node, optional): The child of the node to delete. Defaults to None.
        """
        if node.left is None and node.right is None:
            # Node has no children
            if node == self.root:
                self.root = None
            else:
                parent = self._find_parent(node)
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
        else:
            # Node has one child
            if child is not None:
                if node == self.root:
                    self.root = child
                else:
                    parent = self._find_parent(node)
                    if parent.left == node:
                        parent.left = child
                    else:
                        parent.right = child

    def _find_parent(self, node: Node) -> Node:
        """
        Finds the parent of a node in the tree.

        Args:
            node (Node): The node to find the parent of.

        Returns:
            Node: The parent node.
        """
        if node == self.root:
            return None

        parent = self.root
        while parent.left != node and parent.right != node:
            if node.value < parent.value:
                parent = parent.left
            else:
                parent = parent.right

        return parent

    def _find_successor(self, node: Node) -> Node:
        """
        Finds the successor of a node in the tree.

        Args:
            node (Node): The node to find the successor of.

        Returns:
            Node: The successor node.
        """
        successor = node.right
        while successor.left is not None:
            successor = successor.left

        return successor

    def print(self) -> None:
        """
        Prints the tree in a pretty format.
        """
        self._print_helper(self.root, 0)

    def _print_helper(self, node: Optional[Node], level: int) -> None:
        """
        Recursive helper method for printing the tree.

        Args:
            node (Node): The current node.
            level (int): The level of the current node.
        """
        if node is None:
            return

        print(" " * level, node.value)
        self._print_helper(node.left, level + 1)
        self._print_helper(node.right, level + 1)

```