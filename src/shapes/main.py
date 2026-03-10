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

    def __init__(
        self,
        width: float = 0.0,
        height: float = 0.0,
        x1: float = 0.0,
        y1: float = 0.0,
        rotation: float = 0.0,
    ) -> None:
        # self.name = name
        self.width = width
        self.height = height
        self.x1 = x1
        self.y1 = y1
        self.rotation = rotation


class Circle:
    """A class to represent a circle in a 2D plane.
    Attributes:
        radius (float): The radius of the circle.
        x1 (float): The x-coordinate of the circle's center.
        y1 (float): The y-coordinate of the circle's center.
    """

    def __init__(self, radius: float = 0.0, x1: float = 0.0, y1: float = 0.0) -> None:
        self.radius = radius
        self.x1 = x1
        self.y1 = y1


def main():
    print("Shapes and Classes in Python.")

    my_circle = Circle(radius=2.0, x1=1.0, y1=3.0)
    print(f"Circle: radius={my_circle.radius}, center=({my_circle.x1}, {my_circle.y1})")

    r = Rectangle(width=3.0, height=5.0)  # other attributes will take default values
    print(f"Rectangle: width={r.width}, height={r.height}")


if __name__ == "__main__":
    main()
