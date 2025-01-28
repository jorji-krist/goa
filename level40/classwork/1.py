def password(st):
    if len(st) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in st:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return True
    else:
        return False
    
def is_isogram(string):
    string = string.lower()
    return len(string) == len((string))

def friend(x):
    result = []
    for name in x:
        if len(name) == 4:
            result.append(name)
    return result

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False