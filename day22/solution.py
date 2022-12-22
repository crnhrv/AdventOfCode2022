class CardinalDirections:
    East = 0
    South = 1
    West = 2
    North = 3


def main(data):
    (current_position, open_tiles, walls, _, commands) = data
    current_direction = CardinalDirections.East
    move_turn = 1
    while commands:
        command = commands.pop()
        if move_turn % 2:
            distance = int(command)
            while distance:
                possible_next_tile = get_next_possible_tile(
                    current_direction, current_position
                )
                confirmation_result = confirm_next_tile(
                    possible_next_tile,
                    walls,
                    open_tiles,
                    current_direction,
                )
                if confirmation_result[0]:
                    current_position = confirmation_result[1]
                else:
                    break
                distance -= 1
        else:
            current_direction = turn(command, current_direction)
        move_turn += 1
    final_col = current_position[0] + 1
    final_row = current_position[1] + 1
    ans1 = 1000 * final_row + 4 * final_col + current_direction
    print(ans1)


def turn(turn_direction: str, current: int):
    match turn_direction:
        case "R":
            return (current + 1) % 4
        case "L":
            return (current - 1) % 4


def get_next_possible_tile(direction: int, current_position):
    match direction:
        case CardinalDirections.East:
            return (current_position[0] + 1, current_position[1])
        case CardinalDirections.West:
            return (current_position[0] - 1, current_position[1])
        case CardinalDirections.North:
            return (current_position[0], current_position[1] - 1)
        case CardinalDirections.South:
            return (current_position[0], current_position[1] + 1)
        case _:
            return False


def confirm_next_tile(possible_tile, walls, open_tiles, direction):
    if possible_tile in walls:
        return (False, possible_tile)
    if possible_tile in open_tiles:
        return (True, possible_tile)
    else:
        rebounded_tile = find_first_tile_in_bounds(
            direction,
            open_tiles,
            walls,
            possible_tile,
        )
        return confirm_next_tile(rebounded_tile, walls, open_tiles, direction)


def find_first_tile_in_bounds(direction, open_tiles, walls, possible_tile):
    tile_row = [tile for tile in open_tiles | walls if tile[1] == possible_tile[1]]
    tile_col = [tile for tile in open_tiles | walls if tile[0] == possible_tile[0]]
    match direction:
        case CardinalDirections.East:
            return min((tile for tile in tile_row), key=lambda x: x[0])
        case CardinalDirections.West:
            return max((tile for tile in tile_row), key=lambda x: x[0])
        case CardinalDirections.North:
            return max((tile for tile in tile_col), key=lambda x: x[1])
        case CardinalDirections.South:
            return min((tile for tile in tile_col), key=lambda x: x[1])


def read_input(filename):
    with open(filename, encoding="utf8") as input_file:
        lines = input_file.read().splitlines()
        open_tiles = set()
        walls = set()
        off_the_map = set()
        starting_pos = None
        for (y, row) in enumerate(lines[0:-2]):
            for (x, terrain) in enumerate(list(row)):
                match terrain:
                    case ".":
                        if not starting_pos:
                            starting_pos = (x, y)
                        open_tiles.add((x, y))
                    case "#":
                        walls.add((x, y))
                    case _:
                        off_the_map.add((x, y))
        command_line = lines[-1]
        command_line = command_line.replace("L", ",L,")
        command_line = command_line.replace("R", ",R,")
        commands = command_line.split(",")
        commands.reverse()
        return (starting_pos, open_tiles, walls, off_the_map, commands)


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
