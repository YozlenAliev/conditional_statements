speed = float(input())
result = 0

if speed <= 10:
    result = "slow"
elif speed <= 50:
    result = "average"
elif speed <= 150:
    result = "fast"
elif speed <= 1000:
    result = "ultra fast"
else:
    result = "extremely fast"

print(result)
