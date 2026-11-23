from string import ascii_lowercase, ascii_uppercase

def rotate(text: str, key: int) -> str:
    shift = key % 26
    lower = ascii_lowercase
    upper = ascii_uppercase
    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]
    table = str.maketrans(lower + upper, shifted_lower + shifted_upper)
    return text.translate(table)