from math import ceil, floor

holidays_per_year = int(input())

norm_playing = 30000
working_days = 365 - holidays_per_year
on_work = working_days * 63
on_holiday = holidays_per_year * 127
yearly_playing = on_work + on_holiday
play_needed = abs(norm_playing - yearly_playing)
hours = floor(play_needed / 60)
minutes = play_needed % 60

if yearly_playing < norm_playing:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
