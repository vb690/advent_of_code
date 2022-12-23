def read_boarding_pass_file(file_location):
    """Read file with boarding passes informations
    """
    return open(file_location, 'r').read().split('\n')


def find_seat_id(instructions, rows=128, columns=8):
    """Split a list following instructions
    """
    rows = [row for row in range(rows)]
    columns = [column for column in range(columns)]

    for instruction in instructions:

        if instruction == 'F':
            rows = rows[:len(rows) // 2]
        elif instruction == 'B':
            rows = rows[len(rows) // 2:]
        elif instruction == 'R':
            columns = columns[len(columns) // 2:]
        elif instruction == 'L':
            columns = columns[:len(columns) // 2]

    seat_id = (rows[0] * 8) + columns[0]
    return seat_id, rows[0], columns[0]


def find_my_seat(seats_map, list_seat_ids, rows=128, columns=8):
    """Find my seat iterating through the map of Taken and NotTaken seats
    """
    for row in range(128):

        for column in range(8):

            if seats_map[row][column] == 'NT':
                possible_id = (row * 8) + column
                low_id = possible_id - 1
                high_id = possible_id + 1
                if (low_id in list_seat_ids) and (high_id in list_seat_ids):
                    return possible_id


if __name__ == '__main__':
    boarding_passes = read_boarding_pass_file(
        file_location='data\\day_5.txt'
    )
    list_seat_ids = []
    seats_map = [['NT' for column in range(8)] for rows in range(128)]
    for boarding_pass in boarding_passes:

        seat_id, row, column = find_seat_id(
            instructions=boarding_pass
        )
        list_seat_ids.append(seat_id)
        seats_map[row][column] = 'T'

    print(max(list_seat_ids))
    print(
        find_my_seat(
            seats_map=seats_map,
            list_seat_ids=list_seat_ids
        )
    )
