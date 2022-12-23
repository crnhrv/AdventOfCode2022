import collections


class Directions:
    N = (0, -1)
    S = (0, 1)
    E = (1, 0)
    W = (-1, 0)
    NE = (1, -1)
    NW = (-1, -1)
    SW = (-1, 1)
    SE = (1, 1)


def main(elves, rounds, find_last_round):

    directions = [
        [Directions.N, Directions.NE, Directions.NW],
        [Directions.S, Directions.SE, Directions.SW],
        [Directions.W, Directions.NW, Directions.SW],
        [Directions.E, Directions.NE, Directions.SE],
    ]
    max_n = float("inf")
    max_s = float("-inf")
    max_e = float("-inf")
    max_w = float("inf")
    total_rounds = 1
    while rounds:
        elves_in_the_round = []
        for elf in elves:
            if elf_in_any_direction(elf, directions, elves):
                elves_in_the_round.append(elf)

        proposed = collections.defaultdict(list)
        for elf in elves_in_the_round:
            for cardinal_directions in directions:
                if no_elf_in_direction(elf, cardinal_directions, elves):
                    new_elf = get_new_elf_pos(elf, cardinal_directions[0])
                    proposed[new_elf].append(elf)
                    break
        no_elf_moved = True
        for (proposition, proposing_elves) in proposed.items():
            if len(proposing_elves) > 1:
                continue
            no_elf_moved = False
            elf = proposing_elves[0]
            elves.remove(elf)
            new_elf = proposition
            max_n = min(new_elf[1], max_n)
            max_w = min(new_elf[0], max_w)
            max_s = max(new_elf[1], max_s)
            max_e = max(new_elf[0], max_e)
            elves.add(new_elf)

        if no_elf_moved and find_last_round:
            print(total_rounds)  # ans2
            exit(0)
        first_direction = directions.pop(0)
        directions.append(first_direction)
        rounds -= 1
        total_rounds += 1
    count = 0
    for y in range(max_n, max_s + 1):
        for x in range(max_w, max_e + 1):
            if (x, y) in elves:
                print("#", end="")
            else:
                count += 1
                print(".", end="")
        print()
    print(count)  # ans1


def get_new_elf_pos(elf, direction):
    new_x = elf[0] + direction[0]
    new_y = elf[1] + direction[1]
    return (new_x, new_y)


def no_elf_in_direction(elf, directions, elves):
    for direction in directions:
        new_elf = get_new_elf_pos(elf, direction)
        if new_elf in elves:
            return False
    return True


def elf_in_any_direction(elf, directions, elves):
    seen_directions = set()
    for cardinal_directions in directions:
        for direction in cardinal_directions:
            if direction in seen_directions:
                continue
            seen_directions.add(direction)
            new_elf = get_new_elf_pos(elf, direction)
            if new_elf in elves:
                return True

    return False


def read_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        elves = set()
        for (y, line) in enumerate(lines):
            for (x, land) in enumerate(line):
                if land == "#":
                    elves.add((x, y))
    return elves


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt.copy(), 10, False)
    main(dt.copy(), 1000000, True)
