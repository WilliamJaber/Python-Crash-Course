def make_car(manufacturer, model, **extras) -> dict:
    """Builds a dictionary containing information about a car"""
    
    extras['manufacturer'] = manufacturer
    extras['model'] = model
    return f'\n{extras}\n'

car_info = make_car('BMW', 'X5', color = 'white',
                seats_color = 'Red', luxury_wheels = True)

print(car_info)
