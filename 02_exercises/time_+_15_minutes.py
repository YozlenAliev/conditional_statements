hours = int(input())
minutes = int(input())

additional_minutes = minutes + 15
total_minutes = hours * 60 + additional_minutes

new_hours = total_minutes // 60
if new_hours >= 24:
    new_hours = 0
new_minutes = total_minutes % 60

print(f'{new_hours}:{new_minutes:02d}')
