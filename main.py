team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18500.3
team2_time = 18015.2
tasks_total = 82
time_avg = 350.4

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'победа команды Мастера Кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'


print ('В команде Мастера кода участников %s!' %team1_num)
print ('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print ('Команда Волшебники данных решила задач: {}!' .format (score_2))
print ('Волшебники данных решили задачи за {} с' .format (team2_time))
print (f'Команды решили {score_1} и {score_2} задач')
print (f'Результат битвы: {challenge_result}')
print (f'Сегодня было решено {tasks_total} зачад, в среднем по {time_avg} секунды на задачу')
