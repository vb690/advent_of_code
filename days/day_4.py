def read_passports_file(file_location):
    """Read file with passports informations
    """
    return open(file_location, 'r').read()


def split_passports_file(passports_file):
    """Split the passports_file in batches
    """
    return passports_file.split('\n\n')


def change_newline(passports_batch):
    """Replace a newline character with a space
    """
    return passports_batch.replace('\n', ' ')


def change_semicolon(new_line_changed_batch):
    """Replace a semicolon character with a space
    """
    return new_line_changed_batch.replace(':', ' ')


def split(semicolon_changed_batch):
    """Split a batch
    """
    return semicolon_changed_batch.split(' ')


def check_compliance(splitted_batch):
    """Check if a batch is compliant
    """
    pass


def traverse_list(list_to_traverse, count, target):
    """Traverse a list using recursion.
    """
    if len(list_to_traverse) == 1:
        if list_to_traverse[0] in target:
            return count+1
        else:
            return count
    else:
        if list_to_traverse[0] in target:
            return traverse_list(list_to_traverse[1:], count+1, target)
        else:
            return traverse_list(list_to_traverse[1:], count, target)


def traverse_list_of_lists(list_of_lists, total, target):
    """Traverse a list of lists using recursion.
    """
    if len(list_of_lists) == 1:
        if traverse_list(
            split(
                change_semicolon(
                    change_newline(
                        list_of_lists[0]
                    )
                )
            ),
            count=0,
            target=target
        ) == len(target):
            print(total + 1)
        else:
            print(total)

    else:
        if traverse_list(
            split(
                change_semicolon(
                    change_newline(
                        list_of_lists[0]
                    )
                )
            ),
            count=0,
            target=target
        ) == len(target):
            return traverse_list_of_lists(list_of_lists[1:], total+1, target)
        else:
            return traverse_list_of_lists(list_of_lists[1:], total, target)


if __name__ == '__main__':

    traverse_list_of_lists(
        split_passports_file(
            read_passports_file(
                file_location='..\\data\\day_4.txt'
            )
        ),
        total=0,
        target=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    )
