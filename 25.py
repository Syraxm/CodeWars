# https://www.codewars.com/kata/56582133c932d8239900002e/train/python
def most_frequent_item_count(collection):
    # Do your magic. :)
    # При пустом аргументе просто 0 :-|
    if collection == []:
        return 0
    # Создаём новый массив для результата
    a = []
    for i in collection:
        # С помощью цикла вписываем в новый массив количество повторений каждого эллемента
        a.append(collection.count(i))
    # Возвращаем максимальное кол-во повторений    
    return max(a)