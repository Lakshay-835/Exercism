def is_armstrong_number(number):
    number_str = str(number)
    length = len(number_str)
    sum_of_digits = 0
    for index in range(length):
        sum_of_digits += int(number_str[index]) ** length
    return sum_of_digits == number