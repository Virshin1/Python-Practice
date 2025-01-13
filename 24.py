# Complex Python Program #24

```python
import random
import logging
import typing

logging.basicConfig(level=logging.DEBUG, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                    return
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = Node(value)
                    return
                else:
                    current = current.right

    def search(self, value: int) -> typing.Optional[Node]:
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, value: int):
        node = self.search(value)
        if not node:
            logging.warning(f'Node with value {value} not found')
            return

        if not node.left and not node.right:
            self._delete_node(node)
            return

        if not node.left:
            self._transplant_node(node, node.right)
            return

        if not node.right:
            self._transplant_node(node, node.left)
            return

        successor = self._get_successor(node)
        logging.debug(f'Successor of node {node.value} is {successor.value}')
        node.value = successor.value
        self._delete_node(successor)

    def _get_successor(self, node: Node) -> Node:
        current = node.right
        while current.left:
            current = current.left
        return current

    def _transplant_node(self, node_to_delete: Node, new_node: Node):
        if not node_to_delete.parent:
            self.root = new_node
        elif node_to_delete == node_to_delete.parent.left:
            node_to_delete.parent.left = new_node
        else:
            node_to_delete.parent.right = new_node
        new_node.parent = node_to_delete.parent

    def _delete_node(self, node: Node):
        if not node.parent:
            self.root = None
        elif node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None

if __name__ == '__main__':
    bst = BinarySearchTree()
    values = [random.randint(0, 100) for _ in range(10)]
    for value in values:
        bst.insert(value)
    print('Inserted values:', values)
    value_to_search = random.choice(values)
    found_node = bst.search(value_to_search)
    if found_node:
        print(f'Found node with value {found_node.value}')
    value_to_delete = random.choice(values)
    bst.delete(value_to_delete)
    print(f'Deleted node with value {value_to_delete}')
    print('In-order traversal:', [node.value for node in bst.inorder_traversal()])
```