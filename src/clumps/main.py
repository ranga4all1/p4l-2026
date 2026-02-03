from helper import frequency_table
import requests


def main():
    print("Finding Clumps.")

    # Example usage
    text = "ACGTACGTACGT"
    k = 3
    t = 2
    window_length = 8
    clumps = find_clumps(text, k, t, window_length)
    print(f"Clumps found: {clumps}")

    url = (
        "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"
    )
    response = requests.get(url)
    if response.status_code == 200:
        # ecoli_data = response.text.strip()
        # k = 9
        # t = 3
        # window_length = 500
        # ecoli_clumps = find_clumps(ecoli_data, k, t, window_length)
        # print(f"E. coli Clumps found: {ecoli_clumps}")

        # check length of genome data
        genome = response.text.strip()
        print(f"Length of E. coli genome: {len(genome)}")

        # Just to demonstrate, we run the clump finding on small subset
        subset = genome[:5000]
        k = 7
        t = 3
        window_length = 1000
        ecoli_clumps = find_clumps(subset, k, t, window_length)
        print(f"E. coli Clumps found in subset: {ecoli_clumps}")

    else:
        print("Failed to retrieve E. coli data.")


def find_clumps(text: str, k: int, t: int, window_length: int) -> list[str]:
    """
    Finds all substrings (clumps) of a specified length that occur more then some threshold multiple times within a given sequence.

    Parameters:
    - text: str
    - k: int
    - t: int
    - window_length: int
    Returns:
    - list[str]: All the strings of length k that occur at least t times within a window of length window_length in the sequence.
    """

    # what do we need to check in terms of errors?
    if k <= 0 or t <= 0 or window_length <= 0:
        raise ValueError("Error: Non-positive parameter value provided.")
    if len(text) == 0:
        raise ValueError("Error: Empty text provided.")
    if k > window_length:
        raise ValueError("Error: k value larger than window length provided.")
    if k > len(text):
        return []

    patterns_set: set[str] = set()
    n = len(text)
    for i in range(0, n - window_length + 1):
        if i % 1000 == 0:
            print(f"Processing window starting at index {i}...")
        window = text[i : i + window_length]
        frequency_map = frequency_table(window, k)
        for pattern, count in frequency_map.items():
            if count >= t:
                patterns_set.add(pattern)
    return sorted(patterns_set)


def find_clumps_global(text: str, k: int, t: int, window_length: int) -> list[str]:
    """
    Efficiently finds all k-mers that form clumps anywhere in the sequence by
    tracking positions of each k-mer and checking if t occurrences fall within
    a window of length `window_length`.

    This runs in O(n) time to build the positions map (plus additional work
    proportional to the number of k-mer occurrences) and is suitable for
    scanning whole genomes.
    """
    # validation same as find_clumps
    if k <= 0 or t <= 0 or window_length <= 0:
        raise ValueError("Error: Non-positive parameter value provided.")
    if len(text) == 0:
        raise ValueError("Error: Empty text provided.")
    if k > window_length:
        raise ValueError("Error: k value larger than window length provided.")
    if k > len(text):
        return []

    positions: dict[str, list[int]] = {}
    n = len(text)
    for i in range(0, n - k + 1):
        kmer = text[i : i + k]
        if kmer in positions:
            positions[kmer].append(i)
        else:
            positions[kmer] = [i]

    clumps: set[str] = set()
    # For each k-mer, check if any t positions fit inside a window of length (window_length - k)
    max_span = window_length - k
    for kmer, poslist in positions.items():
        if len(poslist) < t:
            continue
        # sliding check over positions
        for i in range(0, len(poslist) - t + 1):
            if poslist[i + t - 1] - poslist[i] <= max_span:
                clumps.add(kmer)
                break
    return sorted(clumps)


if __name__ == "__main__":
    main()
