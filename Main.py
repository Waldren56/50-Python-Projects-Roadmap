def display_units():
    units = {
        'length': {
            'm': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001
        },
        'weight': {
            'g': 1, 'kg': 1000, 'lb': 0.453592
        }
    }

    return units

def convertion_info():
    units = display_units()

    while True:
        category_unit = input("Please enter the category of your unit: ")
        if category_unit not in units.keys():
            print('Please enter a valid category', end=': ')
            for unit in units.keys():
                print(unit, end=' ')
            print('\n')
        else:
            break

    while True:
        user_unit = input("Please enter the unit: ")
        if user_unit not in units[category_unit].keys():
            print('Please enter a valid unit', end=': ')
            for unit in units[category_unit].keys():
                print(unit, end=' ')
            print('\n')
        else:
            break

    while True:
        convertion_unit = input("Please enter the convertion unit: ")
        if convertion_unit not in units[category_unit].keys():
            print('Please enter a valid unit', end=': ')
            for unit in units[category_unit].keys():
                print(unit, end=' ')
            print('\n')
        else:
            break

    while True:
        try:
            user_int = int(input("Please enter the measure to convert: "))
            break
        except ValueError:
            print('Please enter a natural number\n')

    user_factor = units[category_unit][user_unit]
    target_factor = units[category_unit][convertion_unit]

    converted_unit = user_factor / target_factor * user_int

    return converted_unit

def main():
    result = convertion_info()

    print(result)

if __name__ == '__main__':
    main()