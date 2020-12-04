
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


class CarefullValidator:
    """Validate passports against multiple requirements.
    """
    def __init__(self):
        """Initialize validator with number of valid passports
        """
        self.valid_count = 0

    def __parse_passport_file(self, file_location):
        """Parse the passports_file in a list of dictionaries
        """
        list_of_passports = []
        passports_file = open(file_location, 'r').read()
        for passport in passports_file.split('\n\n'):

            passport = passport.replace('\n', ' ')
            entries = passport.split(' ')
            passport_dict = {}
            for entry in entries:

                key, value = entry.split(':')
                passport_dict[key] = value

            list_of_passports.append(passport_dict)

        return list_of_passports

    def __check_entries(self, passport_entries, target_entries):
        """Check if passport has all necessaire entries.
        """
        return set(target_entries) <= set(passport_entries)

    def __check_field(self, field, value):
        """Check fields
        """
        bad_letters = [
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        good_ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if field == 'byr':
            return (len(value) == 4) and (1920 <= int(value) <= 2002)
        elif field == 'iyr':
            return (len(value) == 4) and (2010 <= int(value) <= 2020)
        elif field == 'eyr':
            return (len(value) == 4) and (2020 <= int(value) <= 2030)
        elif field == 'hgt':
            if value[-2:] == 'cm':
                return 150 <= int(value[:-2]) <= 193
            elif value[-2:] == 'in':
                return 59 <= int(value[:-2]) <= 76
            else:
                return False
        elif field == 'hcl':
            return (value[0] == '#') and (value[1:] not in bad_letters)
        elif field == 'ecl':
            return value in good_ecls
        elif field == 'pid':
            return len(value) == 9
        else:
            return True

    def carefully_validate(self, file_location, target_entries):
        """Run a series of careful checks.
        """
        list_of_passports = self.__parse_passport_file(
            file_location=file_location
        )
        for passport in list_of_passports:
            # print(passport)
            broken = False
            if not self.__check_entries(
                passport_entries=list(passport.keys()),
                target_entries=target_entries
            ):
                continue

            for target_entry in target_entries:

                if not self.__check_field(
                    field=target_entry,
                    value=passport[target_entry]
                ):
                    broken = True
                    break

            if broken:
                continue
            self.valid_count += 1

        print(self.valid_count)


if __name__ == '__main__':

    # first star
    traverse_list_of_lists(
        split_passports_file(
            read_passports_file(
                file_location='data\\day_4.txt'
            )
        ),
        total=0,
        target=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    )

    # second star
    validator = CarefullValidator()
    validator.carefully_validate(
        file_location='data\\day_4.txt',
        target_entries=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    )
