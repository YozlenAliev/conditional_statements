PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

holiday_price = float(input())
puzzle_amount = int(input())
talking_doll_amount = int(input())
teddy_bear_amount = int(input())
minion_amount: int = int(input())
trucks_amount = int(input())

total_income = (
        puzzle_amount * PUZZLE_PRICE
        + talking_doll_amount * TALKING_DOLL_PRICE
        + teddy_bear_amount * TEDDY_BEAR_PRICE
        + minion_amount * MINION_PRICE
        +trucks_amount * TRUCK_PRICE
)
total_amount_toys = puzzle_amount + talking_doll_amount + teddy_bear_amount + minion_amount + trucks_amount

discount = 0
if total_amount_toys >=50:
    discount = 0.25

total_income_after_discount = total_income * (1 - discount)

rent_cost = total_income_after_discount * 0.10

final_income = total_income_after_discount - rent_cost

if final_income >= holiday_price:
    money_left = final_income - holiday_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = holiday_price - final_income
    print(f'Not enough money! {money_needed:.2f} lv needed.')
