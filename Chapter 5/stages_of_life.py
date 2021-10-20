age = 16
if age < 2:
    stage_of_life = 'baby'
elif age < 4:
    stage_of_life = 'toddler'
elif age < 13:
    stage_of_life = 'kid'
elif age < 20:
    stage_of_life = 'teenager'
elif age < 65:
    stage_of_life = 'adult'
else:
    stage_of_life = 'elder'

print(f'A person of {age} years old stage life is a/an: {stage_of_life}')
