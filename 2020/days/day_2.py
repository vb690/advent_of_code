def count_character(target_character, long_string):
    """Count target_character appearance in string
    """
    count = 0
    for character in long_string:

        if target_character == character:
            count += 1

    return count


def validate(target_letter, password, mini, maxi):
    """Validate Password
    """

    letter_mini = password[mini - 1]
    letter_maxi = password[maxi - 1]

    counted_character = count_character(
        target_character=target_letter,
        long_string=password
    )
    counted_validation = mini <= counted_character <= maxi

    if letter_mini == target_letter and letter_maxi == target_letter:
        return counted_validation, False
    elif letter_mini == target_letter or letter_maxi == target_letter:
        return counted_validation, True
    else:
        return counted_validation, False


###############################################################################

if __name__ == '__main__':
    day_2_input = open('data\\day_2.txt', 'r')
    day_2_input = day_2_input.read()

    valid_counts = 0
    valid_indices = 0
    for line in day_2_input.split('\n'):

        numbers, target_letter, password = line.split()

        numbers = numbers.split('-')
        mini = int(numbers[0])
        maxi = int(numbers[1])

        target_letter = target_letter[0]

        count_validation, index_validation = validate(
            target_letter=target_letter,
            password=password,
            mini=mini,
            maxi=maxi
        )

        valid_counts += count_validation
        valid_indices += index_validation

    print(valid_counts, valid_indices)
