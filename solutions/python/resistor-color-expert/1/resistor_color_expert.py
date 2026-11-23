COLORS = {
    'black': [0],
    'brown' : [1, 1],
    'red' : [2, 2],
    'orange' : [3], 
    'yellow': [4], 
    'green' : [5, 0.5],
    'blue' : [6, 0.25], 
    'violet' : [7, 0.1], 
    'grey' : [8, 0.05], 
    'white' : [9],
    'gold' : [0, 5],
    'silver' : [0, 10]
}

prefix_identifier = ((10 ** 9, 'giga'), (10 ** 6, 'mega'), (10 ** 3, 'kilo'))

def resistor_label(colors):
    value = 0
    if colors[0] == 'black':
        return f'{value} ohms'
    *value_color, multiplier_color, tolerance_color = colors
    for color in value_color:
        value = value * 10 + COLORS[color][0]
    resistance = value * 10 ** COLORS[multiplier_color][0]
    prefix = ''
    for factor, unit_prefix in prefix_identifier:
        if resistance >= factor:
            resistance /= factor
            prefix = unit_prefix
    return f'{resistance:g} {prefix}ohms ±{COLORS[tolerance_color][1]}%'