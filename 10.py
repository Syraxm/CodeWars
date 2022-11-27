# https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python
def small_enough(array, limit):
    for i in array:
        if i <= limit:
            a = True
        else:
            a = False
            break
    return a
