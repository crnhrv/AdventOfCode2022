import copy


def part1_main(data, instructions):
    boxes = copy.deepcopy(data)
    for instruction in instructions:
        (amount_to_move, from_stack, to_stack) = instruction
        i = 0
        while i < amount_to_move:
            box = boxes[from_stack - 1].pop()
            boxes[to_stack - 1].append(box)
            i += 1
    answer = ""
    for box in boxes:
        answer += box[-1]
    return answer


def part2_main(data, instructions):
    boxes = copy.deepcopy(data)
    for instruction in instructions:
        (amount_to_move, from_stack, to_stack) = instruction
        i = 0
        intermediate = []
        while i < amount_to_move:
            intermediate.append(boxes[from_stack - 1].pop())
            i += 1
        intermediate.reverse()
        insert_at = len(boxes[to_stack - 1])
        i = 0
        while i < amount_to_move:
            boxes[to_stack - 1].insert(insert_at, intermediate.pop())
            i += 1
    answer = ""
    for box in boxes:
        answer += box[-1]
    return answer


def read_input(filename):
    space_between = 4
    data = []
    max_width = 0
    max_height = 0
    with open(filename, encoding="utf8") as f:
        lines = f.readlines()

    row_index = 0
    hit_instructions = False
    for line in lines:
        if hit_instructions:
            break
        space = 0
        col_index = 0
        for char in line:
            if char.isspace():
                space += 1
            elif char.isalpha():
                if space // space_between:
                    (a, b) = divmod(space, space_between)
                    if not b:
                        col_index += a + b + 1
                    else:
                        col_index += a + b
                else:
                    col_index += 1
                data.append((char, col_index - 1))
                max_width = max(col_index, max_width)
                space = 0
            elif char.isnumeric():
                max_height = row_index + 1
                hit_instructions = True
                break
        row_index += 1

    instructions = []
    for line in lines[max_height + 1 :]:
        line = line.split(None)
        instruction = [int(x) for x in [line[1], line[3], line[5]]]
        instructions.append(tuple(instruction))

    stacks = create_stacks(max_width, data)

    return (stacks, instructions)


def create_stacks(cols, data):
    stacks = [[] for _ in range(cols)]
    for item in data:
        (char, col) = item

        stacks[col].insert(0, char)
    return stacks


if __name__ == "__main__":
    (stck, inst) = read_input("input.txt")
    answer1 = part1_main(stck, inst)
    answer2 = part2_main(stck, inst)
    print(answer1)
    print(answer2)
