from math import floor, ceil

vineyard_square_meters = int(input())
grapes_for_square_meter = float(input())
vine_for_sale = int(input())
workers = int(input())

total_grapes = vineyard_square_meters * grapes_for_square_meter
vine = total_grapes * 0.40
vine_produced = ceil(vine / 2.5)
vine_needed = floor(vine_for_sale - vine_produced)
vine_left = ceil(vine_produced - vine_for_sale)

if vine_produced < vine_for_sale:
    print(f'It will be a tough winter! More {vine_needed} liters wine needed.')
else:
    vine_per_person = ceil(vine_left / workers)
    print(f'Good harvest this year! Total wine: {vine_produced} liters.')
    print(f'{vine_left} liters left -> {vine_per_person} liters per person.')
