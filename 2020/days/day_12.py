def read_directions(file_location):
    """Read directions
    """
    directions = []
    amounts = []
    list_directions = open(file_location, 'r').read().split('\n')
    for line in list_directions:

        if line == '':
            continue
        directions.append(line[0])
        amounts.append(int(line[1:]))

    return directions, amounts


def change_direction(current_face, degree, left):
    """
    """
    if left:
        new_face = current_face - degree
    else:
        new_face = current_face + degree

    while 0 >= new_face or new_face > 360:
        if new_face <= 0:
            new_face = 360 + new_face
        elif new_face > 360:
            new_face = new_face - 360
        else:
            new_face = new_face

    return new_face


if __name__ == '__main__':
    directions, amounts = read_directions('data\\day_12.txt')

    # first star
    east = 0
    north = 0
    current_face = 90
    for direction, amount in zip(directions, amounts):

        if direction == 'F':
            if current_face == 90:
                east += amount
            elif current_face == 270:
                east -= amount
            elif current_face == 360:
                north += amount
            elif current_face == 180:
                north -= amount
        elif direction == 'N':
            north += amount
        elif direction == 'S':
            north -= amount
        elif direction == 'E':
            east += amount
        elif direction == 'W':
            east -= amount
        elif direction == 'L':
            current_face = change_direction(current_face, amount, True)
        elif direction == 'R':
            current_face = change_direction(current_face, amount, False)

    print(abs(east) + abs(north))
