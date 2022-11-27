# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
def get_grade(s1, s2, s3):
    sum_of_num = [s1, s2, s3]
    sum_of_num2 = sum(sum_of_num)/3
    if 90 <= sum_of_num2 <= 100:
        return "A"
    elif 80 <= sum_of_num2 < 90:
        return "B"
    elif 70 <= sum_of_num2 < 80:
        return "C"
    elif 60 <= sum_of_num2 < 70:
        return "D"
    elif 0 <= sum_of_num2 < 60:
        return "F"
