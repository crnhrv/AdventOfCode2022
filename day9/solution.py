def main(path):
    h_current = (0, 0)
    t_current = (0, 0)
    traversed = set()
    traversed.add(t_current)
    prev = ()
    for (direction, distance) in path:
        delta = (0, 0)
        match direction:
            case "U":
                delta = (1, 0)
            case "D":
                delta = (-1, 0)
            case "L":
                delta = (0, -1)
            case "R":
                delta = (0, 1)
        while distance:
            distance -= 1
            prev = h_current
            h_current = update_position(h_current, delta)
            if out_of_range(h_current, t_current):
                t_current = prev
                traversed.add(t_current)
    print(len(traversed))


def out_of_range(h, t):
    return abs(h[0] - t[0]) >= 2 or abs(h[1] - t[1]) >= 2


def update_position(current, delta):
    new_x = current[0] + delta[0]
    new_y = current[1] + delta[1]
    return (new_x, new_y)


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        data = []
        for line in f.read().splitlines():
            (direction, move) = line.split(" ")
            data.append((direction, int(move)))
    return data


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
