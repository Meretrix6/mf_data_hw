
import numpy as np

#Константы
MIN_NUMBER = 1
MAX_NUMBER = 101

def random_predict(number:int = 1, min_number:int = 1, max_number:int = 100) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    #Рекурсия которая сохращает кандидаты
    def predict(number, min_curr_number, max_curr_number, curr_count):
        curr_count += 1
        
        #Интересно сколько попыток будет = 8
 #      predicr_number = np.random.randint(min_curr_number, max_curr_number)

 #      Предпологаем число и отсекаем лишние кандидаты
        predicr_number = round(max_curr_number/2) + round(min_curr_number/2)
        if number == predicr_number:
            return curr_count
        elif number > predicr_number:
            return predict(number, predicr_number, max_curr_number, curr_count)
        else:
            return predict(number, min_curr_number, predicr_number, curr_count)
            
    count = predict(number, min_number, max_number, count)

    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(MIN_NUMBER,MAX_NUMBER, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number, MIN_NUMBER, MAX_NUMBER - 1))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)