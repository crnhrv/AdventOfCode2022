class Node(object):
    def __init__(self, name, parent):
        self.size = 0
        self.parent = parent
        self.name = name
        self.children = []

    def add_child_if_not_exists(self, obj):
        if not self.exists_in_children(obj):
            self.children.append(obj)
        return obj

    def exists_in_children(self, obj):
        for child in self.children:
            if child.name == obj.name and child.parent == self:
                return True
        return False

    def calculate_total_size(self):
        for child in self.children:
            child.calculate_total_size()
            self.increase_size(child.size)

    def increase_size(self, size):
        self.size += size

    def get_all_children(self):
        for child in self.children:
            yield child
            yield from child.get_all_children()


def main(data):
    root = Node("/", None)
    current_dir = root
    i = 0
    while i < len(data):
        if data[i].startswith("$ cd"):
            current_dir = handle_cd(data[i], root, current_dir)
            i += 1
        elif data[i].startswith("$ ls"):
            ls_data = []
            i += 1
            while i < len(data) and not data[i].startswith("$"):
                ls_data.append(data[i])
                i += 1
            handle_ls(ls_data, current_dir)
    root.calculate_total_size()
    unused_space = 70000000 - root.size
    required_space = 30000000 - unused_space
    answer1 = 0
    answer2 = root.size
    for child in root.get_all_children():
        if child.size <= 100000:
            answer1 += child.size
        if child.size >= required_space:
            answer2 = min(answer2, child.size)
    return (answer1, answer2)


def handle_cd(command, root, current_dir):
    (_, _, directory) = command.split(" ")
    if directory == root.name:
        current_dir = root
    elif directory == "..":
        current_dir = current_dir.parent
    else:
        current_dir = current_dir.add_child_if_not_exists(Node(directory, current_dir))
    return current_dir


def handle_ls(data, current_dir):
    for line in data:
        if not line.startswith("dir"):
            current_dir.increase_size(int(line.split(" ")[0]))


def read_input(filename):
    with open(filename, encoding="utf8") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    dt = read_input("input.txt")
    (ans1, ans2) = main(dt)
    print(ans1)
    print(ans2)
