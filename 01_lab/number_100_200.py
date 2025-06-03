number = int(input())
result = 0

if number < 100:
    result = "Less than 100"
elif number <= 200:
    result = "Between 100 and 200"
elif number > 200:
    result = "Greater than 200"

print(result)