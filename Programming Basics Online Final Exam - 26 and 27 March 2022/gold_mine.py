count_locations = int(input())

for location in range(count_locations):
    expected_daily_production = float(input())
    count_days = int(input())

    total_production = 0
    for days in range(count_days):
        daily_amount = float(input())
        total_production += daily_amount

    real_daily_production = total_production / count_days
    if real_daily_production >= expected_daily_production:
        print(f"Good job! Average gold per day: {real_daily_production:.2f}.")
    else:
        difference = expected_daily_production - real_daily_production
        print(f"You need {difference:.2f} gold.")