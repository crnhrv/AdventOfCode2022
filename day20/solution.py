def main(data):
    ordering = data[:]


def read_input(filename):
    with open(filename, encoding="utf8") as input_file:
        return list(map(int, input_file.read().splitlines()))


if __name__ == "__main__":
    dt = read_input("test-input.txt")
    main(dt)
