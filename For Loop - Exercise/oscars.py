actor_name = input()
total_points = float(input())
number_of_jury = int(input())

for current_grade in range(number_of_jury):  # range(1,number_of_jury + 1)
    current_name = input()
    current_points = float(input())
    current_final_points = len(current_name) * current_points / 2
    # Точките,които актьора получава се формират от: дължината на името на
    # оценяващия умножено по точките, които дава делено на две.(формулата горе)
    total_points += current_final_points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
