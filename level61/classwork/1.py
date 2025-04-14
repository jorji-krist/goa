def make_upper_case(s):
    return s.upper()

def repeat_str(times, string):
    return string * times

def no_space(x):
    return x.replace(" ", "")

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    
def monkey_count(n):
    return list(range(1, n + 1))