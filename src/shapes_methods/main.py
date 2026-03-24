from dataclasses import dataclass, field
import math


@dataclass
class Rectangle:
    """
    A class to represent a 2Drectangle in a plane.
    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        x1 (float): The x-coordinate of the rectangle's corner.
        y1 (float): The y-coordinate of the rectangle's corner.
        rotation (float): The rotation angle of the rectangle in degrees.
    """

    width: float = field(default=0.0)
    height: float = field(default=0.0)
    x1: float = field(default=0.0)
    y1: float = field(default=0.0)
    rotation: float = field(default=0.0)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def main():
    print("Methods and returning to shapes.")

    rect = Rectangle(width=3.0, height=5.0)  # other attributes will take default values
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")


if __name__ == "__main__":
    main()
