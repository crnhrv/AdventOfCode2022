def main(cubes: list[tuple[int, int, int]]):
    total = 6 * len(cubes)
    for (i, cube_a) in enumerate(cubes):
        for cube_b in cubes[i + 1 :]:
            if (
                abs(cube_a[0] - cube_b[0])
                + abs(cube_a[1] - cube_b[1])
                + abs(cube_a[2] - cube_b[2])
                == 1
            ):
                total -= 2

    print(total)

    all_cubes = set(cubes)
    deltas = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    min_x_cube = min(cubes, key=lambda x: x[0])
    max_x_cube = max(cubes, key=lambda x: x[0])
    ans = 0
    for cube in cubes:
        for delta in deltas:
            test_cube = (cube[0] + delta[0], cube[1] + delta[1], cube[2] + delta[2])
            if is_surface_cube(
                test_cube, (min_x_cube[0], max_x_cube[0]), all_cubes, deltas
            ):
                ans += 1
    print(ans)


def is_surface_cube(cube, minmax, all_cubes, deltas):
    (x, y, z) = cube
    seen = set()
    stack = [(x, y, z)]
    while stack:
        (x, y, z) = stack.pop()
        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))
        if x < minmax[0] or x > minmax[1]:
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
            cubes.append((x, y, z))
    return cubes


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
