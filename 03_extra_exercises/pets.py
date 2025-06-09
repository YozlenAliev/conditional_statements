from math import ceil, floor

days_off = int(input())
food_for_all = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_tortoise = float(input())

dog_food_needed = days_off * food_for_dog
cat_food_needed = days_off * food_for_cat
tortoise_food_needed = (days_off * food_for_tortoise) / 1000

total_foot = dog_food_needed + cat_food_needed + tortoise_food_needed
food_needed = ceil(total_foot - food_for_all)
food_left = floor(food_for_all - total_foot)

if total_foot < food_for_all:
    print(f'{food_left} kilos of food left.')
else:
    print(f'{food_needed} more kilos of food are needed.')
