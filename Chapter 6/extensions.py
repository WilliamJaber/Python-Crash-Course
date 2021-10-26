# Extended 6-2.
# by adding new keys and values, changing the context of the program or
# improving the formatting of the output.
users_evaluation = {
    'kari': [2, 9],
    'dave': [7, 2],
    'dan': [11, 5],
    'alex': [9, 2],
    'edd': [10, 2],
    'gen': [6, 7],
    'jhon': [8, 9],
    }

for name, evaluation in users_evaluation.items():
    print(f"\n{name.title()}'s total evaluation: {sum(evaluation)}")
    if sum(evaluation) < 10:
        print('\tRegular evaluation')
    elif sum(evaluation) < 15:
        print('\tGood evaluation')
    else:
        print('\tExcelente evaluation')
