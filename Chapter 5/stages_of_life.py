while age := int(input('Enter your age: ')):    
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
    # This will place the correct article (a/an) before stage_of_life.
    print(f"A person of {age} years old stage life is {('a', 'an')[stage_of_life[0] in 'aeiou']} {stage_of_life}.")
