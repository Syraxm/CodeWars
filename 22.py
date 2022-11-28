# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
def create_phone_number(n):
    # шизик решает:
    a = "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + str(n[3]) + str(n[4]) + str(n[5]) + "-" + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    return a

    # НОРМАЛЬНОЕ РЕШЕНИЕ:
    g = '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
    return g
        
    # я искренне не понял, почему не сработало:
    a = ["("]
    one = 3
    for i in n:
        a.append(i)
        one -= 1
        n.remove(i)
        if one == 0:
            break
    a.append(")")
    a.append(" ")
    one = 3
    for i in n:
        a.append(i)
        n.remove(i)
        one -= 1
        if one == 0:
            break
    a.append("-")
    for i in n:
        a.append(i)
    return "".join(map(str, a))
        