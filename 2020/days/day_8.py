def read_instructions(file_location):
    """Read file with lugages rules
    """
    return open(file_location, 'r').read().split('\n')


def split_instructions(instructions):
    """Split instruction line
    """
    instruction_types = []
    instruction_signs = []
    instruction_values = []

    for line in instructions:

        if line == '':
            continue

        splitted_instructions = line.split(' ')

        instruction_types.append(splitted_instructions[0])
        instruction_signs.append(splitted_instructions[1][0])
        instruction_values.append(int(splitted_instructions[1][1:]))

    return instruction_types, instruction_signs, instruction_values


def operation(instuction_sign, value_1, value_2):
    """Perform operation between two values
    """
    if instuction_sign == '+':
        return value_1 + value_2
    elif instuction_sign == '-':
        return value_1 - value_2


if __name__ == '__main__':
    instructions = read_instructions('data\\day_8.txt')
    accumulator = 0
    current_index = 0
    visited_indices = []
    instruction_types, instruction_signs, \
        instruction_values = split_instructions(instructions)
    while current_index < len(instruction_types):

        visited_indices.append(current_index)

        instruction_type = instruction_types[current_index]
        instuction_sign = instruction_signs[current_index]
        instruction_value = instruction_values[current_index]

        if instruction_type == 'acc':
            accumulator = operation(
                instuction_sign,
                accumulator,
                instruction_value
            )
            current_index += 1

        elif instruction_type == 'jmp':
            current_index = operation(
                instuction_sign,
                current_index,
                instruction_value
            )
            if current_index in visited_indices:
                print(f'Endless loop reached at {accumulator}')
                break
        else:
            current_index += 1
            if current_index in visited_indices:
                print(f'Endless loop reached at {accumulator}')
                break
