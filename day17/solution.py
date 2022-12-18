class Cave:
    def __init__(self):
        self.grid = []
        self.rock_index = 0
        self.jet_index = 0
        self.width = 7
        self.starting_depth = 4
        self.rock_spawn = 0
        self.rock_count = 0

    def build(self):
        self.grid = [
            ["." for _ in range(self.width)] for _ in range(self.starting_depth)
        ]
        return self


class Rock:
    def __init__(self, shape: str, width: int, height: int, position: tuple[int, int]):
        self.width = width
        self.height = height
        self.shape = shape
        self.bl_edge = position

    def get_tl_edge(self):
        match self.shape:
            case "-":
                return self.bl_edge
            case "+":
                return (self.bl_edge[0] - 2, self.bl_edge[1])
            case "」":
                return (self.bl_edge[0] - 2, self.bl_edge[1] + 2)
            case "|":
                return (self.bl_edge[0] - 3, self.bl_edge[1])
            case "■":
                return (self.bl_edge[0] - 1, self.bl_edge[1])


def drop_rocks(jets, search_range, cave=None):
    rocks = ["-", "+", "」", "|", "■"]
    if not cave:
        cave = Cave().build()
    while cave.rock_count < search_range:
        rock = spawn_rock(rocks[cave.rock_index], cave.rock_spawn, 2)
        rock_is_moving = True
        while rock_is_moving:
            jet = jets[cave.jet_index]
            cave.jet_index = (cave.jet_index + 1) % len(jets)
            jet_blast_rock(rock, jet, cave.grid)
            rock_is_moving = try_move_rock_down(rock, cave.grid)
        tl_edge = rock.get_tl_edge()
        cave.rock_count += 1
        cave.rock_index = (cave.rock_index + 1) % len(rocks)
        if tl_edge[0] - 4 <= 0:
            add_depth_to_cave(cave, abs(tl_edge[0] - 4), cave.width)

    return cave


def add_depth_to_cave(cave: list[list[str]], extra_depth, width):
    for _ in range(extra_depth):
        cave.grid.insert(0, ["." for _ in range(width)])


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
                rightmost_edge = rock.bl_edge[1] + (rock.width - 1)
                if (
                    rightmost_edge + 1 < len(cave[0])
                    and cave[rock.bl_edge[0]][rightmost_edge + 1] == "."
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.bl_edge[1]
                if (
                    leftmost_edge - 1 >= 0
                    and cave[rock.bl_edge[0]][leftmost_edge - 1] == "."
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] - 1,
                    )
        case "+":
            if jet == ">":
                rightmost_edge = rock.bl_edge[1] + 1
                if rightmost_edge + 1 < len(cave[0]) and (
                    rock.bl_edge[0] - 1 < 0
                    or (
                        cave[rock.bl_edge[0] - 1][rightmost_edge + 1] == "."
                        and cave[rock.bl_edge[0]][rock.bl_edge[1] + 1] == "."
                    )
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.bl_edge[1] - 1
                if leftmost_edge - 1 >= 0 and (
                    rock.bl_edge[0] - 1 < 0
                    or (
                        cave[rock.bl_edge[0] - 1][leftmost_edge - 1] == "."
                        and cave[rock.bl_edge[0]][rock.bl_edge[1] - 1] == "."
                    )
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] - 1,
                    )
        case "」":
            if jet == ">":
                rightmost_edge = rock.bl_edge[1] + (rock.width - 1)
                if (
                    rightmost_edge + 1 < len(cave[0])
                    and cave[rock.bl_edge[0]][rightmost_edge + 1] == "."
                    and (
                        rock.bl_edge[0] - 2 < 0
                        or (
                            cave[rock.bl_edge[0] - 1][rightmost_edge + 1] == "."
                            and cave[rock.bl_edge[0] - 2][rightmost_edge + 1] == "."
                        )
                    )
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.bl_edge[1]
                if (
                    leftmost_edge - 1 >= 0
                    and cave[rock.bl_edge[0]][leftmost_edge - 1] == "."
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] - 1,
                    )
        case "|":
            if jet == ">":
                rightmost_edge = rock.bl_edge[1]
                if (
                    rightmost_edge + 1 < len(cave[0])
                    and cave[rock.bl_edge[0]][rightmost_edge + 1] == "."
                ) and (
                    rock.bl_edge[0] - 3 < 0
                    or (
                        cave[rock.bl_edge[0] - 1][rightmost_edge + 1] == "."
                        and cave[rock.bl_edge[0] - 2][rightmost_edge + 1] == "."
                        and cave[rock.bl_edge[0] - 3][rightmost_edge + 1] == "."
                    )
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.bl_edge[1]
                if (
                    leftmost_edge - 1 >= 0
                    and cave[rock.bl_edge[0]][leftmost_edge - 1] == "."
                ) and (
                    rock.bl_edge[0] - 3 < 0
                    or (
                        cave[rock.bl_edge[0] - 1][leftmost_edge - 1] == "."
                        and cave[rock.bl_edge[0] - 2][leftmost_edge - 1] == "."
                        and cave[rock.bl_edge[0] - 3][leftmost_edge - 1] == "."
                    )
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] - 1,
                    )
        case "■":
            if jet == ">":
                rightmost_edge = rock.bl_edge[1] + 1
                if rightmost_edge + 1 < len(cave[0]) and (
                    rock.bl_edge[0] - 1 < 0
                    or (
                        cave[rock.bl_edge[0]][rightmost_edge + 1] == "."
                        and cave[rock.bl_edge[0] - 1][rightmost_edge + 1] == "."
                    )
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] + 1,
                    )
            else:
                leftmost_edge = rock.bl_edge[1]
                if leftmost_edge - 1 >= 0 and (
                    rock.bl_edge[0] < 1 > 0
                    or (
                        cave[rock.bl_edge[0]][leftmost_edge - 1] == "."
                        and cave[rock.bl_edge[0] - 1][leftmost_edge - 1] == "."
                    )
                ):
                    rock.bl_edge = (
                        rock.bl_edge[0],
                        rock.bl_edge[1] - 1,
                    )


def try_move_rock_down(rock: Rock, cave: list[list[str]]):
    match rock.shape:
        case "-":
            (row, col) = rock.bl_edge
            if (
                row + 1 >= len(cave)
                or cave[row + 1][col] != "."
                or cave[row + 1][col + 1] != "."
                or cave[row + 1][col + 2] != "."
                or cave[row + 1][col + 3] != "."
            ):
                for i in range(rock.width):
                    cave[row][col + i] = "#"
                return False
            rock.bl_edge = (row + 1, col)
            return True
        case "+":
            (row, col) = rock.bl_edge
            if (
                row + 1 >= len(cave)
                or cave[row + 1][col] != "."
                or cave[row][col - 1] != "."
                or cave[row][col + 1] != "."
            ):
                cave[row][col] = "#"
                cave[row - 1][col] = "#"
                cave[row - 2][col] = "#"
                cave[row - 1][col - 1] = "#"
                cave[row - 1][col + 1] = "#"
                return False
            rock.bl_edge = (row + 1, col)
            return True
        case "」":
            (row, col) = rock.bl_edge
            if (
                row + 1 >= len(cave)
                or cave[row + 1][col] != "."
                or cave[row + 1][col + 1] != "."
                or cave[row + 1][col + 2] != "."
            ):
                for i in range(rock.width):
                    cave[row][col + i] = "#"

                cave[row - 1][col + 2] = "#"
                cave[row - 2][col + 2] = "#"
                return False
            rock.bl_edge = (row + 1, col)
            return True
        case "|":
            (row, col) = rock.bl_edge
            if row + 1 >= len(cave) or cave[row + 1][col] != ".":
                for i in range(rock.height):
                    cave[row - i][col] = "#"
                return False
            rock.bl_edge = (row + 1, col)
            return True
        case "■":
            (row, col) = rock.bl_edge
            if (
                row + 1 >= len(cave)
                or cave[row + 1][col] != "."
                or cave[row + 1][col + 1] != "."
            ):
                cave[row][col] = "#"
                cave[row][col + 1] = "#"
                cave[row - 1][col] = "#"
                cave[row - 1][col + 1] = "#"
                return False
            rock.bl_edge = (row + 1, col)
            return True
    return True


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return list(f.read())


def print_cave(cave):
    for (r, row) in enumerate(cave):
        print("|", end="")
        for (c, area) in enumerate(row):
            print(area, end="")
        print("|")
    print("I" + "-" * len(cave[0]) + "I")


if __name__ == "__main__":
    dt = read_input("test-input.txt")
    print(len(drop_rocks(dt, 20000).grid) - 4)  # ans1
