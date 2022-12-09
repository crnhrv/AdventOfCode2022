def part1(path):
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


def part2(path):
    rope = [(0, 0) for _ in range(10)]
    traversed = set()
    traversed.add((0, 0))
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
            prev_tail = rope[-1]
            rope = update_rope(rope, delta)
            if prev_tail != rope[-1]:
                traversed.add(rope[-1])

    print(len(traversed))


def update_rope(old_rope, delta):
    new_rope = []
    new_rope.append(update_position(old_rope[0], delta))
    for (i, knot) in enumerate(old_rope[1:]):
        new_head = new_rope[i]
        new_tail = knot
        if out_of_range(new_head, new_tail):
            new_tail = find_new_position(new_head, new_tail)
        new_rope.append(new_tail)
    return new_rope


def out_of_range(h, t):
    return abs(h[0] - t[0]) >= 2 or abs(h[1] - t[1]) >= 2


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def find_new_position(head, tail):
    return update_position(
        tail, (clamp(head[0] - tail[0], -1, 1), clamp(head[1] - tail[1], -1, 1))
    )


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
    part1(dt)
    part2(dt)
