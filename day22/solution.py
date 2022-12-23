class CardinalDirections:
    East = 0
    South = 1
    West = 2
    North = 3


def main(data, is_cube: bool):
    (current_position, open_tiles, walls, off_the_map, commands, cubes) = data
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
                    is_cube,
                    cubes,
                    current_position,
                )
                if confirmation_result[0]:
                    current_position = confirmation_result[1]
                    if is_cube:
                        current_direction = confirmation_result[2]
                else:
                    break
                distance -= 1
        else:
            current_direction = turn(command, current_direction)
        move_turn += 1
    final_row = current_position[1] + 1
    final_col = current_position[0] + 1
    answer = 1000 * final_row + 4 * final_col + current_direction
    print(answer)


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


def confirm_next_tile(
    possible_tile: tuple[int, int],
    walls: set[tuple[int, int]],
    open_tiles: set[tuple[int, int]],
    direction: int,
    is_cube: bool,
    cubes: list[set[tuple[int, int]]],
    current_tile: tuple[int, int],
):
    if possible_tile in walls:
        return (False, None, direction)
    if possible_tile in open_tiles:
        return (True, possible_tile, direction)
    else:
        if is_cube:
            cube_number = find_current_cube(current_tile, cubes)
            (rebounded_tile, new_direction) = find_connecting_tile_large_cube(
                cube_number, cubes, current_tile, direction
            )
            if confirm_next_tile(
                rebounded_tile,
                walls,
                open_tiles,
                new_direction,
                is_cube,
                cubes,
                current_tile,
            )[0]:
                return (True, rebounded_tile, new_direction)
            else:
                return (False, None, direction)
        else:
            rebounded_tile = find_first_tile_in_bounds(
                direction,
                open_tiles,
                walls,
                possible_tile,
            )
        return confirm_next_tile(
            rebounded_tile,
            walls,
            open_tiles,
            direction,
            is_cube,
            cubes,
            current_tile,
        )


def find_current_cube(tile, cubes):
    for (i, cube) in enumerate(cubes):
        if tile in cube:
            return i


def find_connecting_tile_large_cube(
    current_cube: int, cubes, current_tile: tuple[int, int], direction: int
):
    match current_cube:
        case 0:  # verified
            match direction:
                case CardinalDirections.West:
                    new_cube = cubes[3]
                    return get_west_east_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
                case CardinalDirections.North:
                    new_cube = cubes[5]
                    return get_north_east_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
        case 1:  # verified
            match direction:
                case CardinalDirections.East:
                    new_cube = cubes[4]
                    return get_east_west_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
                case CardinalDirections.North:
                    new_cube = cubes[5]
                    return get_north_north_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
                case CardinalDirections.South:
                    new_cube = cubes[2]
                    return get_south_west_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
        case 2:  # veriofied
            match direction:
                case CardinalDirections.East:
                    new_cube = cubes[1]
                    return get_east_north_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
                case CardinalDirections.West:
                    new_cube = cubes[3]
                    return get_west_south_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
        case 3:  # veriofied
            match direction:
                case CardinalDirections.West:
                    new_cube = cubes[0]
                    return get_west_east_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
                case CardinalDirections.North:
                    new_cube = cubes[2]
                    return get_north_east_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
        case 4:  # verified
            match direction:
                case CardinalDirections.East:
                    new_cube = cubes[1]
                    return get_east_west_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
                case CardinalDirections.South:
                    new_cube = cubes[5]
                    return get_south_west_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
        case 5:
            match direction:
                case CardinalDirections.East:
                    new_cube = cubes[4]
                    return get_east_north_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
                case CardinalDirections.West:
                    new_cube = cubes[0]
                    return get_west_south_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )
                case CardinalDirections.South:
                    new_cube = cubes[1]
                    return get_south_south_connection(
                        current_tile, new_cube, cubes[current_cube]
                    )


def invert_tiles(current, next, current_tile):
    index = len(current) - 1
    for tile in current:
        if tile == current_tile:
            return next[index]
        index -= 1


def match_tiles(current, next, current_tile):
    for (index, tile) in enumerate(current):
        if tile == current_tile:
            return next[index]


def get_north_east_connection(
    current_tile, new_cube: set[tuple[int, int]], current_cube: set[tuple[int, int]]
):
    top_of_current = get_top_row(current_cube)
    leftmost_of_next = get_bottom_column(new_cube)
    return (
        match_tiles(top_of_current, leftmost_of_next, current_tile),  # verified both
        CardinalDirections.East,
    )


def get_south_west_connection(
    current_tile, new_cube: set[tuple[int, int]], current_cube: set[tuple[int, int]]
):
    bottom_of_current = get_bottom_row(current_cube)
    rightmost_of_next = get_top_column(new_cube)
    return (
        match_tiles(bottom_of_current, rightmost_of_next, current_tile),  # verified
        CardinalDirections.West,
    )


def get_east_north_connection(
    current_tile, new_cube: set[tuple[int, int]], current_cube: set[tuple[int, int]]
):
    rightmost_of_current = get_top_column(current_cube)
    bottom_of_next = get_bottom_row(new_cube)
    return (
        match_tiles(
            rightmost_of_current, bottom_of_next, current_tile
        ),  # both verified
        CardinalDirections.North,
    )


def get_west_east_connection(
    current_tile, new_cube: set[tuple[int, int]], current_cube: set[tuple[int, int]]
):
    leftmost_of_current = get_bottom_column(current_cube)
    leftmost_of_next = get_bottom_column(new_cube)
    return (
        invert_tiles(
            leftmost_of_current, leftmost_of_next, current_tile
        ),  # verified both
        CardinalDirections.East,
    )


def get_east_west_connection(
    current_tile, new_cube: set[tuple[int, int]], current_cube: set[tuple[int, int]]
):
    rightmost_of_current = get_top_column(current_cube)
    rightmost_of_next = get_top_column(new_cube)
    return (
        invert_tiles(
            rightmost_of_current, rightmost_of_next, current_tile
        ),  # both verified
        CardinalDirections.West,
    )


def get_north_north_connection(
    current_tile, new_cube: set[tuple[int, int]], current_cube: set[tuple[int, int]]
):
    top_of_current = get_top_row(current_cube)
    bottom_of_next = get_bottom_row(new_cube)
    return (
        match_tiles(top_of_current, bottom_of_next, current_tile),  # verified
        CardinalDirections.North,
    )


def get_south_south_connection(
    current_tile, new_cube: set[tuple[int, int]], current_cube: set[tuple[int, int]]
):
    bottom_of_current = get_bottom_row(current_cube)
    top_of_next = get_top_row(new_cube)
    return (
        match_tiles(bottom_of_current, top_of_next, current_tile),
        CardinalDirections.South,
    )


def get_west_south_connection(
    current_tile, new_cube: set[tuple[int, int]], current_cube: set[tuple[int, int]]
):
    leftmost_of_current = get_bottom_column(current_cube)
    top_of_next = get_top_row(new_cube)
    return (
        match_tiles(leftmost_of_current, top_of_next, current_tile),  # both verified
        CardinalDirections.South,
    )


def get_top_column(cube):
    highest_x = max(cube, key=lambda x: x[0])[0]
    top_column = sorted([x for x in cube if x[0] == highest_x])
    return top_column


def get_bottom_column(cube):
    lowest_x = min(cube, key=lambda x: x[0])[0]
    bottom_column = sorted([x for x in cube if x[0] == lowest_x])
    return bottom_column


def get_top_row(cube):
    lowest_y = min(cube, key=lambda x: x[1])[1]
    top_row = sorted([x for x in cube if x[1] == lowest_y])
    return top_row


def get_bottom_row(cube):
    highest_y = max(cube, key=lambda x: x[1])[1]
    top_row = sorted([x for x in cube if x[1] == highest_y])
    return top_row


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


def read_input(filename, cube_size):
    with open(filename, encoding="utf8") as input_file:
        lines = input_file.read().splitlines()
        open_tiles = set()
        walls = set()
        off_the_map = set()
        cubes = [
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
        ]

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
                if (x, y) not in off_the_map:
                    if y in range(0, 50) and x in range(50, 100):
                        cubes[0].add((x, y))
                    elif y in range(0, 50) and x in range(100, 150):
                        cubes[1].add((x, y))
                    elif y in range(50, 100) and x in range(50, 100):
                        cubes[2].add((x, y))
                    elif y in range(100, 150) and x in range(0, 50):
                        cubes[3].add((x, y))
                    elif y in range(100, 150) and x in range(50, 100):
                        cubes[4].add((x, y))
                    else:
                        cubes[5].add((x, y))

        command_line = lines[-1]
        command_line = command_line.replace("L", ",L,")
        command_line = command_line.replace("R", ",R,")
        commands = command_line.split(",")
        commands.reverse()
        return (starting_pos, open_tiles, walls, off_the_map, commands, cubes)


if __name__ == "__main__":
    pt1_dt = read_input("input.txt", 50)
    main(pt1_dt, is_cube=False)
    pt2_dt = read_input("input.txt", 50)
    main(pt2_dt, is_cube=True)
