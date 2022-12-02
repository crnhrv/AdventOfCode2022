def day2_part1_main(rounds):
    # Set the score to 0
    score = 0

    # Define the values for each shape
    SHAPE_VALUES = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    # Loop through each round
    for round in rounds:
        # Split the round into opponent's shape and your shape
        opponent_shape, your_shape = round.split(" ")

        score += SHAPE_VALUES[your_shape]
        # Check if you win, lose, or draw
        if SHAPE_VALUES[opponent_shape] == SHAPE_VALUES[your_shape]:
            # It's a draw, add 3 to the score
            score += 3
        elif (
            (SHAPE_VALUES[opponent_shape] == 1 and SHAPE_VALUES[your_shape] == 3)
            or (SHAPE_VALUES[opponent_shape] == 2 and SHAPE_VALUES[your_shape] == 1)
            or (SHAPE_VALUES[opponent_shape] == 3 and SHAPE_VALUES[your_shape] == 2)
        ):
            # You lose, add 0 to the score
            score += 0
        else:
            # You win, add 6 to the score
            score += 6

    # Print the final score
    print("Total score:", score)


def day2_part2_main(rounds):
    # Set the score to 0
    score = 0

    # Define the values for each shape
    SHAPE_VALUES = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    # Loop through each round
    for round in rounds:
        # Split the round into opponent's shape and your shape
        opponent_shape, outcome = round.split(" ")

        # Choose your shape based on the outcome
        if outcome == "X":
            if opponent_shape == "A":
                your_shape = "C"
            elif opponent_shape == "B":
                your_shape = "A"
            else:
                your_shape = "B"
        elif outcome == "Y":
            your_shape = opponent_shape
        else:
            if opponent_shape == "A":
                your_shape = "B"
            elif opponent_shape == "B":
                your_shape = "C"
            else:
                your_shape = "A"

        # Add the value of your shape to the score
        score += SHAPE_VALUES[your_shape]

        # Check if you win, lose, or draw
        if SHAPE_VALUES[opponent_shape] == SHAPE_VALUES[your_shape]:
            # It's a draw, add 3 to the score
            score += 3
        elif (
            (SHAPE_VALUES[opponent_shape] == 1 and SHAPE_VALUES[your_shape] == 3)
            or (SHAPE_VALUES[opponent_shape] == 2 and SHAPE_VALUES[your_shape] == 1)
            or (SHAPE_VALUES[opponent_shape] == 3 and SHAPE_VALUES[your_shape] == 2)
        ):
            # You lose, add 0 to the score
            score += 0
        else:
            # You win, add 6 to the score
            score += 6

    # Print the final score
    print("Total score:", score)


def read_input():
    with open("input.txt", encoding="utf8") as input_file:
        data = input_file.read().splitlines()
    return data


if __name__ == "__main__":
    rps_data = read_input()
    day2_part1_main(rps_data)
    day2_part2_main(rps_data)
