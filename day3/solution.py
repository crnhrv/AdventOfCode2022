def part1(rucksacks):
    total_priority = 0
    for rucksack in rucksacks:
        container_size = len(rucksack) // 2
        split_containers = [rucksack[container_size:], rucksack[:container_size]]
        duplicate = find_intersection(split_containers)
        total_priority += get_priority(duplicate)
    return total_priority


def part2(rucksacks):
    total_priority = 0
    i = 0

    while i < len(rucksacks):
        badge = find_intersection(rucksacks[i : i + 3])
        total_priority += get_priority(badge)
        i += 3

    return total_priority


def find_intersection(group):
    distinct_values = [set(ruck) for ruck in group]
    intersection = set.intersection(*distinct_values)
    return intersection.pop()


def get_priority(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1


def read_input():
    with open("input.txt", encoding="utf8") as input_file:
        data = input_file.read().splitlines()
    return data


if __name__ == "__main__":
    rucksack_data = read_input()
    answer1 = part1(rucksack_data)
    answer2 = part2(rucksack_data)

    print(answer1)
    print(answer2)
