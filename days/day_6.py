def filter_dict(dict_to_filter, target_value):
    """Filter a dictionary based on certain value
    """
    filtered_dict = {}
    for key, value in dict_to_filter.items():

        if target_value == value:
            filtered_dict[key] = value

    return filtered_dict


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


def read_questionnaire_file(file_location):
    """Read file with boarding passes informations
    """
    return open(file_location, 'r').read().split('\n\n')


def count_unique(list_to_count):
    """Counnunmber of entries for each unique value in list
    """
    uniques = {}
    for element in list_to_count:

        if element in uniques:
            uniques[element] += 1
        else:
            uniques[element] = 1

    return uniques


if __name__ == '__main__':
    total_answers = 0
    total_unanymous_answers = 0
    for questions_group in read_questionnaire_file('data\\day_6.txt'):

        group = questions_group.split('\n')
        # counting only individuals with answers
        group = [individual for individual in group if len(individual) > 0]
        # for avoiding redundacies if any
        group = [unique_list(individual) for individual in group]

        uniques = count_unique(questions_group.replace('\n', ''))

        total_answers += len(uniques)
        total_unanymous_answers += len(filter_dict(uniques, len(group)))

    print(total_answers)
    print(total_unanymous_answers)
