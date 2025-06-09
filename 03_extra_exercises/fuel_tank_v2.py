GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

type_of_fuel = input()  # 'Gas', 'Gasoline', 'Diesel'
fuel_litres = float(input())
club_card = input()  # 'Yes', 'No'

final_price = 0

if club_card == 'Yes':
    if type_of_fuel == 'Gasoline':
        discount = GASOLINE_PRICE - 0.18
        final_price = discount * fuel_litres
    elif type_of_fuel == 'Diesel':
        discount = DIESEL_PRICE - 0.12
        final_price = discount * fuel_litres
    elif type_of_fuel == 'Gas':
        discount = GAS_PRICE - 0.08
        final_price = discount * fuel_litres
elif club_card == 'No':
    if type_of_fuel == 'Gasoline':
        final_price = GASOLINE_PRICE * fuel_litres
    elif type_of_fuel == 'Diesel':
        final_price = DIESEL_PRICE * fuel_litres
    elif type_of_fuel == 'Gas':
        final_price = GAS_PRICE * fuel_litres

if 20 < fuel_litres <= 25:
    discount = 0.08
    final_price = final_price * (1 - discount)
elif fuel_litres > 25:
    discount = 0.10
    final_price = final_price * (1 - discount)
else:
    final_price = final_price

print(f'{final_price:.2f} lv.')
