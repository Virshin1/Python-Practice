# Complex Python Program #4

```python
import random
import logging
from dataclasses import dataclass
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: 'Point') -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

@dataclass
class Rectangle:
    top_left: Point
    bottom_right: Point

    def contains(self, point: Point) -> bool:
        return self.top_left.x <= point.x <= self.bottom_right.x and self.top_left.y <= point.y <= self.bottom_right.y

@dataclass
class Circle:
    center: Point
    radius: float

    def contains(self, point: Point) -> bool:
        return self.center.distance_to(point) <= self.radius

def generate_random_points(n: int) -> List[Point]:
    """
    Generates a list of n random points within a unit square.

    Args:
        n: The number of points to generate.

    Returns:
        A list of n random points.
    """
    points = []
    for _ in range(n):
        point = Point(random.random(), random.random())
        points.append(point)
    return points

def generate_random_rectangles(n: int) -> List[Rectangle]:
    """
    Generates a list of n random rectangles within a unit square.

    Args:
        n: The number of rectangles to generate.

    Returns:
        A list of n random rectangles.
    """
    rectangles = []
    for _ in range(n):
        top_left = Point(random.random(), random.random())
        bottom_right = Point(random.random(), random.random())
        rectangle = Rectangle(top_left, bottom_right)
        rectangles.append(rectangle)
    return rectangles

def generate_random_circles(n: int) -> List[Circle]:
    """
    Generates a list of n random circles within a unit square.

    Args:
        n: The number of circles to generate.

    Returns:
        A list of n random circles.
    """
    circles = []
    for _ in range(n):
        center = Point(random.random(), random.random())
        radius = random.random()
        circle = Circle(center, radius)
        circles.append(circle)
    return circles

def count_points_in_shapes(points: List[Point], shapes: List[Rectangle] + List[Circle]) -> Tuple[int, int]:
    """
    Counts the number of points that are contained within the given shapes.

    Args:
        points: The list of points to check.
        shapes: The list of shapes to check against.

    Returns:
        A tuple containing the number of points contained within rectangles and the number of points contained within circles.
    """
    num_points_in_rectangles = 0
    num_points_in_circles = 0
    for point in points:
        for shape in shapes:
            if isinstance(shape, Rectangle):
                if shape.contains(point):
                    num_points_in_rectangles += 1
            elif isinstance(shape, Circle):
                if shape.contains(point):
                    num_points_in_circles += 1
    return num_points_in_rectangles, num_points_in_circles

if __name__ == "__main__":
    try:
        n_points = int(input("Enter the number of points to generate: "))
        n_rectangles = int(input("Enter the number of rectangles to generate: "))
        n_circles = int(input("Enter the number of circles to generate: "))
    except ValueError:
        logging.error("Invalid input. Please enter a valid integer.")
        exit(1)

    points = generate_random_points(n_points)
    rectangles = generate_random_rectangles(n_rectangles)
    circles = generate_random_circles(n_circles)

    num_points_in_rectangles, num_points_in_circles = count_points_in_shapes(points, rectangles + circles)

    logging.info(f"{num_points_in_rectangles} points are contained within rectangles.")
    logging.info(f"{num_points_in_circles} points are contained within circles.")
```