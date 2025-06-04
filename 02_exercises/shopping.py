budget = float(input())
gpu_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

gpu_price = gpu_amount * 250
cpu_price = cpu_amount * (gpu_price * 0.35)
ram_price = ram_amount * (gpu_price * 0.10)

total_price = gpu_price + cpu_price + ram_price

if gpu_amount >= cpu_amount:
    total_price = total_price - (total_price * 0.15)

money_needed = budget - total_price
if money_needed >= 0:
    print(f'You have {money_needed:.2f} leva left!')
else:
    print(f'Not enough money! You need {-money_needed:.2f} leva more! ')

