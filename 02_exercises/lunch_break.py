from math import ceil, floor

serial_name = input()
episode_lengh = int(input())
break_time = int(input())

lounch_time = break_time * 1 / 8
relax_time = break_time * 1 / 4
free_time = break_time - lounch_time - relax_time
left_time = free_time - episode_lengh

if free_time >= episode_lengh:
    print(f'You have enough time to watch {serial_name} and left with {ceil(left_time)} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(-left_time)} more minutes.")
