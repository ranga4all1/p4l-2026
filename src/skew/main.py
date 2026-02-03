import matplotlib.pyplot as plt
import requests


def main():
    print("Skew arrays for finding replication origins.")

    # We want to find where. replication begins in bacterium
    # half of genome after original spends its life single stranded more often
    #

    # example usage
    genome = "GATACACTTCCCGAGTAGGTACTG"
    skew = skew_array(genome)
    print("Genome:", genome)
    print("Skew Array:", skew)

    print("Drawing skew array...")
    draw_skew_array(skew)
    # save and open file
    draw_skew_array(skew, show=False, filename="skew_array.png")

    # Example usage
    url = (
        "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"
    )
    response = requests.get(url)
    if response.status_code == 200:
        genome = response.text.strip()
        skew = skew_array(genome)
        print("Length of E. coli genome:", len(genome))
        draw_skew_array(skew, show=False, filename="ecoli_skew_array.png")
    else:
        print("Failed to retrieve E. coli data.")


def skew_array(genome: str) -> list[int]:
    """
    Computes the skew array for a given genome

    Parameters:
    - genome (str): The DNA sequence of the genome.

    Returns:
    - list[int]: A list representing the skew array.
    """

    if not genome:
        raise ValueError("Error: Genome sequence cannot be empty.")

    n = len(genome)
    skew_list = [0] * (n + 1)

    mapping: dict[str, int] = {"G": 1, "C": -1, "A": 0, "T": 0}

    for i in range(1, n + 1):
        nucleotide = genome[i - 1]
        if nucleotide in mapping:
            skew_list[i] = skew_list[i - 1] + mapping[nucleotide]
        else:
            raise ValueError(
                f"Error: Invalid nucleotide '{nucleotide}' found in genome sequence."
            )

    return skew_list


def draw_skew_array(
    skew: list[int], show: bool = True, filename: str | None = None, ax=None
) -> tuple["matplotlib.figure.Figure", "matplotlib.axes.Axes"]:
    """
    Draws a visualization of the skew array.

    Parameters:
    - skew (list[int]): The skew array to visualize.
    - show (bool): Whether to call ``plt.show()`` (disable in headless envs/tests).
    - filename (str | None): If provided, saves the figure to this file path.
    - ax (matplotlib.axes.Axes | None): Optional axes to plot on; if None a new figure/axes pair is created.

    Returns:
    - (Figure, Axes): The created or used matplotlib Figure and Axes objects.
    """
    if not isinstance(skew, list) or len(skew) == 0:
        raise ValueError("Error: 'skew' must be a non-empty list of integers.")

    # Create new figure/axes if none provided
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.plot(range(len(skew)), skew, marker="o")
    ax.set_title("Skew Array Visualization")
    ax.set_xlabel("Position in Genome")
    ax.set_ylabel("Skew Value (G - C)")
    ax.grid(True)
    fig.tight_layout()

    if filename:
        fig.savefig(filename)

    if show:
        plt.show()

    return fig, ax


if __name__ == "__main__":
    main()
