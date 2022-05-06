import math

serial_name = input()
episode = int(input())
lunch_brake = int(input())

lunch = lunch_brake / 8
relax = lunch_brake / 4
time_left = lunch_brake - lunch - relax

# needed_time = math.ceil(episode - time_left)
needed_time = abs(episode - time_left)
# създаваме променлива с абсолютна стойност,
# за да се ползва долу и за оставащо и за недостигащо време
needed_time = math.ceil(needed_time)  # закръгляне

if episode <= time_left:
    print(f"You have enough time to watch {serial_name} and left with {needed_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {needed_time} more minutes.")
