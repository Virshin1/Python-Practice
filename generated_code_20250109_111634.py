# Task: Implement a binary search tree class with insert and search methods

```python
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
    else:
      self._insert(value, self.root)

  def _insert(self, value, curr_node):
    if value < curr_node.value:
      if curr_node.left is None:
        curr_node.left = Node(value)
      else:
        self._insert(value, curr_node.left)
    elif value > curr_node.value:
      if curr_node.right is None:
        curr_node.right = Node(value)
      else:
        self._insert(value, curr_node.right)
    else:
      print("Value already exists in the tree.")

  def search(self, value):
    if self.root is None:
      return False
    else:
      return self._search(value, self.root)

  def _search(self, value, curr_node):
    if value == curr_node.value:
      return True
    elif value < curr_node.value:
      if curr_node.left is None:
        return False
      else:
        return self._search(value, curr_node.left)
    else:
      if curr_node.right is None:
        return False
      else:
        return self._search(value, curr_node.right)
```