class Sensor:
    def __init__(self, coords: tuple[int, int], beacon: tuple[int, int]) -> None:
        self.position = coords
        self.closest_beacon = beacon
        self.max_x_value_per_y = {}
        self.max_y_value_per_x = {}

    def __str__(self) -> str:
        return f"s={self.position}/cb={self.closest_beacon}"

    def __repr__(self) -> str:
        return f"{self}"


def main(sensors: list[Sensor], row):
    beacon_pos = set()
    sensor_pos = set()
    for sensor in sensors:
        if sensor.position[1] == row:
            sensor_pos.add(sensor.position[0])
        if sensor.closest_beacon[1] == row:
            beacon_pos.add(sensor.closest_beacon[0])
        distance = calculate_distance(sensor.position, sensor.closest_beacon)
        sensor.max_x_value_per_y = get_x_values_for_ys(sensor.position, distance)
        sensor.max_y_value_per_x = get_y_values_for_xs(sensor.position, distance)

    no_beacon = set()

    for sensor in sensors:
        if row in sensor.max_x_value_per_y:
            (l, r) = sensor.max_x_value_per_y[row]
            for i in range(l, r):
                no_beacon.add(i)
        for i in sensor.max_y_value_per_x.keys():
            (l, r) = sensor.max_y_value_per_x[i]
            if l <= row and r >= row:
                no_beacon.add(i)

    print(len(no_beacon) - len(sensor_pos) - len(beacon_pos))


def get_x_values_for_ys(cur, dis):
    maxes = {}
    starting_x = cur[0]
    starting_y = cur[1]

    left_x = starting_x - dis
    right_x = starting_x + dis
    count = 0
    for _ in range(starting_y, starting_y - dis, -1):
        maxes[starting_y - count] = (left_x, right_x)
        maxes[starting_y + count] = (left_x, right_x)
        left_x += 1
        right_x -= 1
        count += 1
    return maxes


def get_y_values_for_xs(cur, dis):
    maxes = {}
    starting_x = cur[0]
    starting_y = cur[1]

    up_y = starting_y - dis
    down_y = starting_y + dis
    count = 0
    for _ in range(starting_x, starting_x - dis, -1):
        maxes[starting_x - count] = (up_y, down_y)
        maxes[starting_x + count] = (up_y, down_y)
        up_y += 1
        down_y -= 1
        count += 1

    return maxes


def calculate_distance(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def read_input(filename):
    sensors = []
    with open(filename, encoding="utf8") as f:
        lines = f.read().splitlines()
        for line in lines:
            (sensor, beacon) = line.split(":")
            sensor_parts = sensor.split(" ")
            x_part = sensor_parts[2].split("=")
            y_part = sensor_parts[3].split("=")
            sensor_pos = (int(x_part[1].removesuffix(",")), int(y_part[1]))

            beacon_parts = beacon.split(" ")
            x_part = beacon_parts[-2].split("=")
            y_part = beacon_parts[-1].split("=")
            beacon_pos = (int(x_part[1].removesuffix(",")), int(y_part[1]))

            sensors.append(Sensor(sensor_pos, beacon_pos))
    return sensors


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt, 2000000)
