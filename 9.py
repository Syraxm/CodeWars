# https://www.codewars.com/kata/5601409514fc93442500010b/train/python
# Чёт изичные подкидывает код варс...
def better_than_average(class_points, your_points):
    # Можно решить в одну строку, но можно и в 2)
    # Создаём переменную с средним результатом класса

    mid_result = sum(class_points) / len(class_points)
    # И вернём True или False (пайтон сделает это за нас)
    return your_points > mid_result
