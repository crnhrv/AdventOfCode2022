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
        print(total_real_number, snafu_number, max_place)
        if snafu_number == total_real_number:
            snafu_digits.append("0")
        elif snafu_number > total_real_number:
            lowest_potential_subtraction = (base**max_place) * -1
            lowest_potential_new_snafu_number = (
                snafu_number + lowest_potential_subtraction
            )
            lowest_difference = total_real_number - lowest_potential_new_snafu_number
            highest_potential_subtraction = (base**max_place) * -2
            highest_potential_new_snafu_number = (
                snafu_number + highest_potential_subtraction
            )
            highest_difference = total_real_number - highest_potential_new_snafu_number
            next_max_addition = (base ** (max_place - 1)) * 2

            if (
                highest_difference > next_max_addition
                and lowest_difference > next_max_addition
            ):
                snafu_digits.append("0")
            elif highest_difference > next_max_addition:
                snafu_digits.append("-")
                snafu_number += lowest_potential_subtraction
            else:
                snafu_digits.append("=")
                snafu_number += (base**max_place) * -2
        elif snafu_number < total_real_number:
            max_next_subtraction = (base ** (max_place - 1)) * 2
            lowest_addition = (base**max_place) * 1
            lowest_new_snafu_number = snafu_number + lowest_addition
            min_required_to_subtract_after_this = (
                lowest_new_snafu_number - total_real_number
            )

            highest_addition = (base**max_place) * 2
            highest_new_snafu_number = snafu_number + highest_addition
            max_required_to_subtract_after_this = (
                highest_new_snafu_number - total_real_number
            )
            if (
                min_required_to_subtract_after_this > max_next_subtraction
                and max_required_to_subtract_after_this > max_next_subtraction
            ):
                snafu_digits.append("0")
            elif max_required_to_subtract_after_this > max_next_subtraction:
                snafu_digits.append("1")
                snafu_number += (base**max_place) * 1
            else:
                snafu_digits.append("2")
                snafu_number += (base**max_place) * 2
        max_place -= 1
    print("".join(snafu_digits))


def read_input(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


if __name__ == "__main__":
    dt = read_input("input.txt")
    main(dt, 5)
