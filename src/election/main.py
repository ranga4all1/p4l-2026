import random
from election_io import read_electoral_votes, read_polling_data


def main():
    print("Simulating the 2016 US Presidential election.")

    electrol_vote_file = "data/electoralVotes.csv"
    poll_file = "data/earlyPolls.csv"

    electrol_votes = read_electoral_votes(electrol_vote_file)
    polls = read_polling_data(poll_file)

    print("Files read successfully.")
    print("Sanity check...")
    print("-" * 50)
    print(electrol_votes)
    print("-" * 50)
    print(polls)
    print("-" * 50)

    # set some parameters for the simulation
    num_trials = 100000
    margin_of_error = 0.05

    print("Simulation run...")

    probability_1, probability_2, probability_tie = simulate_multiple_elections(
        polls, electrol_votes, num_trials=num_trials, margin_of_error=margin_of_error
    )

    print(f"Probability of candidate 1 winning: {probability_1}")
    print(f"Probability of candidate 2 winning: {probability_2}")
    print(f"Probability of a tie: {probability_tie}")
    print("=" * 50)


def simulate_multiple_elections(
    polls: dict[str, float],
    electoral_votes: dict[str, int],
    num_trials: int,
    margin_of_error: float,
) -> tuple[float, float, float]:
    """
    Simulates multiple elections and calculates winning probabilities.

    Parameters:
    - polls (dict[str, float]): A dictionary of state names to polling percentages for candidate 1.
    - electoral_votes (dict[str, int]): A dictionary of state names to electoral votes.
    - num_trials (int): The number of trials to run.
    - margin_of_error (float): The margin of error in the polls.

    Returns:
    - tuple[float, float, float]: The estimated probabilities of candidate 1 winning,
      candidate 2 winning, and a tie.
    """

    if num_trials <= 0:
        raise ValueError("num_trials must be positive.")
    if margin_of_error < 0:
        raise ValueError("margin_of_error must be non-negative.")

    win_count_1 = 0
    win_count_2 = 0
    tie_count = 0

    # these hold the number of wins for each outcome; what we want is the ratio

    # we need to run simualtions and count the outcomes
    for _ in range(num_trials):
        votes_1, votes_2 = simulate_one_election(
            polls, electoral_votes, margin_of_error
        )
        if votes_1 > votes_2:
            win_count_1 += 1
        elif votes_2 > votes_1:
            win_count_2 += 1
        else:
            tie_count += 1

    probability_1 = win_count_1 / num_trials
    probability_2 = win_count_2 / num_trials
    probability_tie = tie_count / num_trials

    return probability_1, probability_2, probability_tie


def simulate_one_election(
    polls: dict[str, float], electoral_votes: dict[str, int], margin_of_error: float
) -> tuple[int, int]:
    """
    Simulates one election and calculates electoral college votes for each candidate.

    Parameters:
    - polls (dict[str, float]): A dictionary of state names to polling percentages for candidate 1.
    - electoral_votes (dict[str, int]): A dictionary of state names to electoral votes.
    - margin_of_error (float): The margin of error in the polls.

    Returns:
    - tuple[int, int]: The number of electoral college votes for each of the two candidates.
    """
    # basic checks
    if margin_of_error < 0:
        raise ValueError("margin_of_error must be non-negative.")

    college_votes_1 = 0
    college_votes_2 = 0

    # we need to loop through each state and determine the winner
    for state, polling_value in polls.items():
        num_votes = electoral_votes[state]

        # where is randomness
        adjusted_poll = add_noise(polling_value, margin_of_error)

        # as a result, which candidate is simulated to win the state?
        if adjusted_poll > 0.5:
            # candidate 1 wins the state
            college_votes_1 += num_votes
        elif adjusted_poll < 0.5:
            # candidate 2 wins the state
            college_votes_2 += num_votes
        else:
            # in the case of a tie, we can split the votes
            college_votes_1 += num_votes / 2
            college_votes_2 += num_votes / 2

    return int(college_votes_1), int(college_votes_2)


def add_noise(polling_value: float, margin_of_error: float) -> float:
    """
    Adds random noise to a polling value.

    Parameters:
    - polling_value (float): The polling value for candidate 1.
    - margin_of_error (float): The margin of error.

    Returns:
    - float: An adjusted polling value for candidate 1 after adding(subtracting) random noise.
    """
    if margin_of_error < 0 or polling_value < 0 or polling_value > 1:
        raise ValueError("Invalid polling value or margin of error.")

    # margin of error  is the value y such that there is a 95% chance that
    # the true value is within y percentage points of the polling value

    # draw from a standard normal and scale so ~95% of samples lie within
    # +/- `margin_of_error`. For a standard normal, ~95% of values fall
    # within +/- 1.96 sigma, so scale by `margin_of_error / 1.96`.
    x = random.gauss(0, 1)
    x *= margin_of_error / 1.96

    # add the noise to the polling value; this simulates the uncertainty in the polls
    return polling_value + x


if __name__ == "__main__":
    main()
