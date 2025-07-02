hour_from_day = int(input())
day_of_week = input()

if 10 <= hour_from_day <= 18:
    if day_of_week == 'Monday':
        print('open')
    elif day_of_week == 'Tuesday':
        print('open')
    elif day_of_week == 'Wednasday':
        print('open')
    elif day_of_week == 'Thursday':
        print('open')
    elif day_of_week == 'Friday':
        print('open')
    elif day_of_week == 'Saturday':
        print('open')
    else:
        print('closed')
else:
    print('closed')
