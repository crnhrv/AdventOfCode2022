import functools


def main(data):
    i = 1
    ans1 = 0
    for (left, right) in data:
        if compare(left, right) == 1:
            ans1 += i
        i += 1
    print(ans1)

    flattened = [item for sublist in data for item in sublist]
    packets = sorted(flattened, key=functools.cmp_to_key(compare), reverse=True)
    l_divider = packets.index([[2]]) + 1
    r_divider = packets.index([[6]]) + 1
    ans2 = l_divider * r_divider
    print(ans2)


def compare(l, r):
    l_is_list = isinstance(l, list)
    r_is_list = isinstance(r, list)
    if l_is_list and r_is_list:
        return compare_lists(l, r)
    if l_is_list and not r_is_list:
        r_list = [r]
        return compare_lists(l, r_list)
    if not l_is_list and r_is_list:
        l_list = [l]
        return compare_lists(l_list, r)
    if l == r:
        return 0
    if l > r:
        return -1
    if l < r:
        return 1


def compare_lists(left, right):
    i = 0
    while i < len(left) and i < len(right):
        value = compare(left[i], right[i])
        if value != 0:
            return value
        i += 1

    if len(left) == len(right):
        return 0
    if len(left) > len(right):
        return -1
    if len(left) < len(right):
        return 1


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        lines = [l for l in f.read().splitlines() if l]
        items = []
        for item in lines:
            if item[0] == "[":
                new_list = []
                items.append(convert_to_list(item[1:], new_list))
        pairs = [items[i : i + 2] for i in range(0, len(items), 2)]
        return pairs


def convert_to_list(items, new_list):
    if items[0] == "]":
        return new_list
    if items[0] == ",":
        return convert_to_list(items[1:], new_list)
    if items[0] == "'":
        return convert_to_list(items[1:], new_list)
    if items[0] == "[":
        new_new_list = []
        balance = 1
        i = 1
        while balance != 0:
            if items[i] == "[":
                balance += 1
            elif items[i] == "]":
                balance -= 1
            i += 1
        value = convert_to_list(items[1 : i + 1], new_new_list)
    else:
        i = 0
        string = ""
        while items[i].isnumeric():
            string += items[i]
            i += 1
        value = int(string)
    new_list.append(value)
    return convert_to_list(items[i:], new_list)


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt)
