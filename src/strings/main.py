def main():
    print("Strings.")

    s = "Hi"
    t = "Lovers"

    # Concatenation
    u = s + " " + t
    print("Concatenation:", u)

    print(s * 3)  # multiplication with strings is repeated

    # Strings are (kinda) tuples of symbols

    # So, we can access individual elements of a string by index
    print("First symbol:", s[0])
    print("Last symbol:", s[-1])

    if t[2] == "v":
        print("The symbol at position 2 is 'v'")

    # strings, like tuples are immutable
    # t[2] = "s"  # This would raise a TypeError - this is not allowed, I can't change individual letters

    # I can change the entire string
    s = "Yo"
    print("Changed s:", s)

    # we can use += shortcut too
    s += "-Yo"
    s += " Ma"
    print("Modified s:", s)

    dna = "ACCGAT"
    print("Original DNA:", dna)
    print("Complement DNA:", complement(dna))
    print("Reverse Complement DNA:", reverse_complement(dna))


def reverse_complement(dna: str) -> str:
    """Returns the reverse complement of a DNA string.

    e. g. "AGTC" -> "GACT"

    Parameters:
    - dnas: str : input DNA string
    Returns:
    - str : reverse complement of the input DNA string
    """

    # dna = complement(dna)   # complement of "AGTC" is "TCAG"
    # dna = reverse(dna)      # reverses the symbols in a string
    # return dna

    return reverse(complement(dna))


def complement(dna: str) -> str:
    """Returns the complement of a DNA string (without reversing it).

    e. g. "AGTC" -> "TCAG"

    Parameters:
    - dnas: str : input DNA string
    Returns:
    - str : complement of the input DNA string
    """

    # Range over  the string, take complement of each symbol, and concatenate them

    for i, symbol in enumerate(dna):
        if symbol == "A":
            dna = dna[:i] + "T" + dna[i + 1 :]
        elif symbol == "T":
            dna = dna[:i] + "A" + dna[i + 1 :]
        elif symbol == "G":
            dna = dna[:i] + "C" + dna[i + 1 :]
        elif symbol == "C":
            dna = dna[:i] + "G" + dna[i + 1 :]

    return dna


def reverse(s: str) -> str:
    """Reverses the input string.

    e. g. "AGTC" -> "CTGA"

    Parameters:
    - s: str : input string
    Returns:
    - str : reversed string
    """

    rev = ""
    for symbol in s:
        rev = symbol + rev  # prepend the symbol to the result

    return rev


if __name__ == "__main__":
    main()
