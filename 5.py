# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
def count_smileys(arr):
    # Если список пустой, возвращаем 0
    if len(arr) == 0:
        return 0
    else:
        # Переменная a для результата
        result = 0
        for i in arr:
            # Если один из всех приемлимых вариантов есть, то отмечаем это в переменной
            if i in (':-)', ':~)', ':)', ':-D', ':~D', ':D', ';-)', ';~)', ';)', ';-D', ';~D', ';D'):
                result += 1
            # Если же его нет, продолжаем идти по циклу
            else:
                continue
        return result
