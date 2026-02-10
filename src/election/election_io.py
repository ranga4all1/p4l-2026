import csv


def read_electoral_votes(filename: str) -> dict[str, int]:
    """
    Processes the number of electoral votes for each state.

    Parameters:
        filename (str): A filename string.

    Returns:
        dict[str, int]: A dictionary that associates each state name (string)
        to an integer corresponding to its number of Electoral College votes.
    """
    if len(filename) == 0 or not isinstance(filename, str):
        raise ValueError("filename must be a non-empty string.")

    electrol_voates: dict[str, int] = {}
    with open(filename, "r") as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            state_name, votes = row[0], int(row[1])
            electrol_voates[state_name] = votes
    return electrol_voates


def read_polling_data(filename: str) -> dict[str, float]:
    """
    Parses polling percentages from a file.

    Parameters:
    - filename (str): A filename string.

    Returns:
    - dict[str, float]: A dictionary of state names (strings) to floats
      corresponding to the percentages for candidate 1.
    """
    if len(filename) == 0 or not isinstance(filename, str):
        raise ValueError("filename must be a non-empty string.")

    candidate_1_percentages: dict[str, float] = {}

    with open(filename, "r") as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            state_name, percentage = row[0], float(row[1])
            candidate_1_percentages[state_name] = percentage / 100.0
    return candidate_1_percentages
