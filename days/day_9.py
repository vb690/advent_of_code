def read_code(file_location):
    """Read file the code
    """
    code = open(file_location, 'r').read().split('\n')
    code = [int(entry) for entry in code if entry != '']
    return code


def find_additions(list_to_add):
    """Find additions of two terms in list
    """
    additions = []
    for index, first_element in enumerate(list_to_add):

        for second_element in list_to_add[index+1:]:

            additions.append(first_element+second_element)

    return additions


def find_the_key(code, window):
    """Find the key of the code
    """
    for index, target in enumerate(code[window:]):

        code_window = code[index:index+window]
        additions = find_additions(code_window)
        if target not in additions:
            print(target)
            return target


def crack_the_code(target, code):
    """Find window and values matching with the target
    """
    for window in range(2, len(code)):

        for index in range(len(code[window:])):

            code_window = code[index:index+window]
            additions = sum(code_window)
            if target == additions:
                print(min(code_window) + max(code_window))
                break


if __name__ == '__main__':
    code = read_code('data\\day_9.txt')
    window = 25
    crack_the_code(
        target=find_the_key(code=code, window=window),
        code=code
    )
