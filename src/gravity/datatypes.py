from dataclasses import dataclass, field  # field used in Body


@dataclass
class OrderedPair:
    """
    Represents a 2D vector or coordinate pair (x, y).
    """
    x: float = 0.0
    y: float = 0.0


@dataclass
class Body:
    """
    Represents a celestial body within the simulation universe.
    """
    name: str = "Unnamed"
    mass: float = 1.0
    radius: float = 1.0
    position: OrderedPair = field(default_factory=OrderedPair)
    velocity: OrderedPair = field(default_factory=OrderedPair)
    acceleration: OrderedPair = field(default_factory=OrderedPair)
    red: int = 255
    green: int = 255
    blue: int = 255


@dataclass
class Universe:
    """
    Represents the entire simulation environment.
    """
    bodies: list[Body] = field(default_factory=list)
    width: float = 1000.0
    gravitational_constant: float = 6.674e-11
