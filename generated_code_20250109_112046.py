# Task: Implement a basic neural network from scratch

```python
import numpy as np

class NeuralNetwork:
    def __init__(self, layers, activation='relu'):
        """
        Args:
            layers: List of integers representing the number of neurons in each layer.
            activation: Activation function to use.
        """
        self.layers = layers
        self.activation = activation
        self.weights = []
        self.biases = []

        # Initialize weights and biases
        for i in range(1, len(layers)):
            self.weights.append(np.random.randn(layers[i-1], layers[i]))
            self.biases.append(np.zeros((1, layers[i])))

    def forward(self, x):
        """
        Args:
            x: Input data.
        Returns:
            Output of the neural network.
        """
        for i in range(len(self.layers) - 1):
            x = np.dot(x, self.weights[i]) + self.biases[i]
            if self.activation == 'relu':
                x = np.maximum(0, x)
            elif self.activation == 'sigmoid':
                x = 1 / (1 + np.exp(-x))
        return x

    def backward(self, x, y, lr=0.01):
        """
        Args:
            x: Input data.
            y: Target output.
            lr: Learning rate.
        """
        # Forward pass
        out = self.forward(x)

        # Calculate the error
        error = y - out

        # Backpropagate the error
        for i in range(len(self.layers) - 1, 0, -1):
            if self.activation == 'relu':
                grad = np.where(out > 0, 1, 0)
            elif self.activation == 'sigmoid':
                grad = out * (1 - out)

            grad = error * grad
            error = np.dot(grad, self.weights[i].T)

            # Update weights and biases
            self.weights[i] -= lr * np.dot(x.T, grad)
            self.biases[i] -= lr * np.sum(grad, axis=0)

    def train(self, x, y, epochs=1000, batch_size=32, lr=0.01):
        """
        Args:
            x: Input data.
            y: Target output.
            epochs: Number of epochs to train for.
            batch_size: Batch size.
            lr: Learning rate.
        """
        for epoch in range(epochs):
            for i in range(0, len(x), batch_size):
                batch_x = x[i:i+batch_size]
                batch_y = y[i:i+batch_size]
                self.backward(batch_x, batch_y, lr)

    def predict(self, x):
        """
        Args:
            x: Input data.
        Returns:
            Predicted output.
        """
        return self.forward(x)
```