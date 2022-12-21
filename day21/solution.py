def p1(monkeys: dict):
    monkeys["root"] = recurse_until_value(monkeys, monkeys["root"])
    return int(monkeys["root"])


def p2(monkeys: dict, max_possible):
    target_monkeys = monkeys.copy()
    p1(target_monkeys)
    (lmonkey, _, rmonkey) = monkeys["root"].split(" ")
    bin_search_monkeys(
        monkeys,
        max_possible,
        lmonkey,
        target_monkeys[rmonkey],
    )


def bin_search_monkeys(monkeys, max_num, lmonkey, search_val):
    low = 0
    high = max_num
    while low < high:
        mid = (low + high) // 2
        score = search_val - get_left_monkey_val(monkeys.copy(), lmonkey, mid)
        if score < 0:
            low = mid
        elif score == 0:
            print(mid)
            break
        else:
            high = mid


def get_left_monkey_val(monkeys, lmonkey, humn_number):
    monkeys["root"] = monkeys["root"].replace("+", "==")
    monkeys["humn"] = humn_number
    monkeys["root"] = recurse_until_value(monkeys, monkeys["root"])
    return monkeys[lmonkey]


def recurse_until_value(monkeys, equation):
    if isinstance(equation, int):
        return equation
    if isinstance(equation, float):
        return equation
    equation_parts = equation.split(" ")
    if len(equation_parts) == 1:
        return int(equation)
    new_equation = []
    for part in equation_parts:
        if part in monkeys:
            monkeys[part] = recurse_until_value(monkeys, monkeys[part])
            new_equation.append(monkeys[part])
        else:
            new_equation.append(part)
    return eval("".join([str(x) for x in new_equation]))


def read_input(filename):
    monkeys = {}
    with open(filename, encoding="utf8") as input_file:
        lines = input_file.read().splitlines()
        for line in lines:
            (monkey, operation) = line.split(":")
            operation = operation.strip()
            if operation[0].isnumeric():
                monkeys[monkey] = int(operation)
            else:
                monkeys[monkey] = operation

    return monkeys


if __name__ == "__main__":
    p1_data = read_input("input.txt")
    ans1 = p1(p1_data)
    print(ans1)
    p2_data = read_input("input.txt")
    ans2 = p2(p2_data, ans1 * 2)
    print(ans2)
