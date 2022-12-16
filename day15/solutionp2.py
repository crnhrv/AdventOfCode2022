class Sensor:
    def __init__(self, coords: tuple[int, int], beacon: tuple[int, int]) -> None:
        self.position = coords
        self.closest_beacon = beacon
        self.minmax_for_col_per_row = {}
        self.max_row_val_per_col = {}
        self.distance = 0

    def __str__(self) -> str:
        return f"s={self.position}/cb={self.closest_beacon}"

    def __repr__(self) -> str:
        return f"{self}"


def main(sensors: list[Sensor], row, max_pos=10_000_000):
    beacon_pos = set()
    sensor_pos = set()
    ranges_per_row = {}
    ranges_per_col = {}
    for sensor in sensors:
        if sensor.position[1] == row:
            sensor_pos.add(sensor.position[0])
        if sensor.closest_beacon[1] == row:
            beacon_pos.add(sensor.closest_beacon[0])
        distance = calculate_distance(sensor.position, sensor.closest_beacon)
        sensor.distance = distance
        sensor.minmax_for_col_per_row = get_col_values_for_rows(
            sensor.position, distance, max_pos
        )
        sensor.max_row_val_per_col = get_row_values_for_cols(
            sensor.position, distance, max_pos
        )

        for (k, v) in sensor.minmax_for_col_per_row.items():
            if k in ranges_per_row:
                ranges_per_row[k].append(v)
            else:
                ranges_per_row[k] = [v]

        for (k, v) in sensor.max_row_val_per_col.items():
            if k in ranges_per_col:
                ranges_per_col[k].append(v)
            else:
                ranges_per_col[k] = [v]

    for i in range(0, max_pos):
        ranges_per_row[i] = sorted(ranges_per_row[i])
        ranges_per_col[i] = sorted(ranges_per_col[i])

    for col in ranges_per_col.keys():
        row_ranges = ranges_per_col[col]
        potential_range = []
        i = 1
        prev_min = 0
        prev_max = row_ranges[0][1]
        if row_ranges[0][0] > prev_min:
            potential_range.append((0, row_ranges[0][0]))
        while i < len(row_ranges):
            cur = row_ranges[i]
            if prev_max < cur[0]:
                potential_range.append((prev_max + 1, cur[0]))
                prev_min = cur[0]
                prev_max = cur[1]
            if prev_min >= cur[0]:
                i += 1
                continue
            if prev_max >= cur[0] - 1:
                prev_max = max(prev_max, cur[1])
                i += 1
                continue
            if prev_max < cur[0]:
                potential_range.append((prev_max + 1, cur[0]))
                prev_min = cur[0]
                prev_max = cur[1]

            i += 1
        if prev_max < max_pos:
            potential_range.append((prev_max, max_pos))

        ranges_per_col[col] = potential_range

    for row in ranges_per_row.keys():
        col_ranges = ranges_per_row[row]
        potential_range = []
        i = 1
        prev_min = 0
        prev_max = col_ranges[0][1]
        if col_ranges[0][0] > prev_min:
            potential_range.append((0, col_ranges[0][0]))
        while i < len(col_ranges):
            cur = col_ranges[i]
            if prev_max < cur[0]:
                potential_range.append((prev_max + 1, cur[0]))
                prev_min = cur[0]
                prev_max = cur[1]
            if prev_min >= cur[0]:
                i += 1
                continue
            if prev_max >= cur[0] - 1:
                prev_max = max(prev_max, cur[1])
                i += 1
                continue
            if prev_max < cur[0]:
                potential_range.append((prev_max + 1, cur[0]))
                prev_min = cur[0]
                prev_max = cur[1]

            i += 1
        if prev_max < max_pos:
            potential_range.append((prev_max, max_pos))
        ranges_per_row[row] = potential_range
    start_x = 0
    for y in range(0, max_pos):
        x_ranges = ranges_per_row[y]
        for range_ in x_ranges:
            for x in range(max(range_[0], start_x), range_[1]):
                out_of_range = True
                for sensor in sensors:
                    if calculate_distance((x, y), sensor.position) <= sensor.distance:
                        out_of_range = False
                if out_of_range:
                    print(x * 4000000 + y)
                    exit()
            start_x = max(start_x, range_[1])


def get_col_values_for_rows(cur, dis, max_y):
    maxes = {}
    starting_x = cur[0]
    starting_y = cur[1]

    left_x = starting_x - dis
    right_x = starting_x + dis
    count = 0
    for i in range(starting_y, starting_y - dis - 1, -1):
        l_range = max(0, min(left_x, right_x))
        r_range = min(max_y, max(left_x, right_x))
        if i >= 0 and i <= max_y:
            maxes[i] = (l_range, r_range)
        other_i = min(starting_y, max_y) + count
        if other_i >= 0 and other_i <= max_y:
            maxes[min(starting_y, max_y) + count] = (l_range, r_range)

        if (i <= 0 or i >= max_y) and (other_i <= 0 or other_i >= max_y):
            break
        left_x += 1
        right_x -= 1
        count += 1

    return maxes


def get_row_values_for_cols(cur, dis, max_x):
    maxes = {}
    starting_x = cur[0]
    starting_y = cur[1]

    up_y = starting_y - dis
    down_y = starting_y + dis
    count = 0
    for i in range(starting_x, starting_x - dis - 1, -1):
        l_range = max(0, min(up_y, down_y))
        r_range = min(max_x, max(up_y, down_y))

        if i >= 0 and i <= max_x:
            maxes[i] = (l_range, r_range)
        other_i = min(starting_x, max_x) + count
        if other_i >= 0 and other_i <= max_x:
            maxes[other_i] = (l_range, r_range)
        if (i <= 0 or i >= max_x) and (other_i <= 0 or other_i >= max_x):
            break

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
    main(dt, 0, 4000000)  # ans1
