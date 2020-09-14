import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def game_core_v3(number):
    '''После каждой попытки угадать число делим интервал пополам,
    проверям в какой половине число, делим данные интервал на 2 и т.д'''
    count = 0
    first_value = 1  # задаем начальное значение диапазона
    last_value = 101  # задаем конечное значение диапазона
    mean = 0
    while number != mean:
        count += 1
        mean = (first_value + last_value) / 2
        if number > int(mean):
            first_value = int(mean)
        elif number < int(mean):
            last_value = int(mean)
        else:
            return count


score_game(game_core_v3)
