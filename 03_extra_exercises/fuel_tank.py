type_of_fuel = input()  # 'Diesel', 'Gasoline', 'Gas'
fuel_available = float(input())

if type_of_fuel == 'Diesel':
    if fuel_available >= 25:
        print(f'You have enough diesel.')
    else:
        print(f'Fill your tank with diesel!')

elif type_of_fuel == 'Gasoline':
    if fuel_available >= 25:
        print(f'You have enough gasoline.')
    else:
        print(f'Fill your tank with gasoline!')
elif type_of_fuel == 'Gas':
    if fuel_available >= 25:
        print(f'You have enough gas.')
    else:
        print(f'Fill your tank with gas!')
else:
    print('Invalid fuel!')
