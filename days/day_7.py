def read_rules(file_location):
    """Read file with lugages rules
    """
    return open(file_location, 'r').read().split('\n')


def unique_list(list_redundant):
    """Select only unique elements in a list
    """
    list_unique_elements = []
    for element in list_redundant:

        if element in list_unique_elements:
            continue
        else:
            list_unique_elements.append(element)

    return list_unique_elements


def split_rule_matrioska(rule):
    """Split a rule for knowing which bag can contain another bag
    """
    return rule.split(' bags contain ')


if __name__ == '__main__':
    bags_target = ['shiny gold']

    # first start
    index = 0
    while True:

        if index == len(bags_target):
            break
        search_for = bags_target[index]

        for rule in read_rules('data\\day_7.txt'):

            if rule == '':
                continue

            bags = split_rule_matrioska(rule)
            if search_for in bags[1]:
                bags_target.append(bags[0])

        index += 1

    print(len(unique_list(bags_target[1:])))

    # second star
