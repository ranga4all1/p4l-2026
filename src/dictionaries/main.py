def main():
    print("Dictionaries.")

    electrol_votes: dict[str, int] = {
        "Pensylvania": 20,
        "Ohio": 18,
        "Texas": 38,
    }

    print(f"Electrol votes 2020: {electrol_votes}")
    update_votes_2024(electrol_votes)
    print(f"Electrol votes 2024: {electrol_votes}")

    print(
        "As of 2024, the number of votes in Pensylvania is:",
        electrol_votes["Pensylvania"],
    )

    # Dictionaries are passed by reference

    # ranging over dicrtionaries

    for key, votes in electrol_votes.items():
        print(f"{key} has {votes} electrol votes.")

    keys = list(electrol_votes.keys())
    print(f"Keys: {keys}")

    # sort the keys
    keys.sort()
    print(f"Sorted Keys: {keys}")

    # range over sorted keys
    for key in keys:
        print(f"{key} has {electrol_votes[key]} electrol votes.")


def update_votes_2024(votes: dict[str, int]) -> None:
    """
    Docstring for update votes from 2020 to 2024

    :param votes: Description
    :type votes: dict[str, int]

    Returns:
        None
    """
    votes["Pensylvania"] = 19
    votes["Ohio"] = 17
    votes["Texas"] = 40


def complment(dna: str) -> str:
    dna2 = ""
    comp_dict: dict[str, str] = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }
    for symbol in dna:
        dna2 += comp_dict[symbol]
    return dna2


if __name__ == "__main__":
    main()
