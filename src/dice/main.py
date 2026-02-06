import random
import time


def main():
    print("Rolling dice and playing craps.")

    # Rules of craps:
    # 1. if x is 7 or 11, then the player wins, and receives their wager back in addition to the amount of the wager.
    # 2. if x is 2, 3, or 12, then the player loses, and forfeits their wager.
    # 3. if x has some other value, then the player rolls again, and continues to roll until either they roll x again (in which case they win),
    # or they roll 7 (in which case they lose). (Note that this is different to the first roll, when 7 is a winner.)

    # random.seed(time.time_ns())
    # # This is called automatically to establish starting point for generating random numbers,
    # but we can call it ourselves to reset the starting point.

    random.seed(0)

    print(random.random())
    print(random.randrange(0, 10))

    # Simulate rolling a die 10 times.
    for i in range(10):
        print("Rolling die:", roll_die())

    n = 200
    rolls = [roll_die() for i in range(n)]
    print(f"Simualted die rolls {n} times and sum:", sum(rolls))

    # Simulate rolling two dice and summing the result 10 times.
    for i in range(10):
        print(roll_dice_twice())

    # roll die twice and sum the result 1000 times, and count how many times we get each possible result (between 2 and 12, inclusive).
    n = 1000
    counts = {i: 0 for i in range(2, 13)}
    for i in range(n):
        result = roll_dice_twice()
        counts[result] += 1
    print(
        f"Simulated rolling two dice and summing the result {n} times, and counted how many times we got each possible result:"
    )
    for result in range(2, 13):
        print(f"{result}: {counts[result]}")

    # Simulate playing craps 1000 times, and compute the house edge of the game.
    num_trials = 1000
    house_edge = compute_craps_house_edge(num_trials)
    print(
        f"Simulated playing craps {num_trials} times, and computed the house edge of the game: {house_edge:.2f}%"
    )


def compute_craps_house_edge(num_trials: int) -> float:
    """
    Docstring for compute_craps_house_edge

    Parameters:
    - num_trials: The number of times to simulate playing craps.
    :return: The house edge of the game of craps, as a percentage.
    :rtype: float
    """
    # monte carlo simulation of playing craps num_trials times, and counting how many times the player wins and loses, to compute the house edge of the game.
    wins = 0
    losses = 0
    for i in range(num_trials):
        result = roll_dice_twice()
        if result in [7, 11]:
            wins += 1
        elif result in [2, 3, 12]:
            losses += 1
        else:
            # roll again until we get either result or 7
            while True:
                result2 = roll_dice_twice()
                if result2 == result:
                    wins += 1
                    break
                elif result2 == 7:
                    losses += 1
                    break

    # The house edge is the expected value of the player's loss per unit wagered, expressed as a percentage.
    # The player wins their wager back plus an additional amount equal to their wager when they win, and loses their wager when they lose.
    # So the expected value of the player's loss per unit wagered is (losses - wins) / num_trials.
    house_edge = (losses - wins) / num_trials * 100
    return house_edge


def roll_die() -> int:
    """
    Docstring for roll_die

    Parameters:
    - None
    :return: Description
    :rtype: int
    """
    return random.randrange(1, 7)


def roll_dice_twice() -> int:
    """
    Docstring for roll_dice_twice

    Parameters:
    - None
    :return: pseudorandom number between 2 and 12, inclusive, representing the sum of rolling two dice.
    :rtype: int
    """
    # roll = random.random()  # between 0 and 1
    # if roll < 1 / 36:
    #     return 2
    # elif roll < 3 / 36:
    #     return 3
    # elif roll < 6 / 36:
    #     return 4
    # elif roll < 10 / 36:
    #     return 5
    # elif roll < 15 / 36:
    #     return 6
    # elif roll < 21 / 36:
    #     return 7
    # elif roll < 26 / 36:
    #     return 8
    # elif roll < 30 / 36:
    #     return 9
    # elif roll < 33 / 36:
    #     return 10
    # elif roll < 35 / 36:
    #     return 11
    # else:
    #     return 12

    # same as above, but much simpler to read and understand, and less error-prone.
    return roll_die() + roll_die()


if __name__ == "__main__":
    main()
