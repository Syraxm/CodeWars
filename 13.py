# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
def find_uniq(arr):
    # Итак, узнаем какое число повторяется в лучшем случае
    if arr[0] == arr[-1]:
        # И если первое и последнее число равны, соответственно, среди них нет отличающегося
        # Поэтому проверим остальные числа в массиве, и если одно из них не равно первому (и соответственно последнему), значит оно отличающееся
        for i in arr:
            if i == arr[0]:
                continue
            # Нашли, прерываем цикл для вывода этого числа
            else:
                break
        return i
    # Если же они не равны, значит исключением является один из них
    else:
        # Если первый равен второму, то понятно, что исключение последнее число
        if arr[0] == arr[1]:
            return arr[-1]
        # А если нет, то первое
        else:
            return arr[0]
