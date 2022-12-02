def main():
    points = {"X": 1, "Y": 2, "Z": 3}
    win_key = {"X": "C", "Y": "A", "Z": "B"}

    total_score = 0
    with open("input.txt", encoding="utf8") as input_file:
        rounds = input_file.read().splitlines()
        for rps_round in rounds:
            (move, counter) = rps_round.split(" ")
            total_score += points[counter]
            if win_key[counter] is move:
                total_score += 6
            elif ord(counter) - ord(move) == 23:
                total_score += 3
    print(total_score)  # answer 1


if __name__ == "__main__":
    main()
