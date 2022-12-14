import os
import time


class CaveDimensions:
    def __init__(self, max_height, max_width, min_width, min_height) -> None:
        self.max_height = max_height
        self.max_width = max_width
        self.min_width = min_width
        self.min_height = min_height

    def actual_height(self) -> int:
        return self.max_height - self.min_height

    def actual_width(self) -> int:
        return self.max_width - self.min_width


class Cave:
    def __init__(self, dimensions: CaveDimensions, grid: list[list]) -> None:
        self.dimensions = dimensions
        self.grid = grid

    def get_sand_start(self) -> tuple[int, int]:
        sand_start_col = self.dimensions.actual_width() - (
            self.dimensions.max_width - 500
        )
        stand_start_row = self.dimensions.min_height
        return (stand_start_row, sand_start_col)


def main(paths):
    min_width = 1000
    max_width = 0
    max_height = 0
    min_height = 0
    for line in paths:
        for (width, height) in line:
            max_width = max(width, max_width)
            min_width = min(width, min_width)
            max_height = max(height, max_height)

    dimensions = CaveDimensions(max_height, max_width, min_width, min_height)
    cave = setup_empty_cave(dimensions)
    add_cave_walls(cave, paths)
    collected = False
    while not collected:
        (r, c) = cave.get_sand_start()
        collected = drop_sand(cave, r, c)

    print(count_collected(cave))


def count_collected(cave: Cave):
    sand = 0
    for row in cave.grid:
        for col in row:
            if col == "o":
                sand += 1
    return sand


def drop_sand(cave: Cave, r, c):
    while True:
        if r < 0 or r > len(cave.grid) - 2 or c > len(cave.grid[0]) - 2 or c < 0:
            return True
        if cave.grid[r + 1][c] == "o" or cave.grid[r + 1][c] == "#":
            if cave.grid[r + 1][c - 1] == ".":
                return drop_sand(cave, r + 1, c - 1)
            if cave.grid[r + 1][c + 1] == ".":
                return drop_sand(cave, r + 1, c + 1)
            cave.grid[r][c] = "o"
            break
        if cave.grid[r + 1][c] == "#":
            cave.grid[r][c] = "o"
            break
        else:
            r += 1
    return False


def setup_empty_cave(dimensions: CaveDimensions) -> Cave:
    grid = [
        ["." for _ in range(dimensions.actual_width() + 1)]
        for _ in range(dimensions.actual_height() + 1)
    ]

    cave = Cave(dimensions, grid)
    (r, c) = cave.get_sand_start()
    cave.grid[r][c] = "+"
    return cave


def add_cave_walls(cave: Cave, paths):
    for line in paths:
        for (i, coords) in enumerate(line[1:]):
            (start_col, start_row) = line[(i + 1) - 1]
            (end_col, end_row) = coords
            horizontal_start = cave.dimensions.actual_width() - (
                cave.dimensions.max_width - start_col
            )
            horizontal_end = cave.dimensions.actual_width() - (
                cave.dimensions.max_width - end_col
            )
            vertical_start = cave.dimensions.actual_height() - (
                cave.dimensions.max_height - start_row
            )
            vertical_end = cave.dimensions.actual_height() - (
                cave.dimensions.max_height - end_row
            )

            if horizontal_start != horizontal_end:
                add_walls_horizontally(
                    cave, horizontal_start, horizontal_end, vertical_start
                )
            else:
                add_walls_vertically(
                    cave, vertical_start, vertical_end, horizontal_start
                )


def add_walls_horizontally(cave, horizontal_start, horizontal_end, r):
    delta = 0
    if horizontal_start > horizontal_end:
        delta = -1
    else:
        delta = 1
    i = horizontal_start
    while i != horizontal_end + delta:
        cave.grid[r][i] = "#"
        i += delta


def add_walls_vertically(cave, vertical_start, vertical_end, c):
    delta = 0
    if vertical_start > vertical_end:
        delta = -1
    else:
        delta = 1
    i = vertical_start
    while i != vertical_end + delta:
        cave.grid[i][c] = "#"
        i += delta


def print_cave(cave: Cave):
    for row in cave.grid:
        for item in row:
            print(item, end="")
        print()


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        paths = []
        lines = f.read().splitlines()
        for path_line in lines:
            paths.append([eval(x) for x in path_line.split(" -> ")])
    return paths


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
