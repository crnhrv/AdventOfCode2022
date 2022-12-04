def main(pairs, check_fn):
    total = 0
    for (first, second) in [pair.split(",") for pair in pairs]:
        first_range = [int(x) for x in first.split("-")]
        second_range = [int(x) for x in second.split("-")]
        if check_fn(first_range, second_range):
            total += 1
    return total


def fully_contains(first, second):
    return (first[0] <= second[0] and first[1] >= second[1]) or (
        second[0] <= first[0] and second[1] >= first[1]
    )


def overlap(first, second):
    return (first[0] <= second[0] and first[1] >= second[0]) or (
        second[0] <= first[0] and second[1] >= first[0]
    )


def read_input(filename):
    with open(filename, encoding="utf8") as input_file:
        data = input_file.read().splitlines()
    return data


if __name__ == "__main__":
    input_ = read_input("input.txt")

    ANSWER1 = main(input_, fully_contains)
    ANSWER2 = main(input_, overlap)

    print(ANSWER1)
    print(ANSWER2)
