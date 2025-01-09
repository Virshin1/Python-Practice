# Complex Python Program #6

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Dict, Any
import logging
import random
import string

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s %(message)s')

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'

class Shape(Enum):
    CIRCLE = 'circle'
    SQUARE = 'square'
    TRIANGLE = 'triangle'

class Toy:
    def __init__(self, name: str, color: Color, shape: Shape):
        self.name = name
        self.color = color
        self.shape = shape

    def __str__(self):
        return f'{self.name} is a {self.color} {self.shape}.'

class ToyBox:
    def __init__(self):
        self.toys: List[Toy] = []

    def add_toy(self, toy: Toy):
        self.toys.append(toy)
    
    def remove_toy(self, toy: Toy):
        self.toys.remove(toy)
    
    def get_toys_by_color(self, color: Color) -> List[Toy]:
        return [toy for toy in self.toys if toy.color == color]
    
    def get_toys_by_shape(self, shape: Shape) -> List[Toy]:
        return [toy for toy in self.toys if toy.shape == shape]

class ToyGenerator:
    def __init__(self):
        self.toy_names = ['Teddy Bear', 'Doll', 'Car', 'Train', 'Airplane']
        self.colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
        self.shapes = [Shape.CIRCLE, Shape.SQUARE, Shape.TRIANGLE]

    def generate_toy(self) -> Toy:
        name = random.choice(self.toy_names)
        color = random.choice(self.colors)
        shape = random.choice(self.shapes)
        return Toy(name, color, shape)

    def generate_toy_box(self, num_toys: int) -> ToyBox:
        toy_box = ToyBox()
        for _ in range(num_toys):
            toy_box.add_toy(self.generate_toy())
        return toy_box

def main():
    try:
        toy_generator = ToyGenerator()
        toy_box = toy_generator.generate_toy_box(10)
        print('Toys in the box:')
        for toy in toy_box.toys:
            print(toy)

        print(f'Red toys: {toy_box.get_toys_by_color(Color.RED)}')
        print(f'Square toys: {toy_box.get_toys_by_shape(Shape.SQUARE)}')
    except Exception as e:
        logging.error('An error occurred', exc_info=e)

if __name__ == '__main__':
    main()
```