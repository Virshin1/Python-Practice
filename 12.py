# Complex Python Program #12

```python
import logging
import random
import string
import time

# Configure logging
logging.basicConfig(filename='unique_program.log', level=logging.DEBUG)

class Node:
    """
    Node class for a custom data structure.

    Attributes:
        value: The value stored in the node.
        next: The next node in the linked list.
    """

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node

class CustomList:
    """
    Custom linked list implementation with additional functionality.

    Attributes:
        head: The head node of the linked list.
    """

    def __init__(self):
        self.head = None

    def insert_beginning(self, value: int):
        """
        Inserts a node with the given value at the beginning of the linked list.

        Args:
            value: The value to store in the new node.
        """

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove_last(self):
        """
        Removes and returns the last node from the linked list.

        Returns:
            The value of the removed node, or None if the linked list is empty.
        """

        if self.head is None:
            return None

        current_node = self.head
        previous_node = None

        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next

        if previous_node is not None:
            previous_node.next = None
        else:
            self.head = None

        return current_node.value

    def reverse(self):
        """
        Reverses the order of the nodes in the linked list.
        """

        current_node = self.head
        previous_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

class ShuffleGenerator:
    """
    Generator that yields a random permutation of the given string.

    Attributes:
        string: The string to generate permutations of.
    """

    def __init__(self, string: str):
        self.string = string
        self.remaining_characters = list(string)

    def __iter__(self):
        while self.remaining_characters:
            index = random.randint(0, len(self.remaining_characters) - 1)
            yield self.remaining_characters.pop(index)

def generate_random_string(length: int) -> str:
    """
    Generates a random string of the given length.

    Args:
        length: The length of the string to generate.

    Returns:
        A random string of the given length.
    """

    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def main():
    # Generate a random 10-character string
    random_string = generate_random_string(10)
    logging.info(f'Generated random string: {random_string}')

    # Create a custom linked list and insert the random string into it
    custom_list = CustomList()
    for character in random_string:
        custom_list.insert_beginning(ord(character))

    # Reverse the linked list
    custom_list.reverse()

    # Create a shuffle generator for the reversed string
    shuffle_generator = ShuffleGenerator(random_string)

    # Print the shuffled string
    shuffled_string = ''.join(shuffle_generator)
    logging.info(f'Shuffled random string: {shuffled_string}')

    # Remove the last node from the linked list and print its value
    last_node_value = custom_list.remove_last()
    logging.info(f'Value of the removed last node: {last_node_value}')

if __name__ == '__main__':
    main()
```