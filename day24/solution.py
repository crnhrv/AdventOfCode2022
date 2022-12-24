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
    (current_position, ending_spot, available_spots, walls, blizzards) = data
    distance_to_end = get_manhattan_distance(current_position, ending_spot)
    directions = [Directions.U, Directions.L, Directions.D, Directions.R]
    while distance_to_end > 0:
        current_blizzard_positions = set()
        new_blizzards = []
        for (blizzard, direction, spawn_point) in blizzards:
            new_blizzard_position = move(blizzard, direction)
            if new_blizzard_position in walls:
                new_blizzard = (spawn_point, direction, spawn_point)
                current_blizzard_positions.add(spawn_point)
            else:
                new_blizzard = (new_blizzard_position, direction, spawn_point)
                current_blizzard_positions.add(new_blizzard_position)
            new_blizzards.append(new_blizzard)

        potential_moves = []
        for direction in directions:
            new_position = move(current_position, direction)
            if new_position in (available_spots - current_blizzard_positions):
                potential_moves.append(new_position)

        potential_moves.sort(key=lambda x: get_manhattan_distance(x, ending_spot))

        # make this dfs?


def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def get_manhattan_distance(position: tuple[int, int], target_position: tuple[int, int]):
    return abs(position[0] - target_position[0]) + abs(position[1] - target_position[1])


def get_blizzard_spawn(blizzard, direction, max_x, max_y):
    match direction:
        case Directions.L:
            return (max_x, blizzard[1])
        case Directions.R:
            return (1, blizzard[1])
        case Directions.U:
            return (blizzard[0], max_y)
        case Directions.D:
            return (blizzard[0], 1)


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
                    if y == len(lines) - 1:
                        ending_spot = (x, y)
                    available_spots.add((x, y))
                elif spot == "#":
                    walls.add((x, y))
                else:
                    direction = Directions.convert_direction(spot)
                    starting_position = get_blizzard_spawn(
                        (x, y), direction, len(line) - 2, len(lines) - 2
                    )
                    blizzards.append(((x, y), direction, starting_position))
                    available_spots.add((x, y))

    return (starting_spot, ending_spot, available_spots, walls, blizzards)


if __name__ == "__main__":
    dt = read_input("sample-input.txt")
    main(dt)
