# https://www.codewars.com/kata/57d814e4950d8489720008db/train/python
def index(array, n):
    try:
        return array[n] ** n
    except:
        return -1
    # Мог бы рассписать с if, но было лень
