# Complex Python Program #1

```python
import random
import string
import time
import logging

class Node:
    """
    A single node in the network.

    Attributes:
        id: A unique identifier for the node.
        connections: A list of connections to other nodes.
        messages: A list of messages received by the node.
    """

    def __init__(self, id: int):
        self.id = id
        self.connections = []
        self.messages = []

    def add_connection(self, other_node: "Node"):
        """
        Adds a connection to another node.

        Args:
            other_node: The node to connect to.
        """

        self.connections.append(other_node)

    def send_message(self, message: str):
        """
        Sends a message to all connected nodes.

        Args:
            message: The message to send.
        """

        for node in self.connections:
            node.messages.append(message)

class Network:
    """
    A collection of nodes connected together.

    Attributes:
        nodes: A list of nodes in the network.
    """

    def __init__(self, nodes: list[Node]):
        self.nodes = nodes

    def broadcast_message(self, message: str):
        """
        Broadcasts a message to all nodes in the network.

        Args:
            message: The message to broadcast.
        """

        for node in self.nodes:
            node.messages.append(message)

class MessageGenerator:
    """
    A generator of random messages.

    Attributes:
        alphabet: The alphabet to use when generating messages.
        message_length: The length of messages to generate.
    """

    def __init__(self, alphabet: str, message_length: int):
        self.alphabet = alphabet
        self.message_length = message_length

    def generate_message(self) -> str:
        """
        Generates a random message.

        Returns:
            A random message.
        """

        return "".join(random.choices(self.alphabet, k=self.message_length))

def main():
    """
    The main function.
    """

    # Create a logger
    logger = logging.getLogger(__name__)

    # Create a network
    network = Network([Node(i) for i in range(10)])

    # Create a message generator
    message_generator = MessageGenerator(string.ascii_letters, 10)

    # Generate and broadcast messages
    for _ in range(10):
        try:
            message = message_generator.generate_message()
            network.broadcast_message(message)
        except Exception as e:
            logger.error(f"Error generating and broadcasting message: {e}")

    # Print the messages received by each node
    for node in network.nodes:
        print(f"Node {node.id} received the following messages: {node.messages}")

if __name__ == "__main__":
    main()
```