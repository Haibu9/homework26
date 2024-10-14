
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team2_time + team1_time) / tasks_total

def work():
    print("В команде Мастера кода участников: %s ! " % team1_num + '\n'
    + "В команде Волшебники Данных %s участников! " % team2_num + '\n'
    + "Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num) + '\n'
    + "Команда Волшебники данных решили {1} задачи, а их соперники решили"
      " {0} задач!".format(score_1, score_2) + '\n' +
    "За время {t1}c. и {t2}c. соответственно".format(t1 = team1_time, t2 = team2_time) + '\n'
    f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        print('Победа команды Мастера кода!')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        print('Победа команды Волшебники Данных!')
    else:
        print('Ничья!')

work()