# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz') == set(s.lower().replace(' ', ''))