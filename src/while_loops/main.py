def main():
    print("While loops in Python.")

    print("Factorial of given int:")
    print(factorial(5))  # Expected output: 120
    print(factorial(0))  # Expected output: 1
    print(factorial(1))  # Expected output: 1
    print(factorial(6))  # Expected output: 720

    # n = 5
    # m = factorial(n)
    # print(f"The factorial of {n} is {m}")

    print("0! is:", factorial(0))  # Expected output: 1
    # n! = n*(n-1)
    # 1! = 1*0! = 1*1 = 1
    # 1 = 0!

    # Edge case: Handle negative input
    try:
        print(factorial(-100))
    except ValueError as e:
        print(f"Error: {e}")

    print("Sum of first 100 integers:")
    print(sum_first_n_integers(100))  # Expected output: 5050

    print("Gauss sum of first 100 integers:")
    print(gauss_sum(100))  # Expected output: 5050

    print("GCD of 48 and 18:")
    print(euclid_gcd(48, 18))  # Expected output: 6


def euclid_gcd(a: int, b: int) -> int:
    """
    Computes the greatest common divisor (GCD) of two integers using Euclid's algorithm.

    Parameters:
    - a (int)
    - b (int)
    Returns:
    - int : GCD of a and b
    """
    while b != 0:
        a, b = b, a % b  # Update a and b
    return abs(a)  # GCD is always non-negative


def gauss_sum(n: int) -> int:
    """
    Computes the sum of the first n integers using Gauss's formula: n(n+1)/2

    Parameters:
    - n (int)

    Returns:
    - int : sum of first n integers

    Raises an error if n < 0
    """

    if n < 0:
        # Handle negative input gracefully with error message
        raise ValueError("negative input given to my gauss_sum function.")

    return n * (n + 1) // 2  # Using integer division


def sum_first_n_integers(n: int) -> int:
    """
    Computes the sum of the first n integers: 1 + 2 + ... + n

    Parameters:
    - n (int)

    Returns:
    - int : sum of first n integers

    Raises an error if n < 0
    """

    s = 0  # Initialize sum
    i = 1  # Counter variable

    if n < 0:
        # Handle negative input gracefully with error message
        raise ValueError("negative input given to my sum_first_n_integers function.")

    while i <= n:
        s += i  # Update the sum
        i += 1  # Update the counter
    return s


def factorial(n: int) -> int:
    """
    Produces n! = n * (n-1) * ...(2) * 1

    Parameters:
    -n (int)

    Returns:
    - int : n!

    Raises an error if n < 0
    """

    p = 1  # Think of p as the container that will represent my growing product.

    i = 1  # Counter variable

    if n < 0:
        # Handle negative input gracefully with error message
        raise ValueError("Factorial is not defined for negative numbers.")

    while i <= n:
        p = p * i  # Update the product (Left side: variable, Right side: value)
        i = i + 1  # Update the counter
    return p


if __name__ == "__main__":
    main()
