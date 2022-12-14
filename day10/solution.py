def main(data):
    register_at_cycle = {}
    cycle = 1
    register = 1
    for (cycle_count, to_add) in data:
        register_at_cycle[cycle] = register
        if cycle_count == 2:
            register_at_cycle[cycle + 1] = register
        cycle += cycle_count
        register += to_add

    answer1 = 0
    important_cycles = [20, 60, 100, 140, 180, 220]
    for cycle in important_cycles:
        answer1 += register_at_cycle[cycle] * cycle
    print(answer1)

    print_crt(register_at_cycle)


def print_crt(register_at_cycle):
    crt_width = 40
    crt = [
        ["." for _ in range(crt_width)]
        for _ in range(len(register_at_cycle) // crt_width)
    ]
    crt_current_position = 1
    for (i, row) in enumerate(crt):
        for (j, _) in enumerate(row):
            sprite_position = register_at_cycle[crt_current_position]
            if abs(sprite_position - j) <= 1:
                crt[i][j] = "#"
            crt_current_position += 1
            print(crt[i][j], end="")
        print("\n", end="")


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        data = []
        for line in f.read().splitlines():
            command = line.split(" ")
            if len(command) == 1:
                data.append((1, 0))
            else:
                data.append((2, int(command[1])))
    return data


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
