"""
Docstring for gcd.main

TrivialGCD(a, b)
    d <- 1
    m <- Min2(a, b)
    for i in range(2, m + 1):
        if a % i == 0 and b % i == 0:
            d <- i
    return d
"""

# from conditionals.main import min_2
import time


# def faster_euclid_gcd(a: int, b: int) -> int:
#     """
#     Returns the GCD of two integers using a faster version of Euclid's algorithm.
#     Do not subtract, use modulus only.

#     Parameters:
#     - a (int): First integer
#     - b (int): Second integer

#     Returns:
#     - int: The GCD of a and b
#     """

#     a = abs(a)
#     b = abs(b)

#     while b != 0:
#         a, b = b, a % b
#     return a


def euclid_gcd(a: int, b: int) -> int:
    """
    Returns the GCD of two integers using Euclid's algorithm.

    Parameters:
    - a (int): First integer
    - b (int): Second integer

    Returns:
    - int: The GCD of a and b
    """

    # if (a <= 0) or (b <= 0):
    #     raise ValueError("Both numbers must be positive integers.")

    # Make both numbers non-negative
    # if a < 0:
    #     a = -a
    # elif b < 0:
    #     b = -b

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b
    return a


def trivial_gcd(a: int, b: int) -> int:
    """
    Returns the GCD of two intergers using a trivial algorithm
    that tries every possible divisor of a and b.

    Parameters:
    - a (int): First integer
    - b (int): Second integer

    Returns:
    - int: The GCD of a and b
    """

    # if (a <= 0) or (b <= 0):
    #     raise ValueError("Both numbers must be positive integers.")

    # Make both numbers non-negative
    # if a < 0:
    #     a = -a
    # elif b < 0:
    #     b = -b

    a = abs(a)
    b = abs(b)

    d = 1

    m = min(a, b)
    for p in range(2, m + 1):
        # if p is a divisor of both, then d = p
        if (a % p == 0) and (b % p == 0):
            d = p
    return d
    # if the first statement in an AND is false, the whole thing is immediately false
    # and 2nd condition is not evaluated.

    # x         y           x and y         x or y
    # True      True        True            True
    # True      False       False           True
    # False     True        False           True
    # False     False       False           False


def main():
    print("Studying GCD (Greatest Common Divisor) algorithms.")

    print("GCD of 12 and 15 is:", trivial_gcd(12, 15))

    x = 63
    y = 42
    print(f"GCD of {x} and {y} is:", trivial_gcd(x, y))

    # try:
    #     print("GCD of -12 and 15 is:", trivial_gcd(-12, 15))
    # except ValueError as e:
    #     print(f"Error: {e}")

    print("GCD of -12 and 15 is:", trivial_gcd(-12, 15))

    print("GCD of 12 and 15 is:", euclid_gcd(12, 15))
    print(f"GCD of {x} and {y} is:", euclid_gcd(x, y))

    # try:
    #     print("GCD of -12 and 15 is:", euclid_gcd(-12, 15))
    # except ValueError as e:
    #     print(f"Error: {e}")

    print("GCD of -12 and 15 is:", euclid_gcd(-12, 15))

    x = 37820262
    y = 27314790

    #  time the trivial approach
    start = time.time()
    print(f"GCD of {x} and {y} is:", trivial_gcd(x, y))
    end = time.time()
    elapsed_trivial = end - start
    print(f"Trivial GCD took {elapsed_trivial:.6f} seconds.")

    #  time Euclid's approach
    start = time.time()
    print(f"GCD of {x} and {y} is:", euclid_gcd(x, y))
    end = time.time()
    elapsed_euclid = end - start
    print(f"Euclid's GCD took {elapsed_euclid:.6f} seconds.")

    #  the speedup provided by Euclid's algorithm
    speedup = elapsed_trivial / elapsed_euclid
    print(
        f"Euclid's algorithm was {speedup:.2f} times faster than the trivial algorithm."
    )


if __name__ == "__main__":
    main()
