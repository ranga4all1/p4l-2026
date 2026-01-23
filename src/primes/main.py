def trivial_prime_finder(n: int) -> list[bool]:
    """
    DFinds all prime numbers up to and possible including n.

    Parameters:
    - n: int

    Output:
    A list of booleans where True indicates a prime number.
    """

    prime_booleans = [False] * (n + 1)  # set default values

    for p in range(2, n + 1):  # We know 0 and 1 are not prime
        # is it the case that p is prime?
        prime_booleans[p] = is_prime(p)

    return prime_booleans


def is_prime(p: int) -> bool:
    """
    Returns True if p is prime, False otherwise.

    Parameters:
        p: int

    Returns:
        bool
    """
    if p < 0:
        raise ValueError("Negative int given as input.")

    # easy cases: p = 0 or 1 (False)
    if p < 2:
        return False

    # check every possible candidate divisor of p
    for k in range(2, p):
        # is k a divisor of p?
        if p % k == 0:
            # yes, divisor of p, so p is not prime
            return False

    # if we survive all divisor checks, p is prime
    return True


def main():
    print("Prime finding.")

    n = 11
    prime_booleans = trivial_prime_finder(n)
    print(f"Primes up to {n}: {prime_booleans}")

    print(f"Is 7 prime?: {is_prime(7)}")


if __name__ == "__main__":
    main()
