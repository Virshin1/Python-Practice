# Complex Python Program #25

```python
import logging
import random
import time

class Shape:
    def __init__(self, name: str, vertices: int) -> None:
        self.name = name
        self.vertices = vertices

    def __repr__(self) -> str:
        return f'{self.name} ({self.vertices} vertices)'

class Prism(Shape):
    def __init__(self, name: str, vertices: int, height: float) -> None:
        super().__init__(name, vertices)
        self.height = height

    def volume(self) -> float:
        """Calculates the volume of the prism."""
        return (self.vertices / 4) * self.height ** 2

class Pyramid(Shape):
    def __init__(self, name: str, vertices: int, base_length: float) -> None:
        super().__init__(name, vertices)
        self.base_length = base_length

    def volume(self) -> float:
        """Calculates the volume of the pyramid."""
        return (self.vertices / 3) * self.base_length ** 3

class ShapeGenerator:
    def __init__(self, max_vertices: int = 10, max_height: float = 10.0, max_base_length: float = 10.0) -> None:
        self.max_vertices = max_vertices
        self.max_height = max_height
        self.max_base_length = max_base_length

    def generate(self) -> Shape:
        """Randomly generates and returns a shape."""
        shape_type = random.choice([Prism, Pyramid])
        shape = shape_type(
            f'{shape_type.__name__}#{random.randint(1, 100)}',
            random.randint(3, self.max_vertices),
            random.random() * self.max_height if isinstance(shape, Prism) else random.random() * self.max_base_length
        )
        return shape


def main():
    logging.basicConfig(level=logging.INFO)

    generator = ShapeGenerator()

    shapes = []
    try:
        for _ in range(10):
            shapes.append(generator.generate())
    except ValueError as e:
        logging.error(f'Invalid shape parameters: {e}')
        return

    total_volume = sum(shape.volume() for shape in shapes)
    logging.info(f'Total volume of all shapes: {total_volume:.2f}')

    print('Shapes:')
    for shape in shapes:
        print(f' - {shape}')

if __name__ == '__main__':
    main()
```