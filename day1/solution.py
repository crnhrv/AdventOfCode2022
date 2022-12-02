def main():
    total_calories_per_elf = []
    calories = 0
    with open("input.txt", encoding="utf8") as input_file:
        calorie_chunks = input_file.read().splitlines()
        for calories in calorie_chunks:
            if not calories:
                total_calories_per_elf.append(total_calories)
                total_calories = 0
            else:
                total_calories += int(calories)

    total_calories_per_elf.sort()
    highest_total = total_calories_per_elf[-1]
    print(highest_total)  # answer 1

    top3 = total_calories_per_elf[-3:]
    print(sum(top3))  # answer 2


if __name__ == "__main__":
    main()
