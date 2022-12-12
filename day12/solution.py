from pprint import pprint

import dijkstar


def main(terrain_map):
    start, end = (0, 0)
    graph = dijkstar.Graph()
    starting_points = []
    for (i, chars) in enumerate(terrain_map):
        for (j, char) in enumerate(chars):
            if char == "a":
                starting_points.append((i, j))
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
            if i < len(terrain_map) - 1 and can_move_between(char, terrain_map[i + 1][j]):
                graph.add_edge((i, j), (i + 1, j), 1)
            if i >= 1 and can_move_between(char, terrain_map[i - 1][j]):
                graph.add_edge((i, j), (i - 1, j), 1)
            if j < len(chars) - 1 and can_move_between(char, chars[j + 1]):
                graph.add_edge((i, j), (i, j + 1), 1)
            if j >= 1 and can_move_between(char, chars[j - 1]):
                graph.add_edge((i, j), (i, j - 1), 1)

    path = dijkstar.find_path(graph, start, end)
    print(path.total_cost)

    ans2 = path.total_cost
    for starting_point in starting_points:
        try:
            ans2 = min(ans2, dijkstar.find_path(graph, starting_point, end).total_cost)
        except dijkstar.NoPathError:
            continue
    print(ans2)


def can_move_between(a, b):
    if a == "S":
        a = "a"
    if b == "S":
        a = "a"
    if b == "E":
        b = "z"
    if a == "E":
        a = "z"
    return ord(b) <= ord(a) or ord(b) - ord(a) == 1


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return [list(x) for x in f.read().splitlines()]


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
