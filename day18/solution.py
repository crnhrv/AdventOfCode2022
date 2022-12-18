class Cube:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"({self.x},{self.y},{self.z})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self) -> str:
        return f"{self}"


def main(cubes: list[Cube]):
    total = 6 * len(cubes)
    for (i, cube_a) in enumerate(cubes):
        for cube_b in cubes[i + 1 :]:
            if (
                abs(cube_a.x - cube_b.x)
                + abs(cube_a.y - cube_b.y)
                + abs(cube_a.z - cube_b.z)
                == 1
            ):
                total -= 2

    print(total)

    min_x_cube = min(cubes, key=lambda x: x.x)
    max_x_cube = max(cubes, key=lambda x: x.x)

    min_y_cube = min(cubes, key=lambda x: x.y)
    max_y_cube = max(cubes, key=lambda x: x.y)

    min_z_cube = min(cubes, key=lambda x: x.z)
    max_z_cube = max(cubes, key=lambda x: x.z)

    minmaxes = (
        (min_x_cube.x, max_x_cube.x),
        (min_y_cube.y, max_y_cube.y),
        (min_z_cube.z, max_z_cube.z),
    )

    deltas = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

    all_cubes = set([(x.x, x.y, x.z) for x in cubes])
    ans = 0
    for cube in cubes:
        for delta in deltas:
            test_cube = (cube.x + delta[0], cube.y + delta[1], cube.z + delta[2])
            if is_surface_cube(test_cube, minmaxes, all_cubes, deltas):
                ans += 1
    print(ans)


def is_surface_cube(cube, minmaxes, all_cubes, deltas):
    (x, y, z) = cube
    seen = set()
    stack = [(x, y, z)]
    while stack:
        (x, y, z) = stack.pop()
        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))
        if (
            x < minmaxes[0][0]
            or x > minmaxes[0][1]
            or x < minmaxes[1][0]
            or x > minmaxes[1][1]
            or x < minmaxes[2][0]
            or x > minmaxes[2][1]
        ):
            return True
        if (x, y, z) not in all_cubes:
            for delta in deltas:
                test_cube = (x + delta[0], y + delta[1], z + delta[2])
                stack.append(test_cube)

    return False


def read_input(filename):
    cubes = []
    with open(filename, encoding="utf8") as f:
        cubes_coords = f.read().splitlines()
        for coords in cubes_coords:
            (x, y, z) = [int(x) for x in coords.split(",")]
            cubes.append(Cube(x, y, z))
    return cubes


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
