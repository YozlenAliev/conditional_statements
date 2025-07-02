city = input()
sales = float(input())
commission_value = 0
error_value = False

if city == 'Sofia':
    if 0 <= sales <= 500:
        commission_value = sales * 0.05
    elif 500 <= sales <= 1000:
        commission_value = sales * 0.07
    elif 1000 <= sales <= 10000:
        commission_value = sales * 0.08
    elif sales >= 10000:
        commission_value = sales * 0.12
    else:
        error_value = True

elif city == 'Varna':
    if 0 <= sales <= 500:
        commission_value = sales * 0.045
    elif 500 <= sales <= 1000:
        commission_value = sales * 0.075
    elif 1000 <= sales <= 10000:
        commission_value = sales * 0.10
    elif sales >= 10000:
        commission_value = sales * 0.13
    else:
        error_value = True

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commission_value = sales * 0.055
    elif 500 <= sales <= 1000:
        commission_value = sales * 0.08
    elif 1000 <= sales <= 10000:
        commission_value = sales * 0.12
    elif sales >= 10000:
        commission_value = sales * 0.145
    else:
        error_value = True
else:
    error_value = True

if not error_value:
    print(f'{commission_value:.02f}')
else:
    print('error')

