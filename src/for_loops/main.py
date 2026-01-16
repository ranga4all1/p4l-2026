def main():
    print("For loops in Python.")

    print("Factorial of given int:")
    print(another_factorial(5))  # Expected output: 120
    print(another_factorial(0))  # Expected output: 1
    print(another_factorial(1))  # Expected output: 1

    print(pittsburg_january())

    print("Sum of first 10 even integers:")
    print(sum_even(10))  # Expected output: 90

    print("Sum of first 0 even integers:")
    try:
        print(sum_even(0))  # Expected to raise ValueError
    except ValueError as e:
        print(f"Error: {e}")


def sum_even(k: int) -> int:
    """
    Computes the sum of the first k even integers.

    Parameters:
    - k (int)

    Returns:
    - int : sum of first k even integers
    """
    if k <= 0:
        raise ValueError("k must be positive.")

    total = 0  # Initialize sum variable

    for i in range(k):
        total += 2 * i  # Add the ith even number

    return total


def pittsburg_january():
    """
    Simulates Pittsburg's winter.
    Each day has 80% chance of snow and 20% chance of dream.

    Returns:
    - str : Description of the weather
    """
    day = 1
    dream = True  # Assume we start with a dream

    for day in range(1, 32):  # Days 1 to 31
        import random

        weather = random.choices(["snow", "dream"], weights=[0.8, 0.2])[0]
        if weather == "snow":
            dream = False
            print(f"Day {day}: Snowed. Dreaming of Tampa")
        else:
            dream = True
            print(f"Day {day}: No snow. Headed to Tampa.")


def another_factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer n using a for loop.

    Parameters:
    - n (int)

    Returns:
    - int : n!
    """
    p = 1  # Initialize product variable

    for i in range(1, n + 1):
        p = p * i  # Update the product

    return p


if __name__ == "__main__":
    main()
