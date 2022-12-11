import collections
import math


class Test:
    def __init__(self, value: int, if_true: int, if_false: int):
        self.divisible_by = value
        self.if_true = if_true
        self.if_false = if_false

    def __str__(self):
        return f"test: divisible by {self.divisible_by}" \
               f"\n\tif true: throw to {self.if_true}" \
               f"\n\tif false:" \
               f"throw to {self.if_false} "

    def __repr__(self):
        return self.__str__()


class Monkey:
    def __init__(self, items: collections.deque, operation: str, test: Test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def __str__(self):
        return f"items: {self.items}\n" \
               f"operation: new = {self.operation}\n" \
               f"test: {self.test}\n" \
               f"inspections:{self.inspections}"

    def __repr__(self):
        return "\n" + self.__str__() + "\n"


def main(monkeys, rounds, p1):
    current_round = 1
    worry_divisor = 1
    for monkey in monkeys:
        worry_divisor = math.lcm(worry_divisor, monkey.test.divisible_by)
    while current_round <= rounds:
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            for j in range(len(monkey.items)):
                old = monkey.items.popleft()
                new = eval(monkey.operation)  # using old
                if p1:
                    new //= 3
                else:
                    new %= worry_divisor
                if new % monkey.test.divisible_by == 0:
                    monkeys[monkey.test.if_true].items.append(new)
                else:
                    monkeys[monkey.test.if_false].items.append(new)
                monkey.inspections += 1

        current_round += 1
    monkeys.sort(key=lambda x: x.inspections, reverse=True)
    answer1 = monkeys[0].inspections * monkeys[1].inspections
    return answer1


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        monkey = Monkey(None, None, None)
        monkeys = []
        for line in f.readlines():
            if line == "\n":
                monkeys.append(monkey)
                monkey = Monkey(None, None, None)
                continue
            (operation, data) = line.strip().split(":")
            match operation:
                case "Starting items":
                    monkey.items = collections.deque([int(x) for x in data.split(",")])
                case "Operation":
                    monkey.operation = data.split("=")[1]
                case "Test":
                    monkey.test = Test(int(data.split(" ")[-1]), 0, 0)
                case "If true":
                    monkey.test.if_true = int(data.split(" ")[-1])
                case "If false":
                    monkey.test.if_false = int(data.split(" ")[-1])
    monkeys.append(monkey)
    return monkeys


if __name__ == "__main__":
    ans1_data = read_input("input.txt")
    ans2_data = read_input("input.txt")
    ans1 = main(ans1_data, 20, True)
    ans2 = main(ans2_data, 10000, False)
    print(ans1)
    print(ans2)
