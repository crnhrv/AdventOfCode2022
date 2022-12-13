def main(data):
    print(data)
    ans1 = 0
    ans2 = 0

    return (ans1, ans2)


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    dt = read_input("input.txt")
    (ans1, ans2) = main(dt)
    print(ans1)
    print(ans2)
