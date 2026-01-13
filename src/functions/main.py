# def function_name(parameters):

# The definition of the functions can be placed anywhere in the file, but it is a good practice to place them at the beginning
# or in a separate module.

# BUT When executions are made, the interpreter reads the file from top to bottom and definitions must have already been encountered
# before being called.


def sum_two_ints(a: int, b: int) -> int:
    """
    Returns sum of two input integers.

    Parameters:
    - a: first integer
    - b: second integer

    Returns:
    int: a + b
    """
    return a + b  # this is output of the function


def double_and_duplicate(x: float) -> tuple[float, float]:
    """
    Returns a tuple with the double of the input value duplicated.

    Parameters:
    - x: input float value

    Returns:
    tuple[float, float]: (2*x, 2*x)
    """
    return 2 * x, 2 * x


def print_hi():
    """
    Takes no input and print Hi to the console.
    """
    print("Hi!")
    # Other things couold happen here
    # nothing ultimately gets returned by the function


def add_one(k: int) -> int:
    """
    Adds one to the input integer and returns the result.

    Parameters:
    - k: input integer

    Returns:
    int: k + 1
    """
    k = k + 1
    return k

    # With basic types(str, int, float  ...), python uses 'pass by value'.
    # Function arguments are passed by value (a copy is made)

    # 'Pass by reference' is used with complex types (like lists, dictionaries, custom objects ...)
    # In that case, a reference to the original object is passed to the function.

    # This is an important distinction to understand when working with functions in Python. OOB explains it well.


def main():
    """Main function to demonstrate the use of other functions."""

    print("Functions in Python.")

    x = 3
    n = sum_two_ints(x, 4)
    print("The sum of 3 and 4 is:", n)

    print(sum_two_ints(-2.1, 4.7))  # this will work but is not type safe
    print("type of result is", type(sum_two_ints(-2.1, 4.7)))

    print(double_and_duplicate(2.7))

    print_hi()

    # Let's call add_one()
    m = 17
    print(add_one(m))
    print("Original m is still:", m)  # m is unchanged


if __name__ == "__main__":
    main()
