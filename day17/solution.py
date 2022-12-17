class Rock:
    def __init__(self, shape: str, width: int, height: int, position: tuple[int, int]):
        self.width = width
        self.height = height
        self.shape = shape
        self.current_bottom_edge = position


def main(jets):
    rock_index = 0
    rock_count = 0
    jet_index = 0
    highest_rock = 0
    rocks = ["-", "+", "」", "|", "■"]
    cave = create_cave(width=7, starting_depth=4)
    print_cave(cave)
    while rock_count < 2022:
        rock = spawn_rock(rocks[rock_index], highest_rock + 3, 2)
        print(highest_rock)
        rock_is_moving = True
        even_turn = 0
        while rock_is_moving:
            if even_turn:
                jet = jets[jet_index]
                jet_index = (jet_index + 1) % len(jets)
                jet_blast_rock(rock, jet, cave)
            else:
                rock_is_moving = try_move_rock_down(rock, cave)

            even_turn += 1

        rock_count += 1
        rock_index = (rock_index + 1) % len(rocks)
        highest_rock = max(highest_rock, rock.current_bottom_edge + (rock.height - 1))


def spawn_rock(rock_shape: str, starting_row, starting_col):
    match rock_shape:
        case "-":
            return Rock(
                rock_shape, width=4, height=1, position=(starting_row, starting_col)
            )
        case "+":
            return Rock(
                rock_shape, width=3, height=3, position=(starting_row, starting_col + 1)
            )
        case "」":
            return Rock(
                rock_shape, width=3, height=3, position=(starting_row, starting_col)
            )
        case "|":
            return Rock(
                rock_shape, width=1, height=4, position=(starting_row, starting_col)
            )
        case "■":
            return Rock(
                rock_shape, width=2, height=2, position=(starting_row, starting_col)
            )


def jet_blast_rock(rock: Rock, jet: str, cave: list[list[str]]):
    match rock.shape:
        case "-":
            if jet == ">":
                rightmost_edge = rock.current_bottom_edge[1] + (rock.width - 1)
                if (
                    rightmost_edge + 1 < len(cave[0])
                    and cave[rock.current_bottom_edge[0]][rightmost_edge + 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.current_bottom_edge[1]
                if (
                    leftmost_edge - 1 >= 0
                    and cave[rock.current_bottom_edge[0]][leftmost_edge - 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] - 1,
                    )
        case "+":
            if jet == ">":
                rightmost_edge = rock.current_bottom_edge[1] + 1
                if (
                    rightmost_edge + 1 < len(cave[0])
                    and cave[rock.current_bottom_edge[0] - 1][rightmost_edge + 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.current_bottom_edge[1] - 1
                if (
                    leftmost_edge - 1 >= 0
                    and cave[rock.current_bottom_edge[0] - 1][leftmost_edge - 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] - 1,
                    )
        case "」":
            if jet == ">":
                rightmost_edge = rock.current_bottom_edge[1] + (rock.width - 1)
                if (
                    rightmost_edge + 1 < len(cave[0])
                    and cave[rock.current_bottom_edge[0]][rightmost_edge + 1] == "."
                    and cave[rock.current_bottom_edge[0] - 1][rightmost_edge + 1] == "."
                    and cave[rock.current_bottom_edge[0] - 2][rightmost_edge + 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.current_bottom_edge[1]
                if (
                    leftmost_edge - 1 >= 0
                    and cave[rock.current_bottom_edge[0]][leftmost_edge - 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] - 1,
                    )
        case "|":
            if jet == ">":
                rightmost_edge = rock.current_bottom_edge[1]
                if (
                    rightmost_edge + 1 < len(cave[0])
                    and cave[rock.current_bottom_edge[0]][rightmost_edge + 1] == "."
                    and cave[rock.current_bottom_edge[0] - 1][rightmost_edge + 1] == "."
                    and cave[rock.current_bottom_edge[0] - 2][rightmost_edge + 1] == "."
                    and cave[rock.current_bottom_edge[0] - 3][rightmost_edge + 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.current_bottom_edge[1]
                if (
                    leftmost_edge - 1 >= 0
                    and cave[rock.current_bottom_edge[0]][leftmost_edge - 1] == "."
                    and cave[rock.current_bottom_edge[0] - 1][leftmost_edge - 1] == "."
                    and cave[rock.current_bottom_edge[0] - 2][leftmost_edge - 1] == "."
                    and cave[rock.current_bottom_edge[0] - 3][leftmost_edge - 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] - 1,
                    )
        case "■":
            if jet == ">":
                rightmost_edge = rock.current_bottom_edge[1] + 1
                if (
                    rightmost_edge + 1 < len(cave[0])
                    and cave[rock.current_bottom_edge[0]][rightmost_edge + 1] == "."
                    and cave[rock.current_bottom_edge[0] - 1][rightmost_edge + 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.current_bottom_edge[1]
                if (
                    leftmost_edge - 1 >= 0
                    and cave[rock.current_bottom_edge[0]][leftmost_edge - 1] == "."
                    and cave[rock.current_bottom_edge[0] - 1][leftmost_edge - 1] == "."
                ):
                    rock.current_bottom_edge = (
                        rock.current_bottom_edge[0],
                        rock.current_bottom_edge[1] - 1,
                    )


def try_move_rock_down(rock: Rock, cave: list[list[str]]):
    match rock:
        case "-":
            pass
        case "+":
            pass
        case "」":
            pass
        case "|":
            pass
        case "■":
            pass
    return True


def create_cave(width, starting_depth):
    return [["." for _ in range(width)] for _ in range(starting_depth)]


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return list(f.read())


def print_cave(cave):
    for row in cave:
        print("|", end="")
        for area in row:
            print(area, end="")
        print("|")
    print("I" + "-" * len(cave[0]) + "I")


if __name__ == "__main__":
    dt = read_input("test-input.txt")
    main(dt)
