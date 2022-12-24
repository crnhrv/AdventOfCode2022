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
    (starting_spot, ending_spot, available_spots, walls, blizzards) = data


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
                    elif y == len(lines) - 1:
                        ending_spot = (x, y)
                    else:
                        available_spots.add((x, y))
                elif spot == "#":
                    walls.add((x, y))
                else:
                    direction = Directions.convert_direction(spot)
                    blizzards.append(((x, y), direction))

    return (starting_spot, ending_spot, available_spots, walls, blizzards)


if __name__ == "__main__":
    dt = read_input("sample-input.txt")
    main(dt)
