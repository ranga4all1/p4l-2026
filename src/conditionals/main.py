def main():
    print("Conditionals in Python.")

    print("Minimum of 3 and 4 is:", min_2(3, 4))
    print("Minimum of 4 and 3 is:", min_2(4, 3))

    print("Which is greater between 3 and 5:", which_is_greater(3, 5))
    print(which_is_greater(42, 42))
    print(which_is_greater(-2, -7))

    print("Checking same sign:")
    print(same_sign(3, 5))  # True
    print(same_sign(-2, 0))  # True
    print(same_sign(-23, 17))  # False

    # Index of comparision operators:
    # < : less than
    # > : greater than
    # <= : less than or equal to
    # >= : greater than or equal to
    # == : equal to
    # != : not equal to


def same_sign(x: int, y: int) -> bool:
    """
    Take two integers as input and returns True if both have the same sign (both positive or both negative), False otherwise.

    Parameters:
    -x (int)
    -y (int)

    Returns:
    bool: True if both x and y have the same sign, False otherwise. (Zero has the same sign as all integers.)
    """
    # Three cases:
    # 1. both positive
    # 2. both negative
    # 3. Opposite signs

    if x >= 0 and y >= 0:
        return True  # both positive
    elif x <= 0 and y <= 0:
        return True  # both negative
    else:  # They can't have same sign
        return False  # opposite signs


def min_2(a: int, b: int) -> int:
    """
    Take two integers and returns their minimum.

    Parameters:
    -a (int)
    -b (int)

    Returns:
    int: The minimum of a and b.
    """

    if a < b:
        return a  # a is smaller
    else:
        return b  # b is greater or equal to a


def which_is_greater(x: int, y: int) -> int:
    """
    Take two integers as input and returns 1 if first is greater, -1 if second is greater, and 0 if they are equal.
    Parameters:
    -x (int)
    -y (int)

    Returns:
    int: 1 if x > y, -1 if x < y, and 0 if x = y
    """

    if x == y:
        return 0  # both are equal
    elif x > y:
        return 1  # x is greater
    else:
        return -1  # y is greater


if __name__ == "__main__":
    main()
