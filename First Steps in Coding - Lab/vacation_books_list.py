total_count_pages = int(input())
pages_hour = int(input())
count_days = int(input())

total_hours = total_count_pages // pages_hour

hours_per_day = total_hours / count_days

print(hours_per_day)
