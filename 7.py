# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
def open_or_senior(data):
    # Уже по привычке сразу создаём переменную для вывода результата
    result = []
    # В этом случае результатом будет список
    # Пройдёмся по входным данным
    for i in data:
        # т.к формат входных данных обязует, идём по индксам
        if i[0] >= 55:
            # Чтобы лишний раз не проверять, сначало чекаем только возраст
            if i[1] > 7:
                # Если всё подходит, добавляем отметку сеньёр в список
                result.append("Senior")
            else:
                result.append("Open")
        else:
            result.append("Open")
    # Вернём результат
    return result
