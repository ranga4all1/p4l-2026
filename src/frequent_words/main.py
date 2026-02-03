def main():
    print("Frequent word finder.")

    # Example usage: word frequency
    text = "the quick brown fox jumps over the lazy dog the quick brown fox"
    k = 2
    result = frequent_words(text, k)
    print(f"The {k} most frequent words are: {result}")

    # Example usage: DNA sequence k-mer frequency
    dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    kmer_len = 4
    kmer_result = frequent_kmers(dna, kmer_len)
    print(f"Most frequent {kmer_len}-mers in DNA: {kmer_result}")

    # dna sequence example
    dna_sequence = (
        "ATGCGTACGTTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAC"
        "GATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATAG"
        "CTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"
        "CGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGAT"
        "ATGCGTACGTTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"
        "CGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGAT"
        "AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT"
        "CGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGAT"
        "ATGCGTACGTTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"
        "CGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGAT"
    )

    k_dna = 3
    result_dna = frequent_words(dna_sequence, k_dna)
    print(f"The {k_dna} most frequent words in the DNA sequence are: {result_dna}")


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


def frequent_kmers(sequence: str, k: int) -> list[str]:
    """
    Returns the most frequent k-mers (substrings of length k) in the given DNA sequence.
    """
    if k <= 0:
        raise ValueError("Error: k must be a positive integer.")
    if k > len(sequence):
        return []
    from collections import Counter

    kmers = [sequence[i : i + k] for i in range(len(sequence) - k + 1)]
    kmer_counts = Counter(kmers)
    max_count = max(kmer_counts.values())
    return [kmer for kmer, count in kmer_counts.items() if count == max_count]


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
