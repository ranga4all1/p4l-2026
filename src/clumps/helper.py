def frequency_table(text: str, k: int) -> dict[str, int]:
    """
    Returns a frequency table of all k-length substrings (k-mers) in the given text.

    Parameters:
    - text: the sequence to analyze
    - k: length of substrings to count

    Returns:
    - dict mapping k-mer -> count
    """
    if k <= 0:
        raise ValueError("Error: k must be a positive integer.")
    if k > len(text):
        return {}

    freq: dict[str, int] = {}
    for i in range(len(text) - k + 1):
        kmer = text[i : i + k]
        freq[kmer] = freq.get(kmer, 0) + 1
    return freq
