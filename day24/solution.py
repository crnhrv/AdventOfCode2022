import collections


class Directions:
    U = (0, -1)
    D = (0, 1)
    L = (-1, 0)
    R = (1, 0)

    def convert_direction(blizzard):
        match blizzard:
            case ">":
                return Directions.R
            case "^":
                return Directions.U
            case "<":
                return Directions.L
            case "v":
                return Directions.D


def main(data):
    (current_position, ending_spot, _, walls, blizzards) = data
    directions = [Directions.U, Directions.L, Directions.D, Directions.R]
    max_x = max(w[0] for w in walls) - 1
    max_y = max(w[1] for w in walls) - 2
    minutes = 0
    positions = [(current_position, minutes)]
    quickest = float("inf")
    stack = collections.deque(positions)
    blizzard_cache = {}
    seen = set()

    while stack:
        (current_position, minutes) = stack.popleft()
        if minutes > quickest:
            continue
        if current_position == ending_spot:
            quickest = min(minutes, quickest)
            continue

        if minutes in blizzard_cache:
            current_blizzards = blizzard_cache[minutes]
        else:
            new_blizzards = []
            for (blizzard, direction) in blizzards.copy():
                new_bpos = move_blizzard(blizzard, direction, max_x, max_y)
                new_blizzards.append((new_bpos, direction))
            blizzards = new_blizzards
            current_blizzards = set((x[0] for x in blizzards))
            blizzard_cache[minutes] = current_blizzards
        key = (current_position, minutes)
        if key in seen:
            continue
        seen.add(key)
        potentials = set(
            [move(current_position, direction) for direction in directions]
        )
        new_locations = potentials - current_blizzards - walls

        for new_location in new_locations:
            stack.append((new_location, minutes + 1))

        if not new_locations:
            stack.append((current_position, minutes + 1))

    print(quickest)


def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def move_blizzard(position, direction, max_x, max_y):
    new_pos = move(position, direction)
    if new_pos[0] < 1:
        return (max_x, new_pos[1])
    if new_pos[0] > max_x:
        return (1, new_pos[1])
    if new_pos[1] < 1:
        return (new_pos[0], max_y)
    if new_pos[1] > max_y:
        return (new_pos[0], 1)
    return new_pos


def read_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        starting_spot = (0, 0)
        ending_spot = (0, 0)
        available_spots = set()
        walls = set()
        blizzards = []
        for (y, line) in enumerate(lines):
            for (x, spot) in enumerate(line):
                if spot == ".":
                    if y == 0:
                        starting_spot = (x, y)
                        walls.add((x, y - 1))
                        continue
                    if y == len(lines) - 1:
                        ending_spot = (x, y)
                        walls.add((x, y + 1))
                    available_spots.add((x, y))
                elif spot == "#":
                    walls.add((x, y))
                else:
                    direction = Directions.convert_direction(spot)
                    blizzards.append(((x, y), direction))
                    available_spots.add((x, y))
        print(blizzards)
        print(walls)
        print(available_spots)

    return (starting_spot, ending_spot, available_spots, walls, blizzards)


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
