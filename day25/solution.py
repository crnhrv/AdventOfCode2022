def main(data, base):
    mapping = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

    total_real_number = 0
    for number in data:
        place = len(number) - 1
        current_real_number = 0
        for digit in number:
            current_real_number += (base**place) * mapping[digit]
            place -= 1
        total_real_number += current_real_number

    max_place = 0
    for place in range(len(str(total_real_number)) + 10):
        if total_real_number < (base**place) * 2:
            max_place = place
            break

    snafu_number = 0
    snafu_digits = []
    while max_place > -1:
        if snafu_number == total_real_number:
            snafu_digits.append("0")
        elif snafu_number > total_real_number:
            min_subtraction = (base**max_place) * -1
            min_new_snafu = snafu_number + min_subtraction
            min_diff = total_real_number - min_new_snafu

            max_subtraction = (base**max_place) * -2
            max_new_snafu = snafu_number + max_subtraction
            max_diff = total_real_number - max_new_snafu

            next_max_addition = (base ** (max_place - 1)) * 2

            if max_diff > next_max_addition and min_diff > next_max_addition:
                snafu_digits.append("0")
            elif max_diff > next_max_addition:
                snafu_digits.append("-")
                snafu_number = min_new_snafu
            else:
                snafu_digits.append("=")
                snafu_number = max_new_snafu
        elif snafu_number < total_real_number:
            next_max_subtraction = (base ** (max_place - 1)) * 2

            min_addition = (base**max_place) * 1
            min_new_snafu = snafu_number + min_addition
            min_required_subtraction = min_new_snafu - total_real_number

            max_addition = (base**max_place) * 2
            max_new_snafu = snafu_number + max_addition
            max_required_subtraction = max_new_snafu - total_real_number
            if (
                min_required_subtraction > next_max_subtraction
                and max_required_subtraction > next_max_subtraction
            ):
                snafu_digits.append("0")
            elif max_required_subtraction > next_max_subtraction:
                snafu_digits.append("1")
                snafu_number = min_new_snafu
            else:
                snafu_digits.append("2")
                snafu_number = max_new_snafu
        max_place -= 1
    print("".join(snafu_digits))


def read_input(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt, 5)
