# Complex Python Program #15

```python
from dataclasses import dataclass
from typing import List, Tuple
import os
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Define data classes
@dataclass
class Point:
    x: int
    y: int

@dataclass
class LineSegment:
    start: Point
    end: Point

@dataclass
class Rectangle:
    width: int
    height: int

# Define custom exception
class RectangleIntersectionError(Exception):
    pass

# Define classes
class PointGenerator:
    """Generates random points within a given range."""

    def __init__(self, min_x: int, max_x: int, min_y: int, max_y: int):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def generate(self, num_points: int) -> List[Point]:
        """Generates a list of random points within the specified range."""

        points = []
        for _ in range(num_points):
            x = random.randint(self.min_x, self.max_x)
            y = random.randint(self.min_y, self.max_y)
            points.append(Point(x, y))
        return points

class LineSegmentGenerator:
    """Generates random line segments within a given range."""

    def __init__(self, min_x: int, max_x: int, min_y: int, max_y: int):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def generate(self, num_segments: int) -> List[LineSegment]:
        """Generates a list of random line segments within the specified range."""

        segments = []
        for _ in range(num_segments):
            start_x = random.randint(self.min_x, self.max_x)
            start_y = random.randint(self.min_y, self.max_y)
            end_x = random.randint(self.min_x, self.max_x)
            end_y = random.randint(self.min_y, self.max_y)
            segments.append(LineSegment(Point(start_x, start_y), Point(end_x, end_y)))
        return segments

class RectangleGenerator:
    """Generates random rectangles within a given range."""

    def __init__(self, min_width: int, max_width: int, min_height: int, max_height: int):
        self.min_width = min_width
        self.max_width = max_width
        self.min_height = min_height
        self.max_height = max_height

    def generate(self, num_rectangles: int) -> List[Rectangle]:
        """Generates a list of random rectangles within the specified range."""

        rectangles = []
        for _ in range(num_rectangles):
            width = random.randint(self.min_width, self.max_width)
            height = random.randint(self.min_height, self.max_height)
            rectangles.append(Rectangle(width, height))
        return rectangles

# Define functions
def check_rectangle_intersection(rect1: Rectangle, rect2: Rectangle) -> bool:
    """Checks if two rectangles intersect."""

    # Check if the rectangles overlap on the x-axis
    if rect1.x + rect1.width < rect2.x or rect2.x + rect2.width < rect1.x:
        return False

    # Check if the rectangles overlap on the y-axis
    if rect1.y + rect1.height < rect2.y or rect2.y + rect2.height < rect1.y:
        return False

    return True

# Define main function
def main():
    """Generates random points, line segments, and rectangles and checks for intersections."""

    # Generate random points, line segments, and rectangles
    point_generator = PointGenerator(-100, 100, -100, 100)
    line_segment_generator = LineSegmentGenerator(-100, 100, -100, 100)
    rectangle_generator = RectangleGenerator(10, 50, 10, 50)

    num_points = 100
    num_line_segments = 50
    num_rectangles = 25

    points = point_generator.generate(num_points)
    line_segments = line_segment_generator.generate(num_line_segments)
    rectangles = rectangle_generator.generate(num_rectangles)

    # Check for intersections between points and line segments
    for point in points:
        for line_segment in line_segments:
            if point.x >= line_segment.start.x and point.x <= line_segment.end.x:
                if point.y >= line_segment.start.y and point.y <= line_segment.end.y:
                    logging.info(f"Point ({point.x}, {point.y}) intersects with line segment ({line_segment.start.x}, {line_segment.start.y}) -> ({line_segment.end.x}, {line_segment.end.y})")

    # Check for intersections between line segments
    for line_segment1 in line_segments:
        for line_segment2 in line_segments:
            if line_segment1 is line_segment2:
                continue

            if check_rectangle_intersection(Rectangle(line_segment1.start.x, line_segment1.start.y, line_segment1.end.x - line_segment1.start.x, line_segment1.end.y - line_segment1.start.y),
                                            Rectangle(line_segment2.start.x, line_segment2.start.y, line_segment2.end.x - line_segment2.start.x, line_segment2.end.y - line_segment2.start.y)):
                logging.info(f"Line segment ({line_segment1.start.x}, {line_segment1.start.y}) -> ({line_segment1.end.x}, {line_segment1.end.y}) intersects with line segment ({line_segment2.start.x}, {line_segment2.start.y}) -> ({line_segment2.end.x}, {line_segment2.end.y})")

    # Check for intersections between rectangles
    for rectangle1 in rectangles:
        for rectangle2 in rectangles:
            if rectangle1 is rectangle2:
                continue

            try:
                if check_rectangle_intersection(rectangle1, rectangle2):
                    logging.info(f"Rectangle ({rectangle1.x}, {rectangle1.y}, {rectangle1.width}, {rectangle1.height}) intersects with rectangle ({rectangle2.x}, {rectangle2.y}, {rectangle2.width}, {rectangle2.height})")
            except RectangleIntersectionError as e:
                logging.error(f"Error checking intersection between rectangles: {e}")

# Run main function
if __name__ == "__main__":
    main()
```