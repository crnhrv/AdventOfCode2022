def main(valves: dict[str, tuple[int, list[str]]]):
    current_position = "AA"
    current_flow = 0
    ans1 = 0
    minutes = 1
    while minutes <= 30:
        ans1 += current_flow
        best_option = calculate_best_option(valves, current_position)
        if current_position == best_option:
            valve_flow = valves[current_position][0]
            current_flow += valve_flow
            valves[current_position] = (0, valves[current_position][1])
        else:
            current_position = score_paths_from_here(valves, current_position)
        minutes += 1
    print(ans1)


def calculate_best_option(valves, current_position):
    valves = dict([kvp for kvp in valves.items()])
    for key in valves.keys():
        valve = valves[key]
        valves[key] = (valve[0] * 1000, valve[1])

    ranking = naive_ranking(current_position, valves, 1, {}, set())
    best_option = max(ranking.items(), key=lambda x: x[1])
    return best_option[0]


def score_paths_from_here(
    valves: dict[str, tuple[int, list[str]]],
    current_position,
):
    path_list = [[current_position]]
    path_index = 0
    seen = {current_position}

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_valve = current_path[-1]
        next_tunnels = valves[last_valve][1]
        for next_node in next_tunnels:
            if not next_node in seen:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                seen.add(next_node)
        path_index += 1

    scores = []
    for path in path_list:
        score = 0
        distance = 1
        for valve in path[1:]:
            score += valves[valve][0] // distance
            distance += 1
        scores.append(score)

    zipped = sorted(zip(scores, path_list), key=lambda x: x[0], reverse=True)
    for pair in zipped:
        if pair[0] == 0:
            return pair[1][0]
        return pair[1][1]


def naive_ranking(current, valves, distance=1, ranking={}, seen=set()):
    if current in seen:
        return ranking

    seen.add(current)

    ranking[current] = valves[current][0] // distance

    for tunnel in [x for x in valves[current][1] if x not in seen]:
        naive_ranking(tunnel, valves, distance + 1, ranking, seen)
    return ranking


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
    dt = read_input("test-input.txt")
    main(dt)
