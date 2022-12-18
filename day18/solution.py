class Cube:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"({self.x},{self.y},{self.z})"

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
