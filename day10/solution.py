def main(data):
    print(data)


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
