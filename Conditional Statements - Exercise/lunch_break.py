import math

serial_name = input()
time_episode = int(input())
rest_time = int(input())


time_for_lunch = rest_time / 8
time_for_rest = rest_time / 4

time_left = rest_time - time_for_lunch - time_for_rest

needed_time = abs(time_episode - time_left)

needed_time = math.ceil(needed_time)

if time_left >= time_episode:
    print(f"You have enough time to watch {serial_name} and left with"
          f" {needed_time} minutes free time.")

else:
    print(f"You don't have enough time to watch {serial_name}, you need {needed_time} more minutes.")