def is_pangram(sentence):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    return all(letter in sentence for letter in alphabets)