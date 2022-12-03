def part1(rounds):
    move_points = {"X": 1, "Y": 2, "Z": 3}
    key = {"X": "C", "Y": "A", "Z": "B"}

    total_score = 0
    for rps_round in rounds:
        (move, counter) = rps_round.split(" ")
        total_score += move_points[counter]
        if key[counter] is move:
            total_score += 6
        elif ord(counter) - ord(move) == 23:
            total_score += 3

    print(total_score)  # answer 1


def part2(rounds):
    move_points = {"A": 1, "B": 2, "C": 3}
    key = {"A": "C", "B": "A", "C": "B"}

    total_score = 0
    for rps_round in rounds:
        (move, result) = rps_round.split(" ")
        if result == "Z":
            total_score += 6
            actual_counter = [
                winning_move
                for winning_move, losing_move in key.items()
                if losing_move is move
            ]
            total_score += move_points[actual_counter[0]]
        elif result == "Y":
            total_score += 3
            total_score += move_points[move]
        else:
            actual_counter = key[move]
            total_score += move_points[actual_counter]

    print(total_score)  # answer 2


def read_input():
    with open("input.txt", encoding="utf8") as input_file:
        data = input_file.read().splitlines()
    return data


if __name__ == "__main__":
    rps_data = read_input()
    part1(rps_data)
    part2(rps_data)
