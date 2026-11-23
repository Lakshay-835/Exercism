def is_valid(isbn):
    if not ('-' in isbn and len(isbn) == 13 or len(isbn) == 10) :
        return False
    validator = 0
    multiplier = 10
    semi_break_isbn = isbn.split('-')
    for number in semi_break_isbn:
        for digit in number:
            try:
                if digit == 'X' and multiplier == 1:
                    digit = 10
                validator += int(digit) * multiplier
                multiplier -= 1
            except ValueError:
                return False
    return validator % 11 == 0