world_record = float(input())
distance = float(input())
time_for_meter = float(input())

swimming_time = distance * time_for_meter
additional_time = distance // 15
delay_time = additional_time * 12.5
total_time = swimming_time + delay_time

if total_time < world_record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    seconds_needed = total_time - world_record
    print(f'No, he failed! He was {seconds_needed:.2f} seconds slower.')
