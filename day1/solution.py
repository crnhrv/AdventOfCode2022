total_calories_per_elf = []

with open("input.txt") as f:
    input = f.read().splitlines()
    total_calories = 0
    for calories in input:
        if not calories:
            total_calories_per_elf.append(total_calories)
            total_calories = 0
        else:
            total_calories += int(calories)

total_calories_per_elf.sort()
highest_total = total_calories_per_elf[-1]
print(highest_total) # answer 1

top3 = total_calories_per_elf[-3:]
print(sum(top3)) # answer 2

