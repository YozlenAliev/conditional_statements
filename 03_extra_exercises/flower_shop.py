from math import ceil, floor

magnolias_count = int(input())
zyumbyuls_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

magnolias_price = magnolias_count * 3.25
zyumbyuls_price = zyumbyuls_count * 4.00
roses_price = roses_count * 3.50
cactus_price = cactus_count * 8.00
total_price_before_taxes = magnolias_price + zyumbyuls_price + roses_price + cactus_price
total_price_after_taxes = total_price_before_taxes - (total_price_before_taxes * 0.05)

money_left = floor(total_price_after_taxes - present_price)
money_needed = ceil(present_price - total_price_after_taxes)

if present_price <= total_price_after_taxes:
    print(f'She is left with {money_left} leva.')
else:
    print(f'She will have to borrow {money_needed} leva.')
