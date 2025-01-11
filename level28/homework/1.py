def bool_to_word(b):
    if b:
        return "Yes"
    else:
        return "No"
    
def remove_char(s):
    return s[1:-1]

def string_to_number(s):
    return int(s)

def no_space(x):
    return x.replace(" ", "")

def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total