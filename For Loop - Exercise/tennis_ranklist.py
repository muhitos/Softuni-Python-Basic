number_ot_tournaments = int(input())
starting_points = int(input())

points = 0
number_of_winning = 0
for _ in range(number_ot_tournaments):
    stage_of_tournaments = input()

    if stage_of_tournaments == 'SF':
        points += 720
    elif  stage_of_tournaments ==  'F':
        points += 1200
    elif stage_of_tournaments ==  'W':
        points += 2000
        number_of_winning += 1
average_points =  points / number_ot_tournaments
total_sum_of_points = starting_points + points

print(f'Final points: {total_sum_of_points}')
print(f'Average points: {int(average_points)}')
print(f'{number_of_winning / number_ot_tournaments * 100:.2f}%')