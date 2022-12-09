def main(data):
    print(data)


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return [(d[0], int(d[2])) for d in f.read().splitlines()]


if __name__ == "__main__":
    dt = read_input("test-input.txt")
    main(dt)
