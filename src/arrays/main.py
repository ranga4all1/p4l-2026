def main():
    print("Arrays in Python (tuples and lists).")

    # tuples are useful whyen we know values in advance and they won't change
    primes = (2, 3, 5, 7, 11)
    print("Primes:", primes)

    # tuples are immutable
    # tuples are 0 indexed

    # lists are mutable
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("Fibonacci:", fibonacci)
    # lists are also 0 indexed
    # we can append to lists
    fibonacci.append(55)
    print("Fibonacci after appending 55:", fibonacci)
    # we can modify elements in lists
    fibonacci[0] = 1
    print("Fibonacci after modifying first element to 1:", fibonacci)
    # we can remove elements from lists
    fibonacci.remove(21)
    print("Fibonacci after removing 21:", fibonacci)

    #  empty list
    squares = []
    for i in range(10):
        squares.append(i * i)
    print("Squares of first 10 natural numbers:", squares)

    mixed_list = [1, "two", 3.0, (4, 5), [6, 7]]
    print("Mixed list:", mixed_list)

    #  lists use o based indexing (indices start at 0 to n-1 where n is length of list)
    print("First element of Fibonacci list:", fibonacci[0])
    print("Last element of Fibonacci list:", fibonacci[-1])
    print("Elements from index 2 to 5 of Fibonacci list:", fibonacci[2:6])

    # length of list
    print("Length of Fibonacci list:", len(fibonacci))


if __name__ == "__main__":
    main()
