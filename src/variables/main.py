def main():
    print("Variables.")

    # Python wonn't read this line

    # Define variables
    j = 14  # Integer variable
    x = -2.3  # Float variable
    yo_world = "Hi"  # String variable, this is snake_case
    statement = True  # Boolean variable

    # Print variables
    # print(j)
    # print(x)
    # print(yo_world)
    # print(statement)

    print(j, x, yo_world, statement)

    print(type(j), type(x), type(yo_world), type(statement))

    # Python uses dynamic typing (type of vaariables can change)

    yo_world = 2.718
    statement = "I hate python :)"

    print(yo_world)
    print(statement)

    print(type(j), type(x), type(yo_world), type(statement))

    print(2 * (j + 5))
    print(x / 4 + 3.16)

    # Python even allows mixed type math
    print(x * j)

    print("After multiplication, j has type:", type(j))

    # We have three additional operations
    print(14 / 3)  # Float division: 4.666...
    print(14 // 3)  # Integer division (floor division): 4
    print(14 % 3)  # Modulus (remainder): 2
    print(14**3)  # Exponentiation: 2744


if __name__ == "__main__":
    main()
