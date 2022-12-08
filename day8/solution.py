def main(forest):
    visible_trees = set()

    for (i, trees) in enumerate(forest):
        max_so_far = -1
        for (j, tree) in enumerate(trees):
            if tree > max_so_far:
                visible_trees.add((tree, i, j))
            max_so_far = max(tree, max_so_far)

    for (i, trees) in enumerate(forest):
        max_so_far = -1
        for (j, tree) in enumerate(reversed(trees)):
            if tree > max_so_far:
                visible_trees.add((tree, i, len(trees) - 1 - j))
            max_so_far = max(tree, max_so_far)

    for (i, trees) in enumerate((zip(*forest))):
        max_so_far = -1
        for (j, tree) in enumerate((trees)):
            if tree > max_so_far:
                visible_trees.add((tree, j, i))
            max_so_far = max(tree, max_so_far)

    for (i, trees) in enumerate((zip(*forest))):
        max_so_far = -1
        for (j, tree) in enumerate((reversed(trees))):
            if tree > max_so_far:
                visible_trees.add((tree, len(trees) - 1 - j, i))
            max_so_far = max(tree, max_so_far)

    ans2 = 0
    for (tree, i, j) in visible_trees:
        if i == 0 or i == len(forest) - 1:
            continue
        elif j == 0 or j == len(forest[i]) - 1:
            continue
        right = 0
        left = 0
        up = 0
        down = 0

        down_i = i + 1
        while down_i < len(forest):
            down += 1
            if forest[down_i][j] >= tree:
                break
            down_i += 1
        up_i = i - 1
        while up_i >= 0:
            up += 1
            if forest[up_i][j] >= tree:
                break
            up_i -= 1
        right_i = j + 1
        while right_i < len(forest[i]):
            right += 1
            if forest[i][right_i] >= tree:
                break
            right_i += 1
        left_i = j - 1
        while left_i >= 0:
            left += 1
            if forest[i][left_i] >= tree:
                break
            left_i -= 1

        ans2 = max(up * left * down * right, ans2)

    return (len(visible_trees), ans2)


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        lines = f.read().splitlines()
        forest = []
        for line in lines:
            trees = []
            for char in line:
                trees.append(int(char))
            forest.append(trees)
    return forest


if __name__ == "__main__":
    dt = read_input("input.txt")
    (ans1, ans2) = part_1(dt)
    print(ans1)
    print(ans2)
