fruit = input()
day_of_week = input()
quantity = float(input())
result = 0
error_value = False

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if fruit == 'banana':
        result = quantity * 2.50
    elif fruit == 'apple':
        result = quantity * 1.20
    elif fruit == 'orange':
        result = quantity * 0.85
    elif fruit == 'grapefruit':
        result = quantity * 1.45
    elif fruit == 'kiwi':
        result = quantity * 2.70
    elif fruit == 'pineapple':
        result = quantity * 5.50
    elif fruit == 'grapes':
        result = quantity * 3.85
    else:
        error_value =True

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        result = quantity * 2.70
    elif fruit == 'apple':
        result = quantity * 1.25
    elif fruit == 'orange':
        result = quantity * 0.90
    elif fruit == 'grapefruit':
        result = quantity * 1.60
    elif fruit == 'kiwi':
        result = quantity * 3.00
    elif fruit == 'pineapple':
        result = quantity * 5.60
    elif fruit == 'grapes':
        result = quantity * 4.20
    else:
        error_value = True
else:
    error_value = True

if not error_value:
    print(f'{result:.02f}')
else:
    print('error')
