def read_adapters(file_location):
    """Read file the code
    """
    adapters = open(file_location, 'r').read().split('\n')
    adapters = [int(entry) for entry in adapters if entry != '']
    adapters.sort()
    return adapters


if __name__ == '__main__':

    difference_1 = 0
    difference_3 = 0
    current_joltage = 0
    adapters = read_adapters('data\\day_10.txt')
    for adapter in adapters:

        if current_joltage + 1 == adapter:
            difference_1 += 1
            current_joltage = adapter
        elif current_joltage + 3 == adapter:
            difference_3 += 1
            current_joltage = adapter
        else:
            continue

    print(difference_1 * (difference_3+1))
