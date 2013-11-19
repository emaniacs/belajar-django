import random, string

def random_string(length=8):
    letters = string.ascii_letters
    digits = string.digits
    rand = ''.join([random.choice(letters + digits) for i in range(length)])
    
    return rand
