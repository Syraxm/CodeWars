# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
def high_and_low(numbers):

    # Разделяем наш аргумент на части (перевод строки в массив)
    numbers1 = numbers.split()
    # Новый лист для повторения списка numbers1, но в int
    new_list = []
    # Цикл для добавления всех чисел, но в int
    for i in numbers1:
        new_list.append(int(i))
    # Возвращаем строку с макс. и мин. значением
    # *Не забудем про пробел*
    return str(max(new_list)) + " " + str(min(new_list))
    # Объяснять в принципе не было смыла, но ладно

    # А вот умные люди решали:
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])