budget = float(input())
statist_amount = int(input())
statist_dress_price = float(input())

dekor = budget * 0.10
money_dress = statist_amount * statist_dress_price

if statist_amount >= 150:
    money_dress = money_dress - (money_dress * 0.10)

money_needed = dekor + money_dress
final_price = budget - money_needed

if final_price >= 0:
    print('Action!')
    print(f'Wingard starts filming with {final_price:.2f} leva left.')

else:
    print('Not enough money!')
    print(f'Wingard needs {-final_price:.2f} leva more.')
