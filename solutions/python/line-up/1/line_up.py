SUFFIXES = {'1': 'st', '2': 'nd', '3': 'rd'}

def line_up(name, number):
    number_s = str(number)
    if number_s[-1] in '123' and not number_s.endswith(('11', '12', '13')):
        prefix = SUFFIXES[number_s[-1]]
    else:
        prefix = 'th'
    return f'{name}, you are the {number}{prefix} customer we serve today. Thank you!'