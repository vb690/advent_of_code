import os

implemented_days = [day for day in range(1, len(os.listdir('days'))+1)]
selected_day = int(input('Select a day '))

if selected_day not in [-1] + implemented_days:
    raise Exception(f'Day {selected_day} not implemented yet.')

if selected_day == -1:
    print('')
    print('Performing batch execution')
    print('')
    print('############################')
    print('')
    for implemented_day in implemented_days:

        print(f'Running Day {implemented_day}')
        print('')
        os.system(f'days\\day_{implemented_day}.py')
        print('')

else:
    print(f'Running Day {selected_day}')
    print('')
    os.system(f'days\\day_{selected_day}.py')
    print('')
