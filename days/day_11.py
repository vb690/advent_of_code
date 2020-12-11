def read_seats(file_location):
    """Read file the code
    """
    seats = []
    seat_map = open(file_location, 'r').read().split('\n')
    for line in seat_map:

        if line == '':
            continue
        seats.append(list(line))

    return seats


def count_occupied(locations):
    """Count occupied locations
    """
    occupied = 0
    for location in locations:

        if location == '#':
            occupied += 1

    return occupied


def check_neigh(current_loc, seats):
    """Check neighbouring locations
    """
    x, y = current_loc[0], current_loc[1]
    Xs = [x, x, x+1, x-1, x+1, x+1, x-1, x-1]
    Ys = [y+1, y-1, y, y, y+1, y-1, y+1, y-1]
    locations = []
    for xs, ys in zip(Xs, Ys):

        try:
            locations.append(seats[xs][ys])
        except IndexError:
            locations.append('null')

    occupied = count_occupied(locations)
    if occupied == 0:
        return '#'
    if occupied >= 4:
        return 'L'
    else:
        return seats[x][y]


if __name__ == '__main__':

    seats = read_seats('data\\day_11.txt')
    changing = True
    while changing:

        new_seats = []

        for row in range(len(seats)):

            new_row = []

            for column in range(len(seats[0])):

                if seats[row][column] == '.':
                    new_row.append('.')
                else:
                    new_row.append(check_neigh((row, column), seats))

            new_seats.append(new_row)

        if seats == new_seats:
            changing = False
            print(
                count_occupied(
                    [seat for row in new_seats for seat in row]
                )
            )
        else:
            seats = new_seats
