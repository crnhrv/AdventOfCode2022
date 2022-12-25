import collections


def p1(data):
    ans1 = get_max_blueprint_score(data, 30)
    print(ans1)


def p2(data):
    ans1 = get_max_blueprint_score(data, 26)
    print(ans1)


def get_max_blueprint_score(data, mins):
    minute = 0
    valves = data

    def find_max_score(
        minute,
        tunnel,
        pressure_released,
        current_flow,
        opened_valves,
        max_mins,
        visited_count,
        seen,
    ):
        if minute > max_mins:
            return pressure_released

        key = (
            minute,
            current_flow,
            tunnel,
        )
        if key in seen:
            return 0

        if minute > 3 and current_flow == 0:
            return 0

        if visited_count[tunnel] > 2:
            return 0

        seen.add(key)

        best = pressure_released

        valve = valves[tunnel]
        available_tunnels = valve[1]

        if tunnel not in opened_valves and valve[0] > 0:
            new_opened_valves = opened_valves.copy()
            new_opened_valves.add(tunnel)
            best = max(
                find_max_score(
                    minute + 1,
                    tunnel,
                    pressure_released + current_flow,
                    current_flow + valve[0],
                    new_opened_valves,
                    max_mins,
                    visited_count,
                    seen,
                ),
                best,
            )

        for tunnel in available_tunnels:
            new_visited_count = visited_count.copy()
            new_visited_count[tunnel] += 1
            best = max(
                find_max_score(
                    minute + 1,
                    tunnel,
                    pressure_released + current_flow,
                    current_flow,
                    opened_valves,
                    max_mins,
                    new_visited_count,
                    seen,
                ),
                best,
            )

        return best

    best_score = find_max_score(
        minute + 1, "AA", 0, 0, set(), mins, collections.defaultdict(int), set()
    )
    return best_score


def read_input(filename):
    data = {}
    with open(filename, encoding="utf8") as f:
        lines = f.read().splitlines()
        for line in lines:
            (left, right) = line.split(";")
            valve = left.split(" ")[1]
            flow_rate = int(left.split("=")[1])

            right = right.replace(",", "")
            tunnels = right.split(" ")[5:]
            data[valve] = (flow_rate, tunnels)
    return data


if __name__ == "__main__":
    dt = read_input("input.txt")
    p1(dt)
