def main():
    print("Substrings (and sublists).")

    #

    s = "Hi Lovers"
    print(s[1:5])  # length 4, "i Lo"

    print(s[0:7])  # Hi Love, or s[0:7]
    print(s[4 : len(s)])  # overs or s[4:len(s)]

    a = [0] * 6
    for i in range(len(a)):
        a[i] = 2 * i + 1

    a = [1, 3, 5, 7, 9, 11]
    print(a)

    print(a[3:5])  # [7, 9]
    print(a[:3])  # [1, 3, 5]
    print(a[4:])  # [9, 11]

    # pattern count
    text = "GCGCG"
    pattern = "GCG"
    count = pattern_count(pattern, text)
    print(f"Pattern '{pattern}' occurs {count} times in text '{text}'.")

    # another example
    text = "ATATATAT"
    pattern = "ATA"
    count = pattern_count(pattern, text)
    print(f"Pattern '{pattern}' occurs {count} times in text '{text}'.")

    # starting indices
    text = "GCGCG"
    pattern = "GCG"
    indices = starting_indices(pattern, text)
    print(f"Pattern '{pattern}' found at indices {indices} in text '{text}'.")


def starting_indices(pattern: str, text: str) -> list[int]:
    """
    Docstring for starting_indices

    :param pattern: Description
    :type pattern: str
    :param text: Description
    :type text: str
    :return: Description
    :rtype: list[int]
    """
    indices = []
    pattern_length = len(pattern)
    for i in range(len(text) - pattern_length + 1):
        substring = text[i : i + pattern_length]
        if substring == pattern:
            indices.append(i)
    return indices


def pattern_count(pattern: str, text: str) -> int:
    """
    Docstring for pattern_count

    :param pattern: Description
    :type pattern: str
    :param text: Description
    :type text: str
    :return: Description
    :rtype: int
    """
    count = 0
    pattern_length = len(pattern)
    for i in range(len(text) - pattern_length + 1):
        substring = text[i : i + pattern_length]
        if substring == pattern:
            count += 1
    return count


if __name__ == "__main__":
    main()
