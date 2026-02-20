import pygame


def main():
    print("Drawing in Python with PyGame.")

    pygame.init()  # Creates pygame session
    width, height = 1000, 2000

    # make a canvas to draw on
    surface = pygame.Surface((width, height))

    # declare a few colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    purple = (128, 0, 128)

    # paint the canvas black to start
    surface.fill(black)

    # draw a snowperson with nice colors to look better than a plain white snowperson

    draw_snowperson(surface, white, purple, red)

    # save the image and quit pygame to save memory
    pygame.image.save(surface, "snowperson.png")
    pygame.quit()


def draw_snowperson(
    surface: pygame.Surface,
    body_color: tuple[int, int, int],
    object_color: tuple[int, int, int],
    accent_color: tuple[int, int, int],
) -> None:
    """
    Draws a snowperson on the given surface.
    :param surface: The surface to draw on.
    :param body_color: The color of the snowperson's body.
    :param object_color: The color of the snowperson's objects (e.g., buttons).
    :param accent_color: The color of the snowperson's accent (e.g., nose).

    Output: None
    """
    draw_head(surface, body_color, object_color, accent_color)
    draw_body(surface, body_color, object_color, accent_color)
    draw_arms(surface, body_color, object_color, accent_color)
    draw_bottom(surface, body_color, object_color, accent_color)


def draw_head(
    surface: pygame.Surface,
    body_color: tuple[int, int, int],
    object_color: tuple[int, int, int],
    accent_color: tuple[int, int, int],
) -> None:
    """
    Draws the head of the snowperson on the given surface.
    :param surface: The surface to draw on.
    :param body_color: The color of the snowperson's body.
    :param object_color: The color of the snowperson's objects (e.g., buttons).
    :param accent_color: The color of the snowperson's accent (e.g., nose).

    Output: None
    """
    # first paint a big white circle corresponding to the head
    # a circle is defined by its center and radius

    pygame.draw.circle(surface, body_color, (500, 400), 180)

    # add a nose
    pygame.draw.circle(surface, accent_color, (500, 410), 10)

    # add two eyes
    pygame.draw.circle(surface, object_color, (440, 360), 15)
    pygame.draw.circle(surface, object_color, (560, 360), 15)

    # draw the mouth as a rectangle
    # the rectangle is defined by its top left corner, width, and height: top left corner(x, y)
    # and width and height (w, h)
    pygame.draw.rect(surface, accent_color, (450, 450, 100, 20))

    # draw eyebrows as lines
    pygame.draw.line(surface, object_color, (430, 340), (470, 340), 5)
    pygame.draw.line(surface, object_color, (530, 340), (570, 340), 5)


def draw_body(
    surface: pygame.Surface,
    body_color: tuple[int, int, int],
    object_color: tuple[int, int, int],
    accent_color: tuple[int, int, int],
) -> None:
    # paint a big white circle corresponding to the body, centered below the head
    pygame.draw.circle(surface, body_color, (500, 800), 250)
    # add two buttons as small circles of same color
    pygame.draw.circle(surface, object_color, (500, 700), 20)
    pygame.draw.circle(surface, object_color, (500, 800), 20)


def draw_arms(
    surface: pygame.Surface,
    body_color: tuple[int, int, int],
    object_color: tuple[int, int, int],
    accent_color: tuple[int, int, int],
) -> None:
    # draw two lines corresponding to the arms, extending from the body outwards
    pygame.draw.line(surface, object_color, (300, 800), (200, 700), 10)
    pygame.draw.line(surface, object_color, (700, 800), (800, 700), 10)


def draw_bottom(
    surface: pygame.Surface,
    body_color: tuple[int, int, int],
    object_color: tuple[int, int, int],
    accent_color: tuple[int, int, int],
) -> None:
    # paint a big white circle corresponding to the bottom, centered below the body
    pygame.draw.circle(surface, body_color, (500, 1300), 300)

    # add three buttons as small circles
    pygame.draw.circle(surface, object_color, (500, 1100), 20)
    pygame.draw.circle(surface, object_color, (500, 1300), 20)
    pygame.draw.circle(surface, object_color, (500, 1500), 20)


if __name__ == "__main__":
    main()
