def expenses_check(expenses, target_sum):
    """Checking expenses
    """
    first_break = False
    second_break = False
    for lvl_1 in range(len(expenses)):

        for lvl_2 in range(lvl_1, len(expenses)):

            if expenses[lvl_1] + expenses[lvl_2] == 2020:
                result_dyad = expenses[lvl_1] * expenses[lvl_2]
                first_break = True

            for lvl_3 in range(lvl_2, len(expenses)):

                if expenses[lvl_1] + expenses[lvl_2] + expenses[lvl_3] == 2020:
                    result_triad = expenses[lvl_1] * expenses[lvl_2] \
                        * expenses[lvl_3]
                    second_break = True

                if first_break and second_break:
                    break

    return result_dyad, result_triad


###############################################################################


if __name__ == '__main__':
    day_1_input = open('data\\day_1.txt', 'r')
    day_1_input = day_1_input.read()

    expenses = [int(expense) for expense in day_1_input.split('\n')]

    result_dyad, result_triad = expenses_check(
        expenses=expenses,
        target_sum=2020
    )

    print(result_dyad, result_triad)
