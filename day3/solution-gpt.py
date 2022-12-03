# solution created by giving the question prompts verbatim to gpt-3

# input is a list of strings, each string representing the items in a rucksack
input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

# loop through each rucksack and find the item type that appears in both compartments
sum = 0
for rucksack in input:
    # create sets of items in the first and second compartments
    compartment1 = set(rucksack[: len(rucksack) // 2])
    compartment2 = set(rucksack[len(rucksack) // 2 :])

    # find the intersection of the two sets
    common = compartment1.intersection(compartment2)

    # take the first item from the intersection
    item = next(iter(common))

    # compute the priority of the item type
    priority = ord(item)
    if item.islower():
        priority -= 96
    else:
        priority -= 64

    # add the priority to the sum
    sum += priority

# print the result
print(sum)

# part 2

# input is a list of strings, each string representing the items in a rucksack
input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

# loop through each group of three rucksacks
sum = 0
for i in range(0, len(input), 3):
    rucksack1 = input[i]
    rucksack2 = input[i + 1]
    rucksack3 = input[i + 2]

    # create sets of items in each rucksack
    compartment1 = set(rucksack1[: len(rucksack1) // 2])
    compartment2 = set(rucksack1[len(rucksack1) // 2 :])
    compartment3 = set(rucksack2[: len(rucksack2) // 2])
    compartment4 = set(rucksack2[len(rucksack2) // 2 :])
    compartment5 = set(rucksack3[: len(rucksack3) // 2])
    compartment6 = set(rucksack3[len(rucksack3) // 2 :])

    # find the intersection of the three sets
    common = compartment1.intersection(
        compartment2, compartment3, compartment4, compartment5, compartment6
    )

    # take the first item from the intersection
    item = next(iter(common))

    # compute the priority of the item type
    priority = ord(item)
    if item.islower():
        priority -= 96
    else:
        priority -= 64

    # add the priority to the sum
    sum += priority

# print the result
print(sum)
