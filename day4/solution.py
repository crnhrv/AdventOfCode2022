def main(pairs, check_fn):
    total = 0
    for (a, b) in [pair.split(",") for pair in pairs]:
        total += check_fn(
            [int(x) for x in a.split("-")], [int(x) for x in b.split("-")]
        )
    return total


def fully_contains(a, b):
    return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])


def overlap(a, b):
    return not (a[1] < b[0] or a[0] > b[1])


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    input_ = read_input("input.txt")
    print(main(input_, fully_contains))
    print(main(input_, overlap))
