# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for i in geese:
        try:
            birds.remove(i)
        except:
            continue
    return birds