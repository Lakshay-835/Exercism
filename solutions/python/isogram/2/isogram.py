def is_isogram(phrase):
    return all(phrase.lower().count(letter) == 1 for letter in phrase.lower() if letter.isalpha())