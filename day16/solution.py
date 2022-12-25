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

    stack = []

    def find_score(
        minute,
        tunnel,
        pressure_released,
        current_flow,
        opened_valves,
        max_mins,
        seen,
        stack_phase,
    ):
        if minute > max_mins:
            if stack_phase:
                stack.append((pressure_released, opened_valves))
                return pressure_released
            else:
                return pressure_released

        key = (
            minute,
            current_flow,
            tunnel,
        )
        if key in seen:
            return 0

        seen.add(key)

        best = pressure_released

        valve = valves[tunnel]
        available_tunnels = valve[1]

        best = 0

        if tunnel not in opened_valves and valve[0] > 0:
            new_opened_valves = opened_valves.copy()
            new_opened_valves.add(tunnel)
            best = max(
                find_score(
                    minute + 1,
                    tunnel,
                    pressure_released + current_flow,
                    current_flow + valve[0],
                    new_opened_valves,
                    max_mins,
                    seen,
                    stack_phase,
                ),
                best,
            )

        for tunnel in available_tunnels:
            best = max(
                find_score(
                    minute + 1,
                    tunnel,
                    pressure_released + current_flow,
                    current_flow,
                    opened_valves,
                    max_mins,
                    seen,
                    stack_phase,
                ),
                best,
            )

        return best

    if mins == 30:
        return find_score(
            1,
            "AA",
            0,
            0,
            set(),
            mins,
            set(),
            False,
        )
    else:
        find_score(
            1,
            "AA",
            0,
            0,
            set(),
            mins,
            set(),
            True,
        )

    ans2 = 0
    stack = [x for x in stack]
    while stack:
        elephant_score = 0
        (human_score, opened_valves) = stack.pop()
        if human_score * 2 < ans2:
            continue
        elephant_score = find_score(
            1,
            "AA",
            0,
            0,
            opened_valves.copy(),
            mins,
            set(),
            False,
        )
        if elephant_score + human_score > ans2:
            ans2 = elephant_score + human_score

    return ans2


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
    pt1_dt = read_input("input.txt")
    p1(pt1_dt)
    pt2_dt = read_input("input.txt")
    p2(pt2_dt)
