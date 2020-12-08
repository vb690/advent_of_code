def read_instructions(file_location):
    """Read file with lugages rules
    """
    return open(file_location, 'r').read().split('\n')


def get_instructions(line):
    """Split instruction line
    """
    splitted_instructions = line.split(' ')

    instruction_type = splitted_instructions[0]
    instuction_sign = splitted_instructions[1][0]
    instruction_value = int(splitted_instructions[1][1:])

    return instruction_type, instuction_sign, instruction_value


def oparation(instuction_sign, value_1, value_2):
    """
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
    while current_index != len(instructions):

        line = instructions[current_index]
        instruction_type, instuction_sign, \
            instruction_value = get_instructions(line)

        visited_indices.append(current_index)

        if instruction_type == 'acc':
            accumulator = oparation(
                instuction_sign,
                accumulator,
                instruction_value
            )
            current_index += 1
        elif instruction_type == 'jmp':
            current_index = oparation(
                instuction_sign,
                current_index,
                instruction_value
            )
        else:
            current_index += 1

        if current_index in visited_indices:
            print(accumulator)
            break
