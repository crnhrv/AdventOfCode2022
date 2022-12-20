def part1(data):
    data = mix(data[:], data[:])
    data = [x[1] for x in data]
    ans1 = get_answer(data)
    print(ans1)


def part2(data, dec_key):
    data = [x * dec_key for x in data]
    ordering = data[:]
    for _ in range(10):
        data = mix(data, ordering)
        data = [x[1] for x in data]
        print(data)
    ans2 = get_answer(data)
    print(ans2)


def get_answer(data):
    ans = 0
    zero_index = data.index(0)
    for i in range(1000, 3001, 1000):
        index = (zero_index + i) % len(data)
        ans += data[index]
    return ans


def mix(data: list[int], ordering):
    order_pos = 0
    while order_pos < len(ordering):
        current_number = ordering[order_pos]
        shift(data, current_number)
        order_pos += 1
    return data


def shift(data: list[int], shift_by):
    index = data.index(shift_by)
    _ = data.pop(index)
    new_index = (index + shift_by) % len(data)
    new_value = (0, shift_by)
    data.insert(new_index, new_value)


def read_input(filename):
    with open(filename, encoding="utf8") as input_file:
        return list(map(int, input_file.read().splitlines()))


if __name__ == "__main__":
    dt = read_input("test-input.txt")
    part1(dt)
    part2(dt, 811589153)
