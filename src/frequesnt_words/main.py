def main():
    print("Frequent word finder.")

    # Example usage
    text = "the quick brown fox jumps over the lazy dog the quick brown fox"
    k = 2
    result = frequent_words(text, k)
    print(f"The {k} most frequent words are: {result}")


def frequent_words(text: str, k: int) -> list[str]:
    """
    Returns the k most frequent words in the given text.
    """
    if k <= 0:
        raise ValueError("Error: k must be a positive integer.")

    words = text.split()
    if k > len(words):
        return []

    from collections import Counter

    word_counts = Counter(words)
    most_common = word_counts.most_common(k)
    return [word for word, count in most_common]


def max_map_value(map_: dict[str, int]) -> int:
    """
    Returns the maximum value in the given map of counts.
    """
    if not map_:
        return 0
    max_value = float("-inf")
    for val in map_.values():
        if val > max_value:
            max_value = val
    return int(max_value)


def frequency_table(text: str) -> dict[str, int]:
    """
    Returns a frequency table (word -> count) for the words in the given text.
    """
    words = text.split()
    freq_map: dict[str, int] = {}
    for w in words:
        freq_map[w] = freq_map.get(w, 0) + 1
    return freq_map


if __name__ == "__main__":
    main()
