# Complex Python Program #9

```python
import random
import logging
from typing import List, Dict, Union

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Node:
    def __init__(self, value: int, left: 'Node'=None, right: 'Node'=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, current: 'Node') -> None:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(value, current.left)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(value, current.right)

    def find(self, value: int) -> Node:
        if self.root is None:
            return None

        current: Node = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def delete(self, value: int) -> None:
        if self.root is None:
            return

        parent: Node = None
        current: Node = self.root
        while current is not None and value != current.value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            successor: Node = self._find_successor(current)
            current.value = successor.value
            if successor.right is not None:
                successor.right = self._remove_node(successor.right, successor.value)
            else:
                self._remove_node(successor.left, successor.value)

    def _find_successor(self, node: 'Node') -> 'Node':
        current: Node = node.right
        while current.left is not None:
            current = current.left
        return current

    def _remove_node(self, node: 'Node', value: int) -> Node:
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove_node(node.left, value)
        elif value > node.value:
            node.right = self._remove_node(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor: Node = self._find_successor(node)
                node.value = successor.value
                node.right = self._remove_node(node.right, successor.value)
        return node

    def is_balanced(self) -> bool:
        if self.root is None:
            return True

        heights: Dict[Node, int] = {}
        return self._is_balanced(self.root, heights)

    def _is_balanced(self, node: 'Node', heights: Dict[Node, int]) -> bool:
        if node is None:
            return 0

        left_height = self._is_balanced(node.left, heights)
        if left_height == -1:
            return -1

        right_height = self._is_balanced(node.right, heights)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        heights[node] = max(left_height, right_height) + 1
        return heights[node]

    def __str__(self) -> str:
        def _inorder(node: 'Node') -> List[int]:
            if node is None:
                return []
            return _inorder(node.left) + [node.value] + _inorder(node.right)

        return ' '.join(map(str, _inorder(self.root)))

class RandomTreeGenerator:
    def __init__(self, size: int, max_value: int):
        self.size = size
        self.max_value = max_value

    def generate(self) -> BinarySearchTree:
        tree = BinarySearchTree()
        for _ in range(self.size):
            value = random.randint(1, self.max_value)
            tree.insert(value)
        return tree

if __name__ == '__main__':
    size = 10
    max_value = 100
    generator = RandomTreeGenerator(size, max_value)
    tree = generator.generate()
    logging.info(f'Generated random tree: {tree}')
```