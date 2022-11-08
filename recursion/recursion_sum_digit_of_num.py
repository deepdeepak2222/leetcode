def sum_digit_num(num: int, sum_all=0):
    if num < 0:
        return -1
    if num < 10:
        return sum_all + num
    sum_all = sum_all + num % 10
    return sum_digit_num(int(num/10), sum_all)


sum_digit_num(123)
sum_digit_num(345)
sum_digit_num(45)
sum_digit_num(0)
