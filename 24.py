# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(string):
    # Летс го

    # Во-первых проверяем, не пустой ли аргумент
    # И если бог смиловался, возвращаем True
    if string == "":
        return True
    # Если же повезло меньше, то
    # 1. Сортируем массив для удобства
    # 2. Переводим в нижний регистр, дабы не было проблем с ним в будущем 
    string = sorted(string.lower())
    # Создадим переменную для индексов в условии (дальше понятно будет)
    a = 1
    # Проходимся по списку
    for i in string:
        try:
            # Если проверяемый эллемент равен следующему - False сразу же
            if i == string[a]:
                return False
            # Если же это не так, просто увеличим занчение a, чтобы в следующий раз проверить следующий эллемент
            else:
                a += 1
                # *продолжаем цикл*
                continue
        # Если же программа выдаст ошибку, знчит эллемента с таким индексом попросту нет
        # Соответственно, массив закончился, а повторений не найдено
        except:
        # И соответственно, этот массив нам подходит
            return True