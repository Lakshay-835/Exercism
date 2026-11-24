ACTIONS = ('wink', 'double blink', 'close your eyes', 'jump')

def commands(binary_str):
    actions = [action for bit, action in zip(reversed(binary_str), ACTIONS) if bit == '1']
    return actions[::-1] if binary_str[0] == '1' else actions