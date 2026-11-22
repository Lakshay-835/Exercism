def response(hey_bob):
    reply = None
    hey_bob = hey_bob.strip()
    if hey_bob.endswith('?') and hey_bob.isupper():
        reply = "Calm down, I know what I'm doing!"
    elif hey_bob.endswith('?'):
        reply = 'Sure.'
    elif hey_bob.isupper():
        reply = 'Whoa, chill out!'
    elif hey_bob.isspace() or hey_bob == '':
        reply = 'Fine. Be that way!'
    else:
        reply = 'Whatever.'
    return reply