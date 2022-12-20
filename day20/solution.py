def main(data, mix_count, dec_key):
    data = [(i, x * dec_key) for (i, x) in enumerate(data)]
    ordering = data[:]
    for _ in range(mix_count):
        data = mix(data, ordering)

    data = [x[1] for x in data]
    ans = get_answer(data)
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
    new_index = (index + shift_by[1]) % len(data)
    data.insert(new_index, shift_by)


def get_answer(data):
    ans = 0
    zero_index = data.index(0)
    for i in range(1000, 3001, 1000):
        index = (zero_index + i) % len(data)
        ans += data[index]
    return ans


def read_input(filename):
    with open(filename, encoding="utf8") as input_file:
        return list(map(int, input_file.read().splitlines()))


if __name__ == "__main__":
    dt = read_input("input.txt")
    ans1 = main(dt, 1, 1)
    ans2 = main(dt, 10, 811589153)
    print(ans1)
    print(ans2)
