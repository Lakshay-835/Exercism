def response(hey_bob):
    response = None
    hey_bob = hey_bob.strip()
    if hey_bob.endswith('?') and hey_bob.isupper():
        response = "Calm down, I know what I'm doing!"
    elif hey_bob.endswith('?'):
        response = 'Sure.'
    elif hey_bob.isupper():
        response = 'Whoa, chill out!'
    elif hey_bob.isspace() or hey_bob == "":
        response = 'Fine. Be that way!'
    else:
        response = 'Whatever.'
    return response