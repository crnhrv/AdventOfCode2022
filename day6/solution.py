def main(data):
    for line in data:
        print(get_marker(line, 4))
        print(get_marker(line, 14))


def get_marker(line, distinct):
    index = 0
    last_distinct = []
    while len(last_distinct) != distinct:
        if line[index + 1] == line[index]:
            last_distinct = []
        elif line[index] in [char for char, _ in last_distinct]:
            dupe_index = next(i for (char, i) in last_distinct if char == line[index])
            last_distinct = [(char, i) for (char, i) in last_distinct if i > dupe_index]

        last_distinct.append((line[index], index))

        index += 1
    return index


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
